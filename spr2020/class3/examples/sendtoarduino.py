import paho.mqtt.client as mqtt

broker_address="192.168.4.19" #broker address (your pis ip address)

client = mqtt.Client() #create new mqtt client instance

client.connect(broker_address) #connect to broker

client.loop_start() #start client

client.publish("/test","hey") #send message

client.loop_stop() #stop client
