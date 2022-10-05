# HELIOS Raspberry Pi Course
These are the instructions to get started with the HELIOS Raspberry Pi Course. It will take you from a blank Raspberry Pi to running a Jupyter notebook on the Raspberry Pi which controls different electrical components.

When reading these isntructions, the bullet points mark different steps, and the grey "code boxes" mark code to be executed. It is often very handy to triple-click these grey boxes to mark all its content, and then use ctrl+C and ctrl+V (ctrl+shift+V on Ubuntu) to paste this in the rapsberry Pi terminal.

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
  * Mage sure that "Use password authentication" is selected
* Check the box "Set username and password"
  * Set username "pi"
  * Set your own, secret, password
* Check the box "Configure wireless LAN"
  * At "SSID" enter the WiFi name
  * At "Password" enter the WiFi password
  * At "Wireless LAN country" select SE
* Check "Set locate settings"
  * Leave "Time zone" as "Europe/Stockholm"
  * Select "Keyobard layout" as your keyboard layout, probably "se"
*  Un-check the box "Enable telemetry"
* Click "Save"
* At the main window, click "Write"
* Click "Yes" when prompted taht all existing data will be erased
  * Be patient and wait for the writing and verification to finish
  * This takes roughly 15 minutes

## First Boot
* Insert the SD card into the SD card slot on the Raspberry Pi
* Connect the Raspberry Pi to your computer via the ethernet cable
* Connect the Raspberry Pi to power
* Wait 2-3 minutes for the Raspberry Pi to power up, wait until the green LED stops blinking

## Connecting via SSH
### Linux (UBUNTU)
* Go to network settings
* Under "Wired" make sure that the toggle switch ofr "Connected" is truned on
* Click the cog wheel next to the toggle switch
* Go to IPv4 and selkect "Shared to other computers"
* Click Apply
* Connect to the Raspberry Pi with ssh
  * `ssh pi@[raspberrypi_name].local`
* If you have trouble conneting, try powering off and on the Raspberry Pi

### MAC
### Windows

## Setting up Raspberry Pi via SSH
* When connected via SSH do set up the WiFi connection.
* Execute the following commands to setup the different interfaces of the reaspbery pi
  * `sudo raspi-config nonint do_vnc 0`
  * `sudo raspi-config nonint do_i2c 0`
  * `sudo raspi-config nonint do_spi 0`
  * `sudo raspi-config nonint do_rgpio 0`
* Execute these commands to update and isntall necessary software to the pi
  * `sudo apt update`
  * `sudo apt full-upgrade`
  * `pip install -U numpy`
  * `pip install notebook`
  * `pip install jupyterplot`
* Get the wired IP address of the Raspberry Pi
  *  `ifconfig`
  *  Under "eth0" it lists something like "inet 10.42.0.248"
  *  When connecting to the Pi later, this can be useful in addition to the "[raspberrypi_name].local"
* Execute this command to reboot
  * `sudo reboot`

## Optional: Connecting via VNC (Full graphical desktop environment of the Raspberry Pi)
* Install a VNC client on your computer: https://www.realvnc.com/en/connect/download/viewer/
* Open Real VNC on your computer
  * The address of the raspberry pi is: [raspberrypi_name].local
* In the top left, use the black suqare icon to open a terminal window

## Optional: Starting the Jupyter notebook with VNC
* Open a terminal
* Navigate to the Desktop
  * `cd Desktop`
* Clone the code respository:
  *  `git clone https://github.com/exook/helios_pi.git`
*  Enter the new directory
  *  `cd helios_pi/`
* Start the notebook:
  * `jupyter notebook`
* In the browser window, open "helios_pi.ipynb"
* You are ready to go!

## Running the Jupyter notebook without VNC (Less laggy)
* If you think the VNC is a bit slow or laggy you can try this method
* Connect to your raspberry Pi via SSH
  * `ssh pi@[raspberrypi_name].local`
* Navigate to the correct directory
  * `cd Desktop/helios_pi/`
* Start the notebook without a browser, and with as pecific port
  * `jupyter notebook --no-browser --port=8080`
* Copy the "localhost" URL and token given. Example below, but your token will be different:
  * `http://localhost:8080/?token=6d587c101ecd1c75ffa640675a6aaae9179c5118db79f4e4`
* Open a new terminal on your **PC** and run the following command:
  *  `ssh -L 80880:localhost:8080 pi@[raspberrypi_name]`
* Open the browser on your **PC** and enter URL that you copied earlier
* The Jupyter notebook now runs on your RAspberry Pi, but you can itneract with it in your browser, which is faster than VNC
* Not that if you do this in the future, pick a port number that is not standard or often listed on the internet as this can make the Raspberry Pi vulnerable to attacks

## If you need to re-configure WiFi from terminal
  * `sudo raspi-config`
  * Navigate to "System Options", then "Wireless LAN"
    * For "SSID" enter the name of the netwokr, press enter
    * Fpr passphrase, enter the passwrod for the network. Press neter
    * Back at the main menue, use thre right arrow key twice to mark "Finish", then press enter
