# HELIOS Raspberry Pi Course
Follow these instructions to get started with the HELIOS Raspberry Pi Course

## Install the operating system
* Download the Raspberry Pi imager to your computer: https://www.raspberrypi.com/software/
* Insert the Micro SD card into a card reader
* Start the imager
* Select "Raspberry Pi OS (32-bit)" as operating system
* Select your Micro SD card as the choosen storage
* Click the cog wheel icon for advanced options
* Check the box "Set hostname"
  * Set the host name to "Raspberrypi1" or "Raspberrypi2", follwoing the number given on your package
* Check the box "Enable SSH"
* Check the box "Set username and password"
  * Set username "pi"
  * Set your own, secret, password
* Click "Save"
* At the main window, click "Write"
  * Be patient and wait for the writing to finish

## First Boot
* Insert the SD card into the SD card slot on the Raspberry Pi
* Connect the Raspberry Pi to your computer via the ethernet cable
* Connect the Raspberry Pi to power
* Wait 2-3 minutes for the Raspberry Pi to power up, wait until the green LED stops blinking

## Connecting via SHH first
### Linux (UBUNTU)
* Go to network settings
* Under "Wired" make sure that the toggle switch ofr "Connected" is truned on
* Click the cog wheel next to the toggle switch
* Go to IPv4 and selkect "Shared to other computers"
* Click Apply
* Connect to the Raspberry Pi with ssh
  * `ssh pi@[raspberrypi_name].local`

### MAC
### Windows

# Setting up Raspberry Pi via SSH
* When connected via SSH do set up the WiFi connection.
  * `sudo raspi-config`
  * Navigate to "System Options", then "Wireless LAN"
    * For "SSID" enter the name of the netwokr, press enter
    * Fpr passphrase, enter the passwrod for the network. Press neter
    * Vack at the main menue, use thre right arrow key twice to mark "Finish", then press enter
* Execute the following commands to setup the different interfaces of the reaspbery pi
  * `sudo raspi-config nonint do_vnc 0`
  * `sudo raspi-config nonint do_i2c 0`
  * `sudo raspi-config nonint do_spi 0`
  * `sudo raspi-config nonint do_rgpio 0`
* Execute these commands to update and isntall necessary software to the pi
  * `sudo apt update`
  * `sudo apt full-upgrade`
  * `pip install notebook`
  * `pip install jupyterplot`
* Execute this command to reboot
  * `sudo reboot`

## Connecting via VNC
* Install a VNC client on your computer: https://www.realvnc.com/en/connect/download/viewer/
* Open Real VNC on your computer
  * The address of the raspberry pi is: [raspberrypi_name].local
* Set up 
* Update
* Gett all python packages
* Clone HELIOS repository
* Start notebook
