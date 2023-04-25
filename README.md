# J.A.R.V.I.S

Kindly consider starring this repository if you like the program :-)

[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](https://github.com/Epicalable/JARVIS-GUI)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Epicalable/JARVIS-GUI) [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/Epicalable/JARVIS-GUI) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Epicalable/JARVIS-GUI/issues)

![jaruiv1.0](https://user-images.githubusercontent.com/69076784/180637424-8d2737c9-ead7-4d65-a8e8-a2c36d9474e8.png)


## Table Of Contents
- [WHAT'S NEW?](#whats-new)
- [Screenshots of J.A.R.V.I.S](#screenshots-of-jarvis)
- [Introduction to J.A.R.V.I.S](#introduction-to-jarvis)
- [How to run J.A.R.V.I.S](#how-to-run-jarvis)
- [How does J.A.R.V.I.S store info](#how-does-jarvis-store-info-and-is-it-safe)
- [What Are The APIs should I subscribe to?](#what-are-the-apis-should-i-subscribe-to)
- [Examples of J.A.R.V.I.S commands](#some-examples-of-jarvis-commands)
- [License](#license)


## WHAT'S NEW?
Here at Epicalable we are committed in keeping J.A.R.V.I.S up-to-date and up-to-speed with the growing tech solutions and algorithms. Hence this new commit includes:
```
Update Highlights:-
1. Before, each functions had their own Audit uploading code but now, We have a new centralised Audit function to remove redundant code.  
   1a. Using the centralised function we can control audit-writing more effectively and will be integrated into the developer tools soon.
2. Keep a look out for the new upcoming developer tools in the coming days!!!
   We are currently slowly adding Developer tools in the code which are currently unaccessable to users.

Weekly Maintanance Updates:-
1. Updated README.md
2. Weekly Code checks, updates and Maintanence to continue supporting python 3.11.3.

Code Checks Manifest:-
All Checks Status: ✅
-----------------------------------------
Code Integrity Checks: ✅
GUI Stability Checks: ✅
Code-GUI Integration Checks: ✅
(All evaluations are done by the R&D Department)

Last Updated: 25-April-2023 20:50 HRS
Publisher: Epicalable
```
Keep updated to what's happening on this repository by clicking the 'Star' and 'Watch' button on the top right corner of this webpage.



## Screenshots of J.A.R.V.I.S
##### Graphical User Interface :-

<img src="https://user-images.githubusercontent.com/69076784/180637424-8d2737c9-ead7-4d65-a8e8-a2c36d9474e8.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/232394556-eff71901-0926-42e3-9161-7469759c3c7c.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/206891927-da7d86b8-e3df-4922-a887-7be46cc94070.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/210161820-44109b56-a2bf-4410-a90d-a3ded829dfb2.png" width="100" height="60">

##### Code Workspace (VSCode + One Dark Pro + Pylance) :-
<img src="https://user-images.githubusercontent.com/69076784/233782216-154d7e53-fa02-4770-ab9a-dec5f923cbee.png" width="100" height="60"> <img src="https://user-images.githubusercontent.com/69076784/233782218-b09d765c-e7db-4e31-a213-a00b60953b0e.png" width="100" height="60">  
Take a look at the workspace difference between windows 10 and windows 11.  

###### Note: SOON!!! By 1 May all of Epicalable Systems will have been upgraded to windows 11.


## Introduction to J.A.R.V.I.S?
J.A.R.V.I.S was started in 2019 as an Command-Line Interface Application in C++ and after careful consideration was shifted to Python during 2020 due to some limitations.  
J.A.R.V.I.S has been constantly evolved over the years to where it is now, integrated with a GUI and new features being added every month. While our staffs in Epicalable are constantly fixing bugs and closing issues behind the scenes.  
So what does JARVIS do? Well JARVIS is known as a chatbot it also can get news, weather, get location, send emails, flight info, stock prices, wikipedia and some more cool features sprinkled in by our programmers.



## How to run J.A.R.V.I.S?
To run J.A.R.V.I.S, user are to open up the JarvisGUI.py file and 'pip' download the 3rd party packages so users can run Jarvis successfully without any problems.  
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

2. Info-Intents: Stored in Jarsettings file used by J.A.R.V.I.S to access Api keys, User Name and location for data retrieval and also to adjust the output and input screen sizes. You can access these by heading to settings in the menu.  

3. Audit-Indents: Stored in the Jaraudit file used by J.A.R.V.I.S to store user input/output logs, system retrival logs and fallback errors in your computer. You can access them by heading to ChatLogs in the menu.

All CRITICAL INFO REGARDING the USER will be STORED IN your PERSONAL COMPUTER and NOT on the INTERNET.



## What Are The APIs should I subscribe to?
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



## License  
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Epicalable/)  

IMPORTANT NOTE: Any User who are willing to Share or Re-Distribute JARVIS are kindly advised to:

1. A reference to us by keeping a "(C) Epicalable" text in the 'Modified program' such as keeping it in the settings menu, about or help page.

2. a link to this repository from the user's 'Modified program' README file. 

It will be helpful for us as users will know it's original source and about our startup.
Please also refer to LICENSE file for clarifications.  
Thank you for your kind cooperation :-)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Epicalable/)
[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/MahaMohan/)

[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/) 
[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/Epicalable/)

Version 1.3  
J.A.R.V.I.S Copyright (C) Epicalable 2023  
All Rights Reserved.