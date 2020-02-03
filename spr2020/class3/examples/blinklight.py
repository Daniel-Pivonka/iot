import paho.mqtt.client as mqtt
import time

broker_address="192.168.4.19" #broker address (your pis ip address)

client = mqtt.Client() #create new mqtt client instance

client.connect(broker_address) #connect to broker

client.loop_start() #start client

client.publish("/led","on") #send message

time.sleep(1)

client.publish("/led","off") #send message

time.sleep(1)

client.publish("/led","on") #send message

time.sleep(1)

client.publish("/led","off") #send message

time.sleep(1)

client.publish("/led","on") #send message

time.sleep(1)

client.publish("/led","off") #send message

client.loop_stop() #stop client
