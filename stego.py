import os

os.system('cls' if os.name == 'nt' else 'clear')

ans=True
while ans:
    print
    print ('====================================')
    print ('#           STEGANOGRAPHY          #')
    print ('====================================')
    print("1. Install Steghide")
    print("2. Embed A File")
    print("3. Extract A File")
    print("4. Exit")
    print ('====================================')
    ans=input("What would you like to do? Enter your selection: ")

    if ans == '1': 
      os.system('sudo apt-get install steghide')
 
    elif ans == '2': 
      coverfile=input('Enter the name of the file you want to embed in: ')
      print
      embedfile=input('Enter the name of the file you want to embed: ')
      print
      os.system('steghide embed -cf ' + coverfile + ' -ef ' + embedfile)

    elif ans == '3':
       stegfile=input('Enter the name of the file you want to extract from: ')
       print
       print('This will extract your file into the current directory.')
       print
       os.system('steghide extract -sf ' + stegfile)    

    elif ans == '4': 
      break

    else: 
      print('Unknown Option Selected!')
