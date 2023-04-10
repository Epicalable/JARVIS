# J.A.R.V.I.S

Kindly consider starring this repository if you like the program :-)

[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](https://github.com/Epicalable/JARVIS-GUI)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Epicalable/JARVIS-GUI) [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/Epicalable/JARVIS-GUI) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Epicalable/JARVIS-GUI/issues)

![jaruiv1.0](https://user-images.githubusercontent.com/69076784/180637424-8d2737c9-ead7-4d65-a8e8-a2c36d9474e8.png)


## Table Of Contents
- [WHAT'S NEW?](#whats-new)
- [Introduction to J.A.R.V.I.S](#introduction-to-jarvis)
- [How to run J.A.R.V.I.S](#how-to-run-jarvis)
- [How does J.A.R.V.I.S store info](#how-does-jarvis-store-info-and-is-it-safe)
- [What kind of API should I subscribe to?](#what-kind-of-api-should-i-subscribe-to)
- [Examples of J.A.R.V.I.S commands](#some-examples-of-jarvis-commands)
- [Screenshots of J.A.R.V.I.S](#screenshots-of-jarvis)
- [License](#license-open-source-love-svg1)


## WHAT'S NEW?
Starting our Monday with a new update!!! In order to keep J.A.R.V.I.S up-to-date and keep it up with the growing tech industries and solutions this new commit includes,
```
1. We have moved the ability to edit output and input screen sizes to the new Jarsettings.json file from Jarinfo.json for easier segregation of tasks.  
   1a. To access Jarsettings.json head to 'Menu' and click on 'Layout' and start adjusting to your screen size.
2. We have added a Table-Of-Contents to our README.md for users to navigate out repository easier.
   2a. README.md now has a new section to check what's new.
3. Minor Bugs and Issues Fixes.  

Last Updated: 10-April-2023
Publisher:  Epicalable
```
Keep updated on what's happening to this repository by clicking the 'Star' and 'Watch' button on the top right corner of this webpage.



## Introduction to J.A.R.V.I.S?
J.A.R.V.I.S is a chatbot integrated into a GUI built and coded in Python by Epicalable whose aim is to be capable of chatting and retrieving any information or on-going events from the internet for it's users upon requested. Jarvis is also made to help test our organisation's potential and problem-solving techniques.



## How to run J.A.R.V.I.S?
To run J.A.R.V.I.S the user is required to open up the JarvisGUI.py file and run it so as to successfully open the GUI and start chatting with J.A.R.V.I.S.
Users facing any issues can open up an issue at the Issues section of JARVIS Github Page and can expext us to rectify it ASAP.  

In order for J.A.R.V.I.S to work at full capacity a few 3rd party python packages will be required to be installed:
1. pip install PySimpleGUI
2. pip install requests
3. pip install beautifulsoup4
4. pip install wikipedia
5. pip install geocoder



## How does J.A.R.V.I.S store info and is it safe?
Yes, Your info will be safe since it will be stored locally on your personal computer. J.A.R.V.I.S stores these info into 3 main sources.

1. Response-Intents: Stored in Jarintents file used by J.A.R.V.I.S to check your input with tags and provide the appropriate output for the user. Head to Jarindent.json to take a look.

2. Info-Intents: Stored in the Jarinfo file used by J.A.R.V.I.S to store Api keys, User Name and User location for data retrieval. You can access these using the settings menu.  
You can access the Layout menu to help adjust the output and input screen sizes.

3. Audit-Indents: Stored in the Jaraudit file used by J.A.R.V.I.S to store user input/output logs, system retrival logs and fallback errors in your computer. You can access them by heading to ChatLogs on the menu.

All CRITICAL INFO REGARDING the USER will be STORED IN your PERSONAL COMPUTER and NOT on the INTERNET.



## What kind of API should I subscribe to?
When completed installing, by default you can chat with J.A.R.V.I.S using temporary APIs provided to you. But if you want it to be personalised then it is best to activate the API. To do that you will need to head to:

1. https://newsapi.org/ : For Live News, Morning Briefings and News Headlines.

2. https://openweathermap.org/ : For current Weather information.

Both websites once registered will provide you an API key, Users should then copy the API key and paste it in the respective bars in the settings menu.



## Some examples of J.A.R.V.I.S commands.
To make JARVIS respond Users will need to enter a Command in the input bar and then JARVIS will scan for keywords and provide an answer or information.

Here is a sample list of available Commands:
* Hello
* How are you
* Are you fine
* Are you real
* Tell me the time
* News on [your input]--  
    Ex. News on Github.
* Get me news headlines
* Send an email
* Wikipedia [Query]--  
    Ex. Wikipedia github.
* Who is [Query] / What is [Query]--  
    NOTE: JARVIS will get answer from Wikipedia.
* Get me stock price--  
    NOTE: Stock abbreviations EX."TSLA AAPL MSFT" will be in Setting under "StockPrice".
* Track flight <Flight Number>  
    NOTE: Number of Flight like SQ 11, SQ 305, SQ 335, SQ 23   
    Ex. Track flight SQ 242
* Goodbye --  
    NOTE: Command to quit JARVIS.



## Screenshots of J.A.R.V.I.S
<img src="https://user-images.githubusercontent.com/69076784/180637424-8d2737c9-ead7-4d65-a8e8-a2c36d9474e8.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/206891927-da7d86b8-e3df-4922-a887-7be46cc94070.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/210161820-44109b56-a2bf-4410-a90d-a3ded829dfb2.png" width="100" height="60">



## License [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Epicalable/)
IMPORTANT NOTE: Any User who are willing to Share or Re-Distribute the above 'Program' are kindly advised to:

1. keep at least ONE "(C) Epicalable" text in the 'program'.

2. a link to this repository from the user's 'Modified program' README file. 

It will be helpful for us as users will know it's original source and about our startup.
Please also refer to LICENSE file for clarifications. 
THANK YOU FOR YOUR COOPERATION :-)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Epicalable/)
[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/MahaMohan/)

[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/) 
[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/Epicalable/)

J.A.R.V.I.S Copyright (C) 2023 Epicalable LLC. All Rights Reserved.