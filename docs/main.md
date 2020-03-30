# Thing 1 and Thing 2 Documentation

## Types of Connections

There are 3 ways Thing1 and Thing2 can communicate:  Direct, Local, and Remote.

* **Direct:** One device creates a wifi network and the other device connects to it and communicates directly.
  * Documentation: [direct.md](direct.md)
* **Local:**  Both devices connect to the same local wifi network and communicate directly.
  * Documentation: [local.md](local.md)
* **Remote:** Both devices connect to any wifi network and communicate through a remote server.
  * Documentation: [remote.md](remote.md)


## Identity
For this code to work thing1 and thing2 need to know who they are and which role they are playing.  To do this their individual mac addresses are set in settings.py which checks the mac and sets I_AM_THING1 and I_AM_THING2 accordingly.

## Important Scripts

#### firmware/flash.sh

Erase the feather and upload a new CircutePython system.  All program files are lost and you need to install everything again.

#### install.sh

Installs the system files from */src* onto the feather.
* -f: Flash the firmware before loading files
* -m <mode>: Install the given mode (direct, local, remote) as main.py
* -z <port>:  Use the given port to upload files.

Example:
```
./install.sh -f -m remote
```

## Core System files

#### settings.py

This file is loaded first and all variables in it are available to all programs

* Hardware variables (leds, buttons, vibe)
* I_AM_THING1 and I_AM_THING2 respectfully
* Wifi settings

#### main.py

This is the body of the main program that is executed when the system starts.

#### core.py

Library classes such as LED and Vibe to abstract core functionality.

#### utils.py

Universal utility functions.
