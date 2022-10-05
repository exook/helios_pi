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

## Finding the IP address of your Raspberry Pi
### Linux (UBUNTU)
* Go to network settings
* Under "Wired" make sure that the toggle switch ofr "Connected" is truned on
* Click the cog wheel next to the toggle switch
* Go to IPv4 and selkect "Shared to other computers"
* Click Apply
* Open a terminal
* `arp -a`
* The Ip address of the reaspberry pi is listed after the question mark
 * For me this looks like: `? (10.42.0.248) at e4:5f:01:a7:8c:ab [ether] on enp0s31f6`

### MAC
### Windows

## Connecting via SHH first, in order to set up VNC later
* Connect to the Raspberry Pi with ssh
  * On Linux/Mac OS, write the command in a terminal:
    * `ssh pi@[raspberrypi_name].local`
  * On Windows machine install putty: https://www.putty.org/
* When connected via shh do:
  * `raspi-config`
  * Enable the "VNC Client" and quit the application
  * `sudo reboot --force`
* The Raspberry Pi will be up and running in ~ 1 min

## Connecting via VNC
* Install a VNC client on your computer: https://www.realvnc.com/en/connect/download/viewer/
* Open Real VNC on your computer
  * The address of the raspberry pi is: [raspberrypi_name].local
* Set up wifi
* Update
* Gett all python packages
* Clone HELIOS repository
* Start notebook
