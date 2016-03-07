#!/usr/bin/python
'''
This is a topology generation program. Over the years, I have lost interest in building a topology from scratch by creating a router, adding port-adapters to the slot and connecting the interfaces. The goal of this program is to create a automagic way of creating a topology based only on the number of routers.

It is well known that dynampis support Cisco 7200 platforms and this platform has 8 slots. PA-8T is a serial port adapter. The program creates a topology file (.net file which is used as an input to GNS3) for a maximum of 9 routers. Each router would then connect to 8 other routers excluding itself and the topology would have 36 links.
'''
#The number of routers is taken as an input form the command line argument. argv module is imported.
from sys import argv
#Error handling to get the required number of arguments.
if(len(argv)< 2):
    print "Sorry, missing router count value. Please enter the number of routers required in the topology"
    exit()
#unpack the variables from the argv list to the respective variables.
program_name, router_count = argv
#One of the issue with taking input from the cmd line is argv holds variables as strings.
#print type(router_count)
#For all our purposes, we need the router_count to be as a integer rather than string!
router_count = int(router_count)

def full_mesh(a):
        x = 0
        a += 1
        local_slot = 1
        remote_slot = 1
        local_port = 0
        remote_port = 0
        console_port = 2101
        aux_port = 2501
        print '''
        autostart = False
        version = 0.8.6
        [127.0.0.1:7201]
            workingdir = working
            udp = 10101
            [[7200]]
                image = /Volumes/Macintosh HD/2TB Backup/My Juniper Work Folder/Cisco Tools/Cisco IMAGES/7200/C7200-AD.BIN
                sparsemem = True
                ghostios = True
        '''
        for i in range(1, a):
            print " [[Router R%d]]" %(i)
            print "     console = %d" %(console_port)
            print "     aux = %d" %(aux_port)
            print "     slot1 = PA-8T"
            print "     cnfg = /Users/sharath/Desktop/GNS3_Desktop/configs/R%d.cfg" %(i)
            x += 1 
            for j in range(x,a):
                if(i==j): #Router does not connect to itself
                    continue
                print "     s%d/%d = R%d s%d/%d" %(local_slot,local_port,j,remote_slot,remote_port)
                local_port += 1
            remote_port += 1
            local_port = remote_port
            console_port += 1
            aux_port += 1    
full_mesh(router_count)    
