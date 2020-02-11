from influxdb import InfluxDBClient

# Set up a client for InfluxDB
dbclient = InfluxDBClient('0.0.0.0', 8086, 'root', 'root', 'mydb')

#database query
query = 'select mean("value") from "light"'

#make query
result = dbclient.query(query)

print (result)   

#get value inside result
mean = list(result.get_points(measurement='light'))[0]['mean']
print(mean)