echo -e "
\033[32m\033[1mWillkommen bei den LinuxGuidesOS ISO Installer.\033[0m
Wir werden LinuxGuidesOS direkt auf ihrem PC Installieren. Viel Spaß mit LinuxGuidesOS!

\033[31m\033[1mInstaller Version 1.0.1\033[0m

Link-Quellen:
- \033[34mhttps://linuxguides-os.github.io/site/\033[0m
- \033[34mhttps://github.com/LinuxGuides-OS\033[0m
- \033[34mhttps://linuxguides-os.de/\033[0m

Downloadinformationen:
- Downloadserver: \033[34mhttps://cd.linuxguides-os.de/alpha/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso\033[0m
- Installierer: wget
- Dateigröße: 1.5GB
- Installationspfad: ${HOME}/LinuxGuidesOS-Installer/linuxguidesos-21_04_2-/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso

Installer geschrieben von Julian > \033[34mhttps://github.com/Juliaaan2502\033[0m
"

# Zum Home Verzeichniss Navigieren
cd /home/$USER

# Neuen Ordner erstellen für LGOS
mkdir LinuxGuidesOS-Installer

# Im LGOS Ordner Navigieren
cd LinuxGuidesOS-Installer/

# Neuen Ordner für die ISO erstellen
mkdir linuxguidesos-21_04_2-alpha

# In den Ordner Navigieren
cd linuxguidesos-21_04_2-alpha/

echo -e "\033[1m**************Installiervorgang...**************\033[0m
"
# In den Ordner die ISO rein downloaden
wget https://cd.linuxguides-os.de/alpha/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso

