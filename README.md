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
* Connect to the Raspberry Pi with ssh
  * On Linux/Mac OS, write the command in a terminal: ssh pi@[raspberrypi_name].local
  * On Windows machine install putty: https://www.putty.org/
* When connected via shh do:
  * `raspi-config`
  * Enable the "VNC Client" and quit the application
  * `sudo reboot --force`

## Second Boot
* The Raspberry Pi will be up and running in ~ 1 min
* Install a VNC client on your computer: https://www.realvnc.com/en/connect/download/viewer/
* Connect to the Raspberry Pi with the VNC client
  * The address of the raspberry pi is: [raspberrypi_name].local
* Set up wifi
* Update
* Gett all python packages
* Clone HELIOS repository
* Start notebook
