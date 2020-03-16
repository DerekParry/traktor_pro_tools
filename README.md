## Tools for Native Instruments "Traktor Pro" DJ software
*(Confirmed to work with Traktor Pro ver 3.2.1 on macOS Catalina)*

This project was designed to contain tools for working with the "Traktor Pro" DJ software. There is currently one script, but I plan to add more scripts and functionality as needed.

### Setup

This project contains a Makefile with two rules:
- *make* (or *make create*) => creates a virtual environment directory (~/ve/) and installs all required packages via pip
- *make clean* => deletes the virtual environment directory from the above command

This project also contains a config file (~/config.ini). Before running, the user must enter the correct paths for Traktor's "collection.nml" file and "History" directory. If these are at the application's default locations, then the user will only have to change the value of "*myuser*" to the correct macOS username. 

### tracklist.py

tracklist.py can print Traktor Pro playlists or print archive playlists directly to standard ouput. The base application can only display these playlists while running, and does not have copy/paste functionality.
After setup, this file can be executed directly with the following arguments:
- *--playlist* => Allows user to specify a playlist by name (within Traktor Pro, these are found under the "Playlists" dropdown 
- *--archive* => Allows user to specify an archive playlist by name (within Traktor Pro, these are found under the "Explorer" then "Archive" dropdown
