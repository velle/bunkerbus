from em340 import EM340

m = EM340()
m.setFields(['kWh','kWh_L1','kWh_L2','kWh_L3'])

for modbus_addr in [1,2,3,4,5,6]:
    influxLine = collectAsInfluxLine(modbus_addr)
    influxdb.inject(influxLine)
