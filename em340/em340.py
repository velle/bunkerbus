#!/usr/bin/env python3
from meter import ModbusElectricityMeter

class EM340(ModbusElectricityMeter):
    _REGISTERS = [
        ('V_L1',0),
        ('V_L2',2),
        ('V_L3',4),
        ('A_L1',12),
        ('A_L2',14),
        ('A_L3',16),
        ('kWh_L1',64),
        ('kWh_L2',66),
        ('kWh_L3',68),
    ]
