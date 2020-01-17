#! /bin/sh
#
# setup-script.sh
# Copyright (C) 2019 Chris Odom, Jeff Brown, Daniel Pivanka, Joel Savitz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

# TODO:
# - imotion setup

EXIT_SUCCESS=0
EXIT_FAILURE=1

usage() {
	cat <<-EOF
	=== fedora-rpi setup script ===
	usage: setup-script.sh [FLAGS]

	available flags:
		-n: do not create default rpi/rpi user
		-s: skip installation of packages via dnf
		-h: show this message and exit
EOF
}

die_at() {
	cat <<-EOF
	>Fatal error occured at: $1
	>You should fix any errors described above and re-run this script
	>Exiting with failure...
EOF
	exit $EXIT_FAILURE
}

# X and window manager related packages
PKGS_X="xorg-x11-server-Xorg xorg-x11-xinit xorg-x11-xauth dbus-x11 enlightenment"

# desktop applications and other utilities
PKGS_APPS="terminator firefox git bc screenfetch"

# latest RPi.GPIO compatibility layer
# TODO:
# 	- new version with bug fixes
#	- submit to fedora repositories
PKGS_GPIO="https://github.com/underground-software/python3-libgpiod-rpi/releases/download/v0.1/python3-libgpiod-rpi-0.1-1.aarch64.rpm"

# useful libraries: right now this just enables audio
PKGS_LIBS="alsa-plugins-pulseaudio"

NO_USER=""
SKIP_DNF=""
while getopts "nsh" OPTION; do
	case ${OPTION} in
		n)
			NO_USER=y
			;;
		s)	
			SKIP_DNF=y
			;;
		h)
			usage
			exit $EXIT_SUCCESS
			;;
		*)
			echo "Unknown option $OPTION, ignoring"
			;;
	esac
done
shift $((OPTIND -1))

# validate that the user is root
if [ ! $UID -eq 0 ]
then
	echo "This script must be run as root"
	die_at "root user validation"
fi

# set the GPU memory to 80 (default 32) to support camera
if [ $(grep "gpu_mem=32" /boot/efi/config.txt) ]
then
	sed -i s/gpu_mem=32/gpu_mem=80/g /boot/efi/config.txt || die_at "gpu_mem config tweak"
fi

if [ -z "$SKIP_DNF" ]
then
	# update the fedora packages
	dnf -y update || die_at "initial dnf update"

	# install window manager and prereqisites
	dnf install -y $PKGS_X || die_at "X and window manager installation"
	dnf install -y $PKGS_APPS || die_at "Apps installation"
	dnf install -y $PKGS_GPIO || die_at "GPIO installation"
fi

# unless user sepcifies not to, add rpi/rpi user with sudo privileges
if [ -z "$NO_USER" ]
then
	$( [ ! -z "`grep rpi /etc/passwd`" ] || useradd rpi) || die_at "create user rpi"
	echo "rpi" | passwd rpi --stdin || die_at "set user rpi password"
	echo 'rpi ALL=(ALL:ALL) ALL' >> /etc/sudoers || die_at "add rpi user to sudoers"
	export RPIHOME="/home/rpi"
else
	export RPIHOME="/root"
fi



# configure the window manager
echo ". /etc/X11/xinit/xinitrc-common" > $RPIHOME/.xinitrc || die_at "add common xinitrc code to local file"
echo "exec enlightenment_start" >> $RPIHOME/.xinitrc || die_at "add enlighement_start to xinitrc"


cat <<-EOF
	=== setup script completed with success ===
	====== to start the GUI, run: startx ======
EOF

exit $EXIT_SUCCESS
