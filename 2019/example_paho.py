import paho.mqtt.client as mqtt #import the library


def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload)) #print incoming messages




broker_address="192.168.1.3"    #broker address (your pis ip address)

client = mqtt.Client("python client") #create new client instance
client.connect(broker_address) #connect to broker

client.on_message=on_message #set the on message function

client.subscribe("/test") #subscribe to topic

client.loop_start() #start client

#do something
if True:
    client.publish("/test2","test message") #publish


client.loop_stop() #stop client
