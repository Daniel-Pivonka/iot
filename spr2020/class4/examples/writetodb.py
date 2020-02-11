from influxdb import InfluxDBClient
import datetime

# Set up a client for InfluxDB
dbclient = InfluxDBClient('0.0.0.0', 8086, 'root', 'root', 'mydb')

#get current time
receiveTime=datetime.datetime.utcnow()

#create json to insert into db
json_body = [
	{
		"measurement": 'test',
		"time": receiveTime,
		"fields": {
			"value": 99.9
		}
	}
]

#write to db
dbclient.write_points(json_body)
print("Finished writing to InfluxDB")
