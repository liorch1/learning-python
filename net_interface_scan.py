#!/usr/bin/env python36


#####
#
#
#
######

import os
import sys

a_list = []
print('looking for mac addresses!')

net_scan = os.popen('arp -a').readlines() 
print ('finished looking ')
for i in net_scan:
	filed = i.strip().split()
	a_list.append(filed[3][:8].replace(':','').upper())
	
for i in open('/usr/share/nmap/nmap-mac-prefixes', 'r'):
	if i[:6] in a_list:
		print(i)

print(a_list)
