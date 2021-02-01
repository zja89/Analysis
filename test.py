import serial

ser = serial.Serial(port="COM15",baudrate=115200)

import time
# ser.setRTS(True)
# time.sleep(0.1)
ser.setRTS(False)   # 高
# time.sleep(0.5)
# ser.setRTS(True)
time.sleep(50)