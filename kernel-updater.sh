echo "używasz skryptu pierwszy raz czy nie? (y/n)"
read czy
clear
if[ $czy == 'y' ]
then
	wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh
	sudo install ubuntu-mainline-kernel.sh /usr/local/bin/
	./ubuntu-mainline-kernel.sh -i
else
	./ubuntu-mainline-kernel.sh -i
fi