#!/usr/bin/python

import os

ans=True
while ans:

    menu = {}
    menu['1']="Install Steghide" 
    menu['2']="Embed A File"
    menu['3']="Extract A File"
    menu['4']="Create A Hash"
    menu['5']="Exit"

    ans=raw_input('Please Select: ')
    if ans == '1': 
      os.system('sudo apt-get install steghide')
 
    elif ans == '2': 
      coverfile=raw_input('Enter the path and name of the file you want to embed in: ')
      print
      embedfile=raw_inout('Enter the path and name of the file you want to embed: ')
      print
      os.system('steghide embed -cf ' + coverfile + '-ef ' + embedfile)

    elif ans == '3':
       stegfile=raw_input('Enter the path and name of the file you want to extract from: ')
       print
       print('This will extract your file into the current directory.')
       print
       os.system('steghide extract -sf ' + stegfile)
    
    elif ans == '4':
     print
     print('This will set up a hash you can send to a friend.')
     print('Make sure to set up the password with the unencrypted string.')
     print('This is just helps keep things a little more secure when sending over the wire.')
     print
     password=raw_input('Enter a password using any characters you please: ')
     print
     os.sysem('echo ' + password + '| md5sum | sha512sum')    

    elif ans == '5': 
      break

    else: 
      print('Unknown Option Selected!')
