import paho.mqtt.client as mqtt

broker_address="192.168.4.19"    #broker address (your pis ip address)

def on_message(client, userdata, message):
	print(message.topic + " " + str(message.payload)) #print incoming messages

client = mqtt.Client() #create new client instance
client.connect(broker_address) #connect to broker

client.on_message=on_message #set the on message function

client.subscribe("/test") #subscirbe to topic

client.loop_start() #start client

try:
	while True:   # wait for ctrl-c
		pass

except KeyboardInterrupt:
	pass

client.loop_stop() #stop client
