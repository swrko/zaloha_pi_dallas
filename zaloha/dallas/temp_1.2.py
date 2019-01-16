#multidallas python return temp in celsia
#change boot config to enable w1 at pin 4
import os
import glob
import time
import sys
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


slave_number_dir = '/sys/bus/w1/devices/w1_bus_master1/'
slave_number_file = slave_number_dir + 'w1_master_slave_count'
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] # field contains all the results of globe -> finded devices
device_file = device_folder + '/w1_slave'
device_name = device_folder + '/name'
def read_name():
	f = open(device_name, 'r')
	name = f.readline()
	f.close() #print('device_name =   ' + name)
	return name
	
# finds out a number of slave devices connected to the w1 bus
def read_slave_num():
	f = open(slave_number_file, 'r')
	number_of_slaves = f.readline()
	f.close()
	return int( number_of_slaves )

# read raw temperature data from slave dir
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

number_of_slaves = read_slave_num()

while True:
	for x in range(0, number_of_slaves):
		device_folder = glob.glob(base_dir + '28*')[x]
		device_file = device_folder + '/w1_slave'
		device_name = device_folder + '/name'
		print('slave_name: {0}temp: {1} '.format( read_name(), read_temp() ))
		#print(read_temp())	
	sys.stdout.flush()
	time.sleep(900)
	