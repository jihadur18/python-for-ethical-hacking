#! /usr/bin/python3
from termcolor import colored

print (colored("********************Domain To IP Convertor****************",'green'))
print(colored("*********************Create By 0xanon_hash***************",'red'))

import socket

import pyfiglet

banner = colored(pyfiglet.figlet_format("Domain To IP"),'green')
print(banner)
domain_name = input("Enter yur target domain:")
ip = socket.gethostbyname(domain_name)
print("IP for {} : {}".format(domain_name,ip))


