import os
a = input("używasz skryptu pierwszy raz? (y/n) ")
print("okeej")
if a == 'y':    
    os.system('wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh')
    os.system('sudo install ubuntu-mainline-kernel.sh /usr/local/bin/')
    os.system('sudo ubuntu-mainline-kernel.sh -i')
else:
    os.system('sudo ./ubuntu-mainline-kernel.sh -i')