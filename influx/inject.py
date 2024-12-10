from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
# client = InfluxDBClient(host='mydomain.com', port=8086,
#     username='myuser', password='mypass',
#     ssl=True, verify_ssl=True)
#client.create_database('pyexample')


json_body = [
    {
        "measurement": "electricity_meters",
        "tags": {
            "id": "m001",
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "kWh": 127
        }
    }
]
