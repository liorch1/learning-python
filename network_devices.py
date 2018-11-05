#!/usr/bin/env 
###/usr/share/nmap/nmap-mac-prefixes
###
###
import netifaces


def get_interface():
	return netifaces.interfaces()

dic = {}

for inter in get_interface():
	i = netifaces.ifaddresses(inter)[netifaces.AF_LINK][0]['addr']
	i = i.replace(':', '')[:6].upper()
	dic[inter] = i


for x, y in dic.items():
	for mac in open('/usr/share/nmap/nmap-mac-prefixes', 'r'):
		if y == mac[:6]:
			print('your interface  vendor for "{}" is {}'.format(x,mac))
