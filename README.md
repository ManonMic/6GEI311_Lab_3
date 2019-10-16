# 6GEI311 Lab 3
By Manon Michelet & Jean-Michel Plourde.

Implementation of 6GEI311 Lab 3 in Python36

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* A Windows environment
* The Microsoft DirectShow library installed
* Visual Studio
* Python36 installed
* tkinter library

### Installing
- Clone this repo with HTTP or SSH
```
git clone https://github.com/ManonMic/6GEI311_Lab_2.git
```
* Open the project folder in visual studio 
* Set the plateform binary to _x64_ and the configuration to _Release_
* Right-click on the project name in the solution explorer, in _properties_ > _Linker_ > _Input_ > _Additionnal dependencies_ 
    * add _Strmiids.lib_ to the line
* Right-click on the project name in the solution explorer, in _properties_ > General
  * add _videoplayer_ in _Target Name_ line
  * add _.pyd_ in _Target extension_ line
  * add _videoplayer_ in _Configuration Type_ line
* Right-click on the project name in the solution explorer, in _properties_ > VC++ Directories
  * add path to Python36/include in _Include directories_ line
  ```
  C:\Program Files\Python36\include
  ```
  * add path to Python36/include in _Library directories_ line
    ```
    C:\Program Files\Python36\libs
    ```
* Build the solution by pressing _Ctrl + Shift + B_

## Using the video player

* Open Powershell or Command Line
* Move to *..\MyProjectFolders\6GEI311_Lab_3*
* Run the python script
```
python player.py
```
* Press the buttons to trigger an action
```
Select File: Browse your computer to select a .avi file to play. 
Play : Play or pause accordingly to the actual state of the video. It will pause if it's playing, and vice versa
Fast Forward : Fast forward (x2). Press again to go back to the normal rate.
Rewind : Rewinds the video to the beginning with respect to the current playing state. If the video was playing, the video rewinds and automatically plays. If paused, the video will not play until you press P again.

Close the window to quit the program and the video

```


## Support
Note that file browsing is limited to the main drive (C:/)
