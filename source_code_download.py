#!/usr/bin/python3
#Get any website source just one click
from termcolor import colored

print (colored("********************Any Site To Source Code Download****************",'green'))
print(colored("*********************Create By 0xanon_hash***************************",'red'))
import turtle  # import package
import urllib.request as u

import pyfiglet  # import banner package

banner = colored(pyfiglet.figlet_format("Source Code Downloader"),'green') #use for banner
print(banner)
website_name = turtle.textinput("Dimani Name","Url Address") #animation input from user
source_open =u.urlopen(website_name)
source_read=source_open.read()
print(source_read)
