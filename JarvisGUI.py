#J.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.
#For Gui EXE: pyinstaller -wF my_program.py (Runs Without shell window)
#If pyinstaller crashes add: --hidden-import tkinter
import PySimpleGUI as sg
from tkinter.constants import TRUE
import datetime
import time
import requests
import json
import smtplib
import bs4
import wikipedia
import webbrowser
from random import choice


def Weather(timeing):
    try:
        with open("Jarinfo.json") as f:
            contents = json.load(f)
            key = contents["OpenWeatherKey"]
            Place = contents["City"]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + Place + "&APPID=" + key + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temp = current_temperature
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(timeing + Place + ":")
            print(" Temperature (Celsius) = " + str(current_temp) +
                  "\n Humidity (Percentage) = " + str(current_humidiy) + "\n Description = " + str(weather_description))
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER GETS WEATHER REPORT!!!) \n")
            Audfile.close()
        else:
            print("JARVIS: Please check your city in the settings as this is invalid.")
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER'S CITY IS INVALID!!!) \n")
            Audfile.close()
    except:
        print("JARVIS: I am having a problem in getting live weather please check your internet-connection.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(CONNECTION FAILED WITH OPENWEATHERMAP.ORG!!!) \n")
        Audfile.close()


def stocks(tickers):
    # Apple, Microsoft and the S&P500 index.
    # tickers = ['AAPL', 'MSFT', '^GSPC']
    try:
        tickers = tickers.upper()
        link = 'https://finance.yahoo.com/quote/'+tickers+'?p='+tickers
        url = requests.get(link)
        soup = bs4.BeautifulSoup(url.text, features="html.parser")
        price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
            0].find('span').text
        print("Current pricing of Stock for "+tickers+" is: "+price)
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(USER GETS STOCK PRICES FOR "+ tickers +"!!!) \n")
        Audfile.close()
    except:
        print("JARVIS: I am having a problem in getting Stock Prices please check your internet-connection")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(CONNECTION FAILED TO GET STOCK PRICES!!!) \n")
        Audfile.close()


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
        window = sg.Window(title, layout, no_titlebar=True, keep_on_top=True)
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
                        Audfile = open("Jaraudit.txt", "a")
                        querytime = (datetime.datetime.now().ctime())
                        Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                        Audfile.close()
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("JARVIS: Something went wrong!!!" +
                          "\nPlease check if you have a good internet connection and have given a valid \ncategory and location.")
                    Audfile = open("Jaraudit.txt", "a")
                    querytime = (datetime.datetime.now().ctime())
                    Audfile.writelines(
                        querytime + "-(CONNECTION FAILED WITH NEWSAPI.ORG!!!) \n")
                    Audfile.close()
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
                                sg.Button('EXIT')]], no_titlebar=True, keep_on_top=True)
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
                        Audfile = open("Jaraudit.txt", "a")
                        querytime = (datetime.datetime.now().ctime())
                        Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                        Audfile.close()
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("JARVIS: Something went wrong!!!" +
                          "\nJARVIS: Please check if you have a good \ninternet connection and have given a valid \ncategory and location.")
                    Audfile = open("Jaraudit.txt", "a")
                    querytime = (datetime.datetime.now().ctime())
                    Audfile.writelines(
                        querytime + "-(CONNECTION FAILED WITH NEWSAPI.ORG!!!) \n")
                    Audfile.close()
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
        Outputsc = contents["Outputscreensize"]
        Inputbr = contents["Inputbarsize"]
    layout = [[sg.Text('Settings', font='Default 16')],
              [sg.Text('Your-Details:--', font='Default 12')],
              [sg.Text('Enter your information and Api-Keys.', font='Default 10')],
              [sg.T('User-Name:', size=(13, 1)), sg.Input(
                  User, key='-User-', size=(34, 1))],
              [sg.T('NewsApiKey:', size=(13, 1)), sg.Input(
                  NewsApiKey, key='-NewsApi-', size=(34, 1))],
              [sg.T('OpenWeatherMap:', size=(14, 1)), sg.Input(
                  OpenWeatherKey, key='-OpenWeather-', size=(33, 1))],
              [sg.T('Current-Country:', size=(13, 1)), sg.Input(
                  Country, key='-Country-', size=(34, 1))],
              [sg.T('Current-City:', size=(13, 1)), sg.Input(
                  City, key='-City-', size=(34, 1))],
              [sg.Text('GUI-Customization:--', font='Default 12')],
              [sg.Text('Enter only in Numbers to adjust the UI screen size.', font='Default 10')],
              [sg.T('Output-Screen:', size=(13, 1)), sg.Input(
                  Outputsc, key='-Outsc-', size=(34, 1))],
              [sg.T('Input-bar:', size=(13, 1)), sg.Input(
                  Inputbr, key='-Inbr-', size=(34, 1))],
              [sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('Settings', layout, no_titlebar=True, keep_on_top=True)

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
            Outputsc = values['-Outsc-']
            Inputbr = values['-Inbr-']
            dictionary = {
                "!CAUTION!": "PLEASE REFRAIN from TAMPERING with the BELOW DATA!!!",
                "User": User,
                "NewsApiKey": newsapikey,
                "OpenWeatherKey": weatherkey,
                "Country": Country,
                "City": City,
                "Outputscreensize": Outputsc,
                "Inputbarsize": Inputbr
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
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(USER SUCCESSFULLY SENT AN EMAIL!!!) \n")
        Audfile.close()
        s.quit()    # terminating the session
    except:
        sg.popup("Please check your internet connection and have turned 'on' Less secure app access in 'security' section in your Google Account Settings.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(
            querytime + "-(USER FAILED TO SEND AN EMAIL!!!) \n")
        Audfile.close()

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
    layout = [[sg.Text('Help Center', font='Default 14')],
              [sg.Output(size=(60, 20), font=('Helvetica 10'))],
              [sg.Button('GET HELP'), sg.Button('EXIT')]]
    window = sg.Window('Help Center', layout, no_titlebar=True, keep_on_top=True)

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


with open("Jarinfo.json") as f:
    contents = json.load(f)
    LoadOutput = contents["Outputscreensize"]
    LoadInput = contents["Inputbarsize"]
sg.theme('DarkGrey8')  # gives window a spiffy set of colors
sg.set_options(element_padding=(3,3))
menu_def = [['&MENU ', ['&Settings', 'E&xit']],
            ['&HELP', ['&Help', '&Report Issue', '&Version']], 
            ['&ABOUT US', ['&Support Us', '&Our Website']], ]
layout = [[sg.Menu(menu_def, tearoff=False)],
          [sg.Text('J.A.R.V.I.S  A.I', size=(135, 1)),
           sg.Text(('(C) Epicalable'), size=(20, 1))],
          [sg.Output(size=(LoadOutput, 38), font=('Helvetica 10'))],
          [sg.Multiline(size=(LoadInput, 2), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('ENTER',size=(11,2), bind_return_key=True)]]
window = sg.Window('J.A.R.V.I.S GUI', layout, location=(0,0) ,icon=r'icon/JarvisBot.ico', font=(
    'Helvetica', ' 13'), default_button_element_size=(8, 2)).Finalize()
window.maximize()

print("JARVIS: Welcome sir")
Audfile = open("Jaraudit.txt", "a")
querytime = (datetime.datetime.now().ctime())
Audfile.writelines(querytime + "-(USER ACTIVATED JARVIS AND INITIALIZED RELATED PROCESSES!!!) \n")
Audfile.close()

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    timeing = "JARVIS: Good morning, here is the current weather in "
    Weather(timeing)
    Breifing('Morning Briefing', 'Morning News Headlines')
elif hour >= 12 and hour < 18:
    timeing = "JARVIS: Good afternoon, here is the current weather in "
    Weather(timeing)
else:
    timeing = "JARVIS: Good evening, here is the current weather in "
    Weather(timeing)

if __name__ == '__main__':
    while True:     # The Infinity Event Loop
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # quit if exit button or X
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER TERMINATED JARVIS AND ALL IT'S RELATED PROCESSES!!!) \n")
            Audfile.close()
            print("\nJARVIS: Goodbye sir hope you have a nice day :-)")
            print("\nJ.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.")
            time.sleep(4)
            break

        if event == 'ENTER':
            # THE START OF THE RENDER-WORD ENGINE (C) Epicalable
            que = value['-QUERY-'].rstrip()  # Your input here
            query = (que.upper())
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            str = (querytime + ": " + que.capitalize() + "\n")
            Audfile.write(str)
            with open("Jarinfo.json") as f:
                contents = json.load(f)
                User = contents["User"]
                print("\n" + User + ": {}".format(que.capitalize()))
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
                            print("JARVIS: The Date and Time is ",x," respectively sir.")
                            continue

                        if "DAY" in query or "YEAR" in query:
                            x = datetime.datetime.now()
                            print("JARVIS: The Date and Time is ",x," respectively sir.")
                            continue

                        elif "WIKIPEDIA" in query or "WIKI" in query:
                            query = query.replace('WIKI', "")
                            query = query.replace('WIKIPEDIA', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "JARVIS: I am having a problem in getting wikipedia please check your internet-connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION FAILED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "WHAT IS" in query or "WHO IS" in query:
                            query = query.replace('WHAT', "")
                            query = query.replace('IS', "")

                            query = query.replace('WHO', "")
                            query = query.replace('IS', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "JARVIS: I am having a problem in getting wikipedia please check your internet-connection")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION FAILED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
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
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                for ar in article:
                                    results.append(ar["title"])
                                for i in range(len(results)):
                                    print(i + 1,'.', results[i])
                            except:
                                print(
                                    "JARVIS: Something went wrong please check if you have a good internet connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION FAILED WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                continue

                        elif "HEADLINES" in query:
                            Breifing('News Headlines', 'Current Headlines(Enter country abbreviation in given field)')

                        elif "THE NEWS" in query:
                            Breifing('News Headlines', 'Current Headlines(Enter country abbreviation in given field)')
                        
                        elif "STOCKS" in query or "STOCK PRICE" in query:
                            query = query.replace('GET ME ', "")
                            query = query.replace('PRICE ', "")
                            query = query.replace('PRICES ', "")
                            query = query.replace('STOCK ', "")
                            query = query.replace('STOCKS ', "")
                            query = query.replace('FOR ', "")
                            query = query.replace('ON ', "")
                            stocks(tickers=query.upper())

                        elif "SEND AN EMAIL" in query or "SEND A EMAIL" in query:
                            gmail()

                        elif query == "GOODBYE":
                            Audfile = open("Jaraudit.txt", "a")
                            querytime = (datetime.datetime.now().ctime())
                            Audfile.writelines(querytime + "-(USER TERMINATED JARVIS AND ALL IT'S RELATED PROCESSES!!!) \n")
                            Audfile.close()
                            print("JARVIS: Goodbye sir hope you have a nice day :-)")
                            print("\nJ.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.")
                            time.sleep(4)
                            break

                        else:
                            print(
                                "JARVIS: I did not understand you, as you can see i am still evolving :-)")
                            Audfile = open("Jaraudit.txt", "a")  
                            Audfile.write("ERROR 404 (FALLBACK)!!! \n")
                            Audfile.close()


        elif event == 'Settings':
            Settings()

        

        elif event == 'Support Us':
            sg.popup_no_titlebar("Please star our 'JARVIS-GUI' github repository and also",
                              "Subscribe and share our 'Epicalable' Youtube channel")
            webbrowser.open("https://github.com/Epicalable/JARVIS", new=1)

        elif event == 'Our Website':
            webbrowser.open("https://epicalable.github.io/epicalable.html", new=1)

        elif event == 'Help':
            Help()

        elif event == 'Report Issue':
            webbrowser.open("https://github.com/Epicalable/JARVIS-GUI/issues", new=1)

        elif event == 'Version':
            sg.popup_no_titlebar('---About J.A.R.V.I.S---',
                              'Version: 1.0',
                              'Copyright (C) 2022 Epicalable LLC')

window.close()

