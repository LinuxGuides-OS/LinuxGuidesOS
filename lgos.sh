#!/bin/bash
if [ "$EUID" -ne 0 ]
	then echo "Bitte führe das SKript als root aus"
	exit
fi
rm -r /root/linuxguidesos/
apt install sudo xfce4 git vim curl snapd flatpak -y
mkdir /root/linuxguidesos/
git clone https://github.com/LinuxGuides-OS/LinuxGuidesOS.git /root/linuxguidesos

#OS-Release einrichten
cp /root/linuxguidesos/DesignTests/DesignTest-1/os-release /etc/os-release
cp /root/linuxguidesos/DesignTests/DesignTest-1/os-release /usr/lib/os-release

#neofetch einstellen
cp /root/linuxguidesos/neofetch /usr/bin
chmod +x /usr/bin/neofetch

#Hintergrund einstellen
mkdir /usr/share/backgrounds/linuxguides
cp /root/linuxguides/Wallpaper/* /usr/share/backgrounds/linuxguides
