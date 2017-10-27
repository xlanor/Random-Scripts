#!/usr/bin/env bash

#Leaves the latest two installed kernels,
#If yum utils is not installed dnf install yum-utils

package-cleanup --oldkernels --count=2

echo Sucesfully cleaned up old kernels...

#refresh grub for EFI
grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

echo Grub has been refreshed....

i=0
while [ $i -ne 1 ]
do
	echo "Do you want to perform a reboot?(y/n): "

	read answer

	if [ $answer == 'y' ]
	then
		echo "Rebooting now"
		#do a reboot
		i=$((i + 1))
		reboot
	elif [ $answer == 'n' ]
	then
		i=$((i + 1))
		echo "Exiting script"
		exit 0
	else
	echo "I don't recognise that input, please try again."
	fi
done

