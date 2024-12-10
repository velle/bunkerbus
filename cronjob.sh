FIELDS=kWh,kWh_L1,kWh_L2,kWh_L3,U_L1,U_L2,U_L3

# collect_{METER_TYPE}.py may be able to output several types of results:
# 1) json, 2) csv string, 3) influxdb line

collect_ob737.py 001 $FIELDS
