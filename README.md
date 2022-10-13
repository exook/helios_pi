# HELIOS Raspberry Pi Course
These are the instructions to get started with the HELIOS Raspberry Pi
Course. It will take you from a blank Raspberry Pi to running a
Jupyter notebook on the Raspberry Pi which controls different
electrical components.

When reading these instructions, the bullet points mark different
steps, and the grey "code boxes" mark code to be executed. It is often
very handy to triple-click these grey boxes to mark all its content,
and then use ctrl+C and ctrl+V (ctrl+shift+V on Ubuntu) to paste this
in the terminal.

## Install the operating system
* Download the Raspberry Pi imager to your computer:
  https://www.raspberrypi.com/software/
* If you prefer to do it from the terminal, you can do:  
  * `curl -O https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb && sudo apt install imager_latest_amd64.deb # <-- for Ubuntu x86_64`
  * `git clone https://aur.archlinux.org/rpi-imager.git && cd rpi-imager && makepkg -sf && sudo pacman -U rpi-imager-*-x86_64.pkg.* # <-- for ArchLinux`
* Insert the Micro SD card into a card reader
  * Optional: inspecting the ouput from `dmesg` soon after insertion will give
    you a clue as to the location (`/dev/<something>`) of the card in
    the system
* Start the imager either via desktop or terminal via `rpi-imager`
* For "CHOOSE OS" select **Raspberry Pi OS (32-bit)** as operating system
* For "CHOOSE STORAGE" select your Micro SD card as the choosen
  storage (*Make sure to select the correct one. not doing so may have
  irreversible consequences for the incorrectly chosen drive*)
* Click the cog wheel icon for advanced options
* Check the box "Set hostname"
  * Set the host name to `Raspberrypi1` or `Raspberrypi2`, following the number given on your package
* Check the box "Enable SSH"
  * Mage sure that "Use password authentication" is selected
* Check the box "Set username and password"
  * Set username `pi`
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
* No back at the main window, click "Write"
* Click "Yes" when prompted that all existing data will be erased
  * **Be patient** and wait for the writing and verification to finish
  * This takes roughly 15 minutes

## First Boot
* Insert the SD card into the SD card slot on the Raspberry Pi
* Connect the Raspberry Pi to your computer via the ethernet cable
* Connect the Raspberry Pi to power
* Wait 2-3 minutes for the Raspberry Pi to power up, wait until the green LED stops blinking

## Connecting via SSH
### GNU/Linux (UBUNTU)
* Go to Network settings
* Under "Wired" make sure that the toggle switch of "Connected" is turned on
* Click the cog wheel next to the toggle switch
* Go to IPv4 and select "Shared to other computers"
* Click Apply
* Connect to the Raspberry Pi with SSH
  * `ssh pi@[raspberrypi_name].local`
* If you have trouble conneting, try powering cycling the Raspberry Pi ,i.e., _Turn it on and off again_ ;-)

### MAC
* Open a terminal
* Connect to the Raspberry Pi with SSH
  * `ssh pi@[raspberrypi_name].local`

### Windows
* Open the Microsfot store and search for "PuTTY"
* Install PuTTY
* Open the PuTTY App
* Enter your [raspberrypi_name] in the field for "Host Name (or IP address)"
  * For example "Raspberrypi2"
* Click "Open"
  * You might get a "PuTTY Security Alert" saying that "The host key is not cached for this server...", just click "accept"
* A terminal opens and shows "login as:" type `pi`
* The terminal then prompts you for the password that you have set
* Done! You are inside the Raspbperry Pi Terminal
* **IMPORTANT!** To paste commands from your PC into the PuTTY terminal, use the right click or shift+insert

## Setting up Raspberry Pi via SSH
* When connected via SSH Execute the following commands to setup the different interfaces of the Raspberry Pi
  * `sudo raspi-config nonint do_vnc 0`
  * `sudo raspi-config nonint do_i2c 0`
  * `sudo raspi-config nonint do_spi 0`
  * `sudo raspi-config nonint do_rgpio 0`
* Execute these commands to update and install necessary software to the Pi
  * `sudo apt update`
  * `sudo apt full-upgrade`
  * `sudo apt-get install libatlas-base-dev`
  * `pip install -U numpy`
  * `pip install notebook`
  * `pip install jupyterplot`
  * `pip install smbus2`
* Get the wired IP address of the Raspberry Pi
  *  `ifconfig`
  *  Under `eth0` it should show like `inet 10.42.0.248`
  *  When connecting to the Pi later, this can be useful in addition to the name "[raspberrypi_name].local"
* Navigate to the Desktop
  * `cd Desktop`
* Clone the code respository:
  *  `git clone https://github.com/exook/helios_pi.git`
* Execute this command to reboot
  * `sudo reboot`

## Two choices for working with your Rapsberry Pi
### Full graphical desktop environment: Connecting via Real VNC
* **This is only needed if you are not comfortable with the terminal environment**
* Install a VNC client on your computer: https://www.realvnc.com/en/connect/download/viewer/
* Open Real VNC on your computer
  * The address of the raspberry pi is: [raspberrypi_name].local
* In the top left, use the black suqare icon to open a terminal window

### (Recommended) Running the Jupyter notebook without VNC (Indirect but less laggy)
#### Linux/MAC
* If you think the VNC is a bit slow or laggy you can try this method
* Open a new terminal on your **PC** and run the following command to
  create an ssh tunnel to the port where you will host the Jupyter notebook server.
  *  `ssh -L 8080:localhost:8080 pi@[raspberrypi_name].local`
* Navigate to the correct directory
  * `cd Desktop/helios_pi/`
* Start the notebook without a browser, and with a specific port
  * `jupyter notebook --no-browser --port=8080`
* Copy the "localhost" URL and token given at output in the
  terminal. It normally looks something like this:
  * `http://localhost:8080/?token=6d587c101ecd1c75ffa640675a6aaae9179c5118db79f4e4` (your token will be different)
* You should now see a jupyter notebook environment in the browser on
  your **PC**
  * The Jupyter notebook now runs on your Raspberry Pi, but you can
    interact with it in your **PC** browser, which is faster than VNC
* Note that if you do this in the future, pick a port number that is
  not standard and not often listed on the internet as this can make
  the Raspberry Pi vulnerable to attacks
#### Windows
* Open PuTTY and enter the [raspberrypi_name]
* Go to SSH on the bottom of the left pane to expand the menu and then click on Tunnels
* For "Source port", enter the port number which you want to use to access Jupyte. I picked 8080
* Det the destination as "localhost:8080"
* Click the Add button, and the ports should appear in the Forwarded ports list
* Click the Open button to connect to the server via SSH and tunnel to the desired port
* Log in to the Raspberry Pi as usual
* In the terminal run
  * `jupyter notebook --no-browser --port=8080`
* Copy the "localhost" URL and token given at output in the
  terminal. It normally looks something like this:
  * `http://localhost:8080/?token=6d587c101ecd1c75ffa640675a6aaae9179c5118db79f4e4` (your token will be different)
  * Enter it into the browser on your **PC**.
* You should now see a jupyter notebook environment in the browser on
  your **PC**
  * The Jupyter notebook now runs on your Raspberry Pi, but you can
    interact with it in your **PC** browser, which is faster than VNC
* Note that if you do this in the future, pick a port number that is
  not standard and not often listed on the internet as this can make
  the Raspberry Pi vulnerable to attacks

## MISC

#### Optional: Connecting securely to VNC using SSH tunnel (X11VNC and vncviewer [tigervnc])
* **This is only needed if you want to connect to the Jupyter notebook
  from a browser window running directly on the Raspberry Pi. See Bellow**
* Install and setup `X11VNC` on the Raspberry Pi
  * `sudo apt-get install x11vnc`
  * `x11vnc -storepasswd`  <-- set up a password
  * we need to create a configuration file to start x11vnc when the
  Desktop (LXDE) starts
  ```
  cd ~/.config
  mkdir autostart
  cd autostart
  nano x11vnc.desktop
  ```
    * The contents of that file are the following
    ```
    [Desktop Entry]
    Encoding=UTF-8
    Type=Application
    Name=X11VNC
    Comment=
    Exec=x11vnc -forever -usepw -display :0 -ultrafilexfer
    StartupNotify=false
    Terminal=false
    Hidden=false
    ```
* From your local machine, **PC**, we need to setup the SSH tunnel and connect to it
  * `ssh -f -t -L 5900:localhost:5900 [raspberrypi_name].local 'x11vnc -xkb -display :0 -localhost -rfbauth .vnc/passwd`
  * `vncviewer -PreferredEncoding=ZRLE localhost:0`
  * You might want to try different encodings: `copyrect tight zrle hextile zlib corre rre raw`

##### Optional: Graphical Desktop environment using VNC (Direct but potentially laggy)
* This is a conceptually more direct way to run the Jupyter notebook
  but it is not the preferred way as the overhead of running a
  graphical desktop, plus browser, on the raspberry is not small.
* Open a terminal
* Navigate to the Desktop
  * `cd Desktop`
* Clone the code respository:
  *  `git clone https://github.com/exook/helios_pi.git`
*  Enter the new directory
  *  `cd helios_pi/`
* Start the notebook:
  * `jupyter notebook`
* In the browser window, open `helios_pi.ipynb`
* You are ready to go!

## If you need to re-configure WiFi from terminal
  * `sudo raspi-config`
  * Navigate to "System Options", then "Wireless LAN"
    * For "SSID" enter the name of the network, press enter
    * For passphrase, enter the password for the network. Press enter
    * Back at the main menue, use the right arrow key twice to mark
      "Finish", then press enter
      
## If you run into problems with numpy on your Raspberry Pi (for example with the jupyterplot package)
  Part of this information can be found at:
  https://numpy.org/devdocs/user/troubleshooting-importerror.html
  * Open up the terminal on your pi and enter
  * 'sudo pip install -U numpy'
  * 'sudo apt-get install libatlas-base-dev'
  These steps are meant to fix a broken numpy installation on your Raspberry. 
  * Restart the kernel in your jupyter notebook, or restart the application
  *Alternatively:*
  * Open up the terminal on your pi and enter
  * 'sudo pip3 uninstall numpy'  # remove previously installed version
  * 'sudo apt install python3-numpy'
  This way could also work.
    
