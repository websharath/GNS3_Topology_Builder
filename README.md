# GNS3_Topology_Builder
This python script automates Building Cisco 7200 based router topology and creates IOS Configurations for that topology.
Based on the number of routers which is taken as an argument, the program generates a ".net" topology file which has a full mesh connectins to all other routers.
The program assumes the routers have Cisco 7200 based image and uses PA-8T as the module for connecting serial links.

gns3_topology_gen.py generates a ".net" file and contains the topology information.
file_config_gen.py generates IOS configurations for all the routers (Interface configurations, Loopback and IGP (OSPF))

