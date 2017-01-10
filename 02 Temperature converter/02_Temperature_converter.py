# Task 02 Temperature converter from Pro/g/ramming Challanges [Made by Anonymous in January 2015]
# Temperature scales:
# [C]elcius
# [F]arenheit
# [K]elvin
# [R]ankine
# [Re]aumur
# [Ro]mer
# [De]lisle
# [N]ewton
from sys import exit


def temperature_converter(scale, source_temperature):
	if scale in ('f', 'F'):
		t_celcius = (source_temperature - 32.0)/1.8
		t_farenheit = source_temperature
		t_kelvin = (source_temperature + 459.67) * (5.0/9.0)
		t_rankine = (source_temperature + 459.67)
		t_reaumur = (source_temperature - 32.0) * (4.0/9.0)
		t_romer = (source_temperature - 32.0) * (7.0/24.0) + 7.5
		t_delisle = (121 - source_temperature) * (5.0/6.0)
		t_newton = (source_temperature - 32.0) * (11.0/60.0)
		return {'[*C]':t_celcius, '[*F]':t_farenheit, '[*K]':t_kelvin, '[*R]':t_rankine, '[*Re]':t_reaumur, '[*Ro]':t_romer, '[*De]':t_delisle, '[*N]':t_newton}
	elif scale in ('c', 'C'):
		t_celcius = source_temperature
		t_farenheit = (source_temperature * 1.8) + 32.0
		t_kelvin = (source_temperature + 273.13)
		t_rankine = (source_temperature + 273.15) * 1.8
		t_reaumur = (source_temperature * 4.0)/5.0
		t_romer = (source_temperature * (21.0/40.0)) + 7.5
		t_delisle = (100 - source_temperature) * (3.0/2.0)
		t_newton = source_temperature * (33.0/100.0)
		return {'[*C]':t_celcius, '[*F]':t_farenheit, '[*K]':t_kelvin, '[*R]':t_rankine, '[*Re]':t_reaumur, '[*Ro]':t_romer, '[*De]':t_delisle, '[*N]':t_newton}
	elif scale in ('k', 'K'):
		t_celcius = (source_temperature - 273.15)
		t_farenheit = (source_temperature * 1.8) - 459.67
		t_kelvin = source_temperature
		return {'[*C]':t_celcius, '[*F]':t_farenheit, '[*K]':t_kelvin}

scale = input("Select [F]aranheit, [C]elcius or [K]elvin scale: ")
if scale in ('f', 'F', 'c', 'C', 'k', 'K'):
	pass
else:
	print("You need to select [F]aranheit, [C]elcius or [K]elvin scale.")
	exit(0)
source_temperature = float(input("What is the temperature: "))

for keys, values in temperature_converter(scale, source_temperature).items():
	print("%.2f" % source_temperature, "[*", scale, "] =", "%.2f" % values, keys)
	