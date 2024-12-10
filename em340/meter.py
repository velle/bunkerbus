class ModbusElectricityMeter:
    _REGISTERS = None
    _fields = None

    def setFields(self, l):
        self._fields = l

    def collect(self, modbus_addr):
        resultdict = {}
        for fieldname in self._fields:
            regaddr = _REGISTERS[fieldname]
            resultdict[fieldname] = instrument.read_register(regaddr)
            time.sleep(0.5)
        return resultdict

    def collectAsInfluxLine(self, modbus_addr):
