#!/usr/bin/python
from sys import argv
import os

filename, router_number = argv
router_number = int(router_number)
#address_generation routine starts here
address = {}
def address_configuration(a):
    x = 0
    a += 1
    for i in range(1,a):
        x += 1
        for j in range(x,a):
            if (i == j):
                continue
            address[''.join("%d%d") %(i,j)] = ''.join("10.%d.%d.1") %(i,j)
            address[''.join("%d%d") %(j,i)] = ''.join("10.%d.%d.2") %(i,j)
    sorted_keys = address.keys()
    sorted_keys.sort()
    return sorted_keys

address_list = address_configuration(router_number)

#create the list of configuration files that needs to be generated for this topology based on the input router count
file_list = []
for router_config_file in range(0,(router_number+1)):
    file_list.append("R%d.cfg" %(router_config_file))


#function to generate the configuration and write to a file.
def config_gen(a):
    a += 1
    subnet_mask = "255.255.255.252"
    ospf_igp_area = "area 0"
    index_of_sorted_list = 0
    for i in range(1,a):
        fh = open(file_list[i],'w')
        fh.write("!\n")
        fh.write("hostname R%d\n" %(i))
        fh.write("!\n")
        fh.write("no ip domain lookup\n")
        fh.write("!\n")
        fh.write("interface loopback0\n")
        fh.write(" ip address %d.%d.%d.%d 255.255.255.255\n" %(i,i,i,i))
        fh.write(" ip ospf %d %s\n" %(i,ospf_igp_area))
        fh.write("!\n")
        for j in range(0,(a-1)-1):
            fh.write("interface serial1/%d\n" %(j))
            fh.write(" ip address %s %s\n" %(address[address_list[index_of_sorted_list]], subnet_mask))
            fh.write(" ip ospf %d %s\n" %(i,ospf_igp_area))
            fh.write("!\n")
            index_of_sorted_list += 1
        fh.write("router ospf %d\n" %(i))
        fh.write(" router-id %d.%d.%d.%d\n" %(i,i,i,i))
        fh.write(" log-adjacency-changes")
        fh.write('''
!
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
 length 0
 stopbits 1
line aux 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
 stopbits 1
line vty 0 4
 login
!
!
end
''')

config_gen(router_number)
            
        
        