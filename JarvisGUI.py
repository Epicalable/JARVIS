#J.A.R.V.I.S Copyright (C) 2020 Epicalable LLC. All Rights Reserved.
#For Gui EXE: pyinstaller -wF my_program.py (Runs Without shell window)
#If pyinstaller crashes add: --hidden-import tkinter
import PySimpleGUI as sg
from tkinter.constants import TRUE
import datetime
import time
import requests
import json
import smtplib
import wikipedia
from random import choice


def Weather(Timeing):
    try:
        with open("Jarinfo.json") as f:
            contents = json.load(f)
            key = contents["OpenWeatherKey"]
            Place = contents["City"]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + Place + "&APPID=" + key
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temp = current_temperature-273.15
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(Timeing + Place.upper() + ":")
            print(" Temperature (Celsius) = " + str(current_temp) +
                  "\n Humidity (Percentage) = " + str(current_humidiy) + "\n Description = " + str(weather_description))
        else:
            print("JARVIS: PLEASE CHANGE YOUR CITY IN THE SETTINGS AS THIS IS INVALID.")
    except:
        print("JARVIS: I AM HAVING A PROBLEM IN GETTING LIVE WEATHER PLEASE CHECK YOUR INTERNET-CONNECTION.")


def Breifing(title, text):
    str = 'general business science health technology entertainment sports'
    with open("Jarinfo.json") as f:
        contents = json.load(f)
        JNews = contents["NewsApiKey"]
        country = contents["Country"]
    headers = {'Authorization': JNews}
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'

    if title == 'Morning Briefing':
        sg.theme('DarkGreen3')
        layout = [[sg.Text(text)],
                  [sg.Output(size=(45, 20), font=('Helvetica 10'))],
                  [sg.Button('GET NEWS'), sg.Button('EXIT')]]
        window = sg.Window('Morning Briefing', layout)
        while True:     # Event Loop
            event, value = window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
                break
            if event == 'GET NEWS':
                try:
                    splits = str.split()
                    for split in splits:
                        print("\n" + split.upper() + ":--")
                        headlines_payload = {
                            'category': split, 'country': country}
                        open_news_page = requests.get(
                            url=top_headlines_url, headers=headers, params=headlines_payload).json()
                        article = open_news_page["articles"]
                        results = []
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("JARVIS: SOMETHING WENT WRONG!!!" +
                          "\nPLEASE CHECK IF YOU HAVE A GOOD INTERNET CONNECTION AND HAVE GIVEN A VALID \nCATEGORY AND LOCATION.")
                    continue
        window.close()
        event = window.read()
        return event != 'OK'

    else:
        sg.theme('DarkGreen3')
        window = sg.Window(title,
                           [[sg.Text(text)],
                            [sg.Output(size=(46, 20), font=('Helvetica 10'))],
                               [sg.Multiline(size=(28, 1), enter_submits=TRUE, key='-NEWS-', do_not_clear=False),
                                sg.Button('GET NEWS', bind_return_key=True),
                                sg.Button('EXIT')]])
        while True:     # Event Loop
            event, value = window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
                break
            if event == 'GET NEWS':
                country = value['-NEWS-'].rstrip()
                try:
                    splits = str.split()
                    for split in splits:
                        print("\n" + split.upper() + ":--")
                        headlines_payload = {
                            'category': split, 'country': country}
                        open_news_page = requests.get(
                            url=top_headlines_url, headers=headers, params=headlines_payload).json()
                        article = open_news_page["articles"]
                        results = []
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("JARVIS: SOMETHING WENT WRONG!!!" +
                          "\nJARVIS: PLEASE CHECK IF YOU HAVE A GOOD \nINTERNET CONNECTION AND HAVE GIVEN A VALID \nCATEGORY AND LOCATION.")
                    continue
        window.close()
        event = window.read()
        return event != 'OK'


def Settings():
    sg.theme('Dark')
    with open("Jarinfo.json") as f:
        contents = json.load(f)
        User = contents["User"]
        NewsApiKey = contents["NewsApiKey"]
        OpenWeatherKey = contents["OpenWeatherKey"]
        Country = contents["Country"]
        City = contents["City"]
    layout = [[sg.Text('Settings', font='Default 16')],
              [sg.T('User-Name:', size=(13, 1)), sg.Input(
                  User, key='-User-', size=(33, 1))],
              [sg.T('NewsApiKey:', size=(13, 1)), sg.Input(
                  NewsApiKey, key='-NewsApi-', size=(33, 1))],
              [sg.T('OpenWeatherMap:', size=(13, 1)), sg.Input(
                  OpenWeatherKey, key='-OpenWeather-', size=(33, 1))],
              [sg.T('Current-Country:', size=(13, 1)), sg.Input(
                  Country, key='-Country-', size=(33, 1))],
              [sg.T('Current-City:', size=(13, 1)), sg.Input(
                  City, key='-City-', size=(33, 1))],
              [sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('Settings', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Save':
            User = values['-User-']
            newsapikey = values['-NewsApi-']
            weatherkey = values['-OpenWeather-']
            Country = values['-Country-']
            City = values['-City-']
            dictionary = {
                "!CAUTION!": "PLEASE REFRAIN from TAMPERING with the BELOW DATA!!!",
                "User": User,
                "NewsApiKey": newsapikey,
                "OpenWeatherKey": weatherkey,
                "Country": Country,
                "City": City
            }
            json_object = json.dumps(dictionary, indent=4)
            with open("Jarinfo.json", "w") as outfile:
                outfile.write(json_object)
            break
    window.close()
    event = window.read()
    return event != 'OK'


def send_an_email(from_address, to_address, subject, message_text, password):
    try:
        jarvis_mail = '\n \n \n \n                                                        ---This message was sent to you by JARVIS  :-)'
        full_message = "{0} {1}".format(message_text, jarvis_mail)
        email_message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (from_address, to_address, subject, full_message)
        # Use port 587 or 465 using SMTP_SSL
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()    # start TLS for security
        s.login(from_address, password)    # Authentication to your account
        s.sendmail(from_address, to_address,
                   email_message)    # sending the email
        s.quit()    # terminating the session
    except:
        sg.popup('PLEASE CHECK YOUR INTERNET-CONNECTION.')

def gmail():
    sg.theme('Dark')
    layout = [[sg.Text('Send an Email', font='Default 15')],
              [sg.T('From:', size=(8, 1)), sg.Input(
                  key='-EMAIL FROM-', size=(35, 1))],
              [sg.T('To:', size=(8, 1)), sg.Input(
                  key='-EMAIL TO-', size=(35, 1))],
              [sg.T('Subject:', size=(8, 1)), sg.Input(
                  key='-EMAIL SUBJECT-', size=(35, 1))],
              [sg.T('Mail login information', font='Default 14')],
              [sg.T('Password:', size=(8, 1)), sg.Input(
                  password_char='*', key='-PASSWORD-', size=(35, 1))],
              [sg.Multiline('Type your message here',
                            size=(44, 10), key='-EMAIL TEXT-')],
              [sg.Button('Send')]]
    window = sg.Window('Send An Email', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Discard'):
            break
        if event == 'Send':
            send_an_email(from_address=values['-EMAIL FROM-'],
                          to_address=values['-EMAIL TO-'],
                          subject=values['-EMAIL SUBJECT-'],
                          message_text=values['-EMAIL TEXT-'],
                          password=values['-PASSWORD-'])
            continue
        window.close()
        event = window.read()
        return event != 'OK'


def Help():
    sg.theme('Dark')
    layout = [[sg.Text('Help', font='Default 14')],
              [sg.Output(size=(60, 20), font=('Helvetica 10'))],
              [sg.Button('GET HELP'), sg.Button('EXIT')]]
    window = sg.Window('Help', layout)

    while True:     # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
            break
        if event == 'GET HELP':
            with open ("Help.txt","r") as H:
                print(H.read())
            continue
    window.close()
    event = window.read()
    return event != 'OK'











sg.theme('DarkGrey8')  # gives window a spiffy set of colors
sg.set_options(element_padding=(3,3))
menu_def = [['&MENU ', ['&Settings', 'E&xit']],
            ['&HELP', ['&Help','&Support us', '&About...']], ]
layout = [[sg.Menu(menu_def, tearoff=False)],
          [sg.Text('J.A.R.V.I.S  A.I', size=(98, 1)),
           sg.Text(('(C) Epicalable'), size=(20, 1))],
          [sg.Output(size=(139, 38), font=('Helvetica 10'))],
          [sg.Multiline(size=(96, 2), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('ENTER',size=(11,2), bind_return_key=True)]]
window = sg.Window('J.A.R.V.I.S GUI', layout, location=(0,0) ,icon=r'icon/Jarvis.ico', font=(
    'Helvetica', ' 13'), default_button_element_size=(8, 2)).Finalize()
window.maximize()

print("JARVIS: WELCOME SIR")
hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    Timeing = "JARVIS: GOOD MORNING, HERE IS THE CURRENT WEATHER IN "
    Weather(Timeing)
    Breifing('Morning Briefing', 'Morning News Headlines')
elif hour >= 12 and hour < 18:
    Timeing = "JARVIS: GOOD AFTERNOON, HERE IS THE CURRENT WEATHER IN "
    Weather(Timeing)
else:
    Timeing = "JARVIS: GOOD EVENING, HERE IS THE CURRENT WEATHER IN "
    Weather(Timeing)


if __name__ == '__main__':
    while True:     # The Infinity Event Loop
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # quit if exit button or X

            print(
                "\nJARVIS: GOODBYE SIR HOPE YOU HAVE A NICE DAY :-)")
            print(
                "\nJ.A.R.V.I.S Copyright (C) 2020 Epicalable LLC. All Rights Reserved.")
            time.sleep(4)
            break

        if event == 'ENTER':

            # THE START OF THE RENDER-WORD ENGINE (C) Epicalable
            que = value['-QUERY-'].rstrip()
            query = (que.upper()) # YOUR INPUT HERE
            with open("Jarinfo.json") as f:
                contents = json.load(f)
                User = contents["User"]
                print("\n" + User + ": {}".format(query))
                with open("Jarintents.json") as f:
                    data = json.load(f)
                    for word in data['intents']:
                        if word['tags'] in query:
                            print(choice(word["response"]))
                            break
                    # THE END OF THE RENDER-WORD ENGINE (C) Epicalable

                    else:
                        if "DATE" in query or "TIME" in query:
                            x = datetime.datetime.now()
                            print("JARVIS: THE DATE AND TIME IS ",
                                  x,"RESPECTIVELY SIR")
                            continue

                        elif "WIKIPEDIA" in query or "WIKI" in query:
                            query = query.replace('WIKIPEDIA', "")
                            try:
                                print(wikipedia.summary(query))
                            except:
                                print(
                                    "JARVIS: I AM HAVING A PROBLEM IN GETTING WIKIPEDIA PLEASE CHECK YOUR INTERNET-CONNECTION.")
                            continue

                        elif "WHAT IS" in query or "WHO IS" in query:
                            query = query.replace('WHAT', "")
                            query = query.replace('IS', "")

                            query = query.replace('WHO', "")
                            query = query.replace('IS', "")
                            try:
                                print(wikipedia.summary(query))
                            except:
                                print(
                                    "JARVIS: I AM HAVING A PROBLEM IN GETTING WIKIPEDIA PLEASE CHECK YOUR INTERNET-CONNECTION")
                            continue

                        elif "NEWS ABOUT" in query or "NEWS ON" in query:
                            query = query.replace('NEWS ', "")
                            query = query.replace('ABOUT ', "")
                            query = query.replace('ON ', "")
                            try:
                                with open("Jarinfo.json") as f:
                                    contents = json.load(f)
                                    JNews = contents["NewsApiKey"]
                                headers = {'Authorization': JNews}
                                everything_news_url = 'https://newsapi.org/v2/everything'
                                everything_payload = {
                                    'q': query, 'language': 'en', 'sortBy': 'publishedAt'}
                                open_news_page = requests.get(
                                    url=everything_news_url, headers=headers, params=everything_payload).json()
                                article = open_news_page["articles"]
                                results = []
                                for ar in article:
                                    results.append(ar["title"])
                                for i in range(len(results)):
                                    print(i + 1,'.', results[i])
                            except:
                                print( "JARVIS: SOMETHING WENT WRONG PLEASE CHECK IF YOU HAVE A GOOD INTERNET CONNECTION.")
                                continue

                        elif "HEADLINES" in query:
                            Breifing('News Headlines', 'Current Headlines(Enter country abbreviation in given field)')
                        
                        elif "SEND AN EMAIL" in query or "SEND A EMAIL" in query:
                            gmail()

                        elif query == "GOODBYE":
                            print(
                                "JARVIS: GOODBYE SIR HOPE YOU HAVE A NICE DAY :-)")
                            print(
                                "\nJ.A.R.V.I.S Copyright (C) 2020 Epicalable LLC. All Rights Reserved.")
                            time.sleep(4)
                            break

                        else:
                            print("JARVIS: I DID NOT UNDERSTAND YOU, AS YOU CAN SEE I AM STILL EVOLVING :-)")


        elif event == 'Settings':
            Settings()

        elif event == 'Help':
            Help()

        elif event == 'Support us':
            sg.popup_no_frame("Subscribe and share our 'Epicalable' Youtube channel",
                              "so you can watch us play games :-)")

        elif event == 'About...':
            sg.popup_no_frame('---About J.A.R.V.I.S---',
                              'Version: 0.8',
                              'JUi: Version 0.3',
                              'RenderWord: Version 0.2',
                              'Copyright (C) 2020 Epicalable LLC')

window.close()

