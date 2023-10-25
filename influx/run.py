# this script generates a table by querying influxdb
# the table contains data for
#


for meter in meters:
    entity_id = getid(meter)
    timeFilter = """ time >= '2015-08-18T00:06:00Z' AND time <= '2015-08-18T00:06:00Z' """
    influxquery('select first(value) from kWh where (entity_id='$entity_id') AND $timeFilter', entity_id, timeFilter)
    #time >= '2015-08-18T00:06:00Z'
