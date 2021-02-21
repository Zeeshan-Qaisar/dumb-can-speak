# Dumb Can Speak
## Developers
 * [Zeeshan Qaisar](https://github.com/Zeeshan-Qaisar)
 * [Sabir Khan](https://github.com/Sabirkhan233)

# Introduction
Hello we are working on a project to convert hand gestures to speech. It is mainly focused to help mute people to communicate with people who does'nt know sign languuage. This was a team project which we are going to complete as our Final Year project with Fahad Razzaq.

## Project Goals
  The software will capture the hand gesture and convert it into words.
   The software will read the converted words into voice.
## Project Objectives
   * Non-verbal to verbal communication
   * Reduce the efforts
   * Better communication between normal and abnormal people

# Scope
```text
The software will detect hand gestures.
The software only can detect one hand at a time.
The software only detects human hand gestures.
The software will convert words into voice.


The software will not work for blurred hand capture.
The software will not work on multiple hands.
The software will not work for a far hand from the camera.
```


# Usage
## Run Project

You can clone the repository by using the command
```bash
git clone repository url
```
After that you can open it in Pycharm and able to run. You must have all dependency installed

## Installing dependencies

It require to install [PYQT5](https://pypi.org/project/PyQt5/) which is using for GUI.

You need to run this command on your system terminal:
```bash
pip install PyQt5
```
It also require to install [PYMYSQL](https://pypi.org/project/PyMySQL/) for purpose of connecting to database.
Run this command in your terminal
```bash
$ python3 -m pip install PyMySQL
```


## Constraints


* Requires a background with no near skin colours.
* One hand only. The other hand should not be visible
* Sufficient amount of light is needed. Not too much not too less. 
* And preferably avoid using in sunlight, as its yellow light will make everything look skin colour alike.

## Samples

![Demo](https://github.com/Zeeshan-Qaisar/dumb-can-speak/blob/main/demo.gif)

## Project status

We are currently working on the project. the project is in progress.
### What we have done:
* The Complete GUI of the project.
* Login and registeration done.
* See profile and update profile

### What left:
* Detecting hand gestures
* Converting hand gesture to alphabats
* Making paragraph and converting into speech
* Storing the user history