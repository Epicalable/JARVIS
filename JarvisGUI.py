#J.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.
#For Gui EXE: pyinstaller -wF my_program.py (Runs Without shell window)
#If pyinstaller crashes add: --hidden-import tkinter
import PySimpleGUI as sg
import datetime
from datetime import date
import time
import requests
import json
import smtplib
import wikipedia
import webbrowser
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import geocoder
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
            Audfile.writelines(querytime + "-(User Successfully Recieved Weather Report Using OpenWeatherMap.) \n")
            Audfile.close()
        else:
            print("JARVIS: Please check your city in the settings as this is invalid.")
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(ERROR:801, User's City Is Invalid. Please Try Again.) \n")
            Audfile.close()
    except:
        print("JARVIS: I am having a problem in getting live weather please check your internet-connection.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(
            querytime + "-(ERROR:805, Connection Failed with OpenWeatherMap. Please Check your Connection.) \n")
        Audfile.close()


def location():
    #initialize the object
    Nomi_locator = Nominatim(user_agent="Jarvis")
    my_location = geocoder.ip('me')
    #latitude and longitude coordinates
    latitude = my_location.geojson['features'][0]['properties']['lat']
    longitude = my_location.geojson['features'][0]['properties']['lng']
    #getting location
    location = Nomi_locator.reverse(f"{latitude}, {longitude}")
    print("Your Current location is", location)
    Audfile = open("Jaraudit.txt", "a")
    querytime = (datetime.datetime.now().ctime())
    Audfile.writelines(querytime + "-(User Recieved His Current Location Using GeoCoder.) \n")
    Audfile.close()


def stock_price(symbol: str = "AAPL") -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px) W(100%)"
    return soup.find("div", class_=class_).find("fin-streamer").text


def Breifing(title):
    str = 'general business science health technology entertainment sports'
    with open("Jarinfo.json") as f:
        contents = json.load(f)
        JNews = contents["NewsApiKey"]
        country = contents["Country"]
    headers = {'Authorization': JNews}
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'

    if title == 'Morning Briefing':
        try:
            headers = {'Authorization': JNews}
            top_headlines_url = 'https://newsapi.org/v2/top-headlines'
            splits = str.split()
            for split in splits:
                print("\n" + split.upper() + ":--")
                headlines_payload = {'category': split, 'country': country}
                open_news_page = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload).json()
                article = open_news_page["articles"]
                results = []
                querytime = (datetime.datetime.now().ctime())
                for ar in article:
                    results.append(ar["title"])
                for i in range(len(results)):
                    e = i + 1 <= 9
                    print(i + 1, '.', results[i])
                    if e == False:
                        break
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(User Recieved Morning Briefing From NewsAPI.) \n")
            Audfile.close()
        except:
            print("JARVIS: Something went wrong!!!" +
                  "\nJARVIS: Please check if you have a good \ninternet connection and have given a valid \ncategory and location.")
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(
                querytime + "-(ERROR:755, Connection Failed with NewsAPI. Please Check Your Connection.) \n")
            Audfile.close()
    else:
        try:
            headers = {'Authorization': JNews}
            top_headlines_url = 'https://newsapi.org/v2/top-headlines'
            splits = str.split()
            for split in splits:
                print("\n" + split.upper() + ":--")
                headlines_payload = {'category': split, 'country': country}
                open_news_page = requests.get(
                    url=top_headlines_url, headers=headers, params=headlines_payload).json()
                article = open_news_page["articles"]
                results = []
                querytime = (datetime.datetime.now().ctime())
                for ar in article:
                    results.append(ar["title"])
                for i in range(len(results)):
                    print(i + 1, '.', results[i])
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(User Recieved News Headlines From NewsAPI.) \n")
            Audfile.close()
        except:
            print("JARVIS: Something went wrong!!!" +
                  "\nJARVIS: Please check if you have a good \ninternet connection and have given a valid \ncategory and location.")
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(
                querytime + "-(ERROR:765, Connection Failed With NewsAPI. Please Check Your Connection.) \n")
            Audfile.close()


def Settings():
    sg.theme('Dark')
    with open("Jarinfo.json") as f:
        contents = json.load(f)
        User = contents["User"]
        NewsApiKey = contents["NewsApiKey"]
        OpenWeatherKey = contents["OpenWeatherKey"]
        Country = contents["Country"]
        City = contents["City"]
        StockPrice = contents["StockPrice"]
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
              [sg.T('Stock-Price:', size=(13, 1)), sg.Input(
                  StockPrice, key='-Stock-', size=(34, 1))],
              [sg.Text('GUI-Customization:--', font='Default 12')],
              [sg.Text(
                  'Enter only in Numbers to adjust the UI screen size.', font='Default 10')],
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
            StockPrice = values['-Stock-']
            Outputsc = values['-Outsc-']
            Inputbr = values['-Inbr-']
            dictionary = {
                "!CAUTION!": "PLEASE REFRAIN from TAMPERING with the BELOW DATA!!!",
                "User": User,
                "NewsApiKey": newsapikey,
                "OpenWeatherKey": weatherkey,
                "Country": Country,
                "City": City,
                "StockPrice": StockPrice,
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
        Audfile.writelines(
            querytime + "-(User Successfully sent An Email To It's Destination.) \n")
        Audfile.close()
        s.quit()    # terminating the session
    except:
        sg.popup("Please check your internet connection and have turned 'on' Less secure app access in 'security' section in your Google Account Settings.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(
            querytime + "-(ERROR:300, User Failed To Send An Email To It's Destination.) \n")
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


def ChatLog():
    with open('Jaraudit.txt') as file:
        h = file.read()
        file.close()
    sg.popup_scrolled(h, title="ChatLogs", size=(90, 30))


def Tasks():
    sg.theme('Dark')
    try:
        with open('task.txt') as f:
            mylist = []
            for line in f:
                words = line.split()
                mylist += words
    except FileNotFoundError:
        with open('task.txt', 'w') as f:
            first = "Enter tasks here"
            f.writelines(first)

    layout = [[sg.Text('TASKS (Use commas to seperate tasks):', font='Default 16')],
              [sg.T('Tasks:', size=(10, 5)),
               sg.Input(mylist, key='-User-', size=(50, 10))],
              [sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('tasks', layout, no_titlebar=True, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Save':
            tasks = values['-User-']
            tasks = tasks.replace('{', "")
            tasks = tasks.replace('}', "")
            tasks = tasks.replace("\n", "")
            with open('task.txt', 'w') as f:
                f.writelines(tasks)
            break
    window.close()
    event = window.read()
    return event != 'OK'

    
    
def Help():
    sg.popup_scrolled("""Welcome to the Help Centre
            1. Setting up JARVIS: -----------
            JARVIS have the ability to chat once installed by default.
            The User will then need to register at these following websites:

            1. https://newsapi.org/: To integrate live news.

            2. https://openweathermap.org/ : To integrate live weather.

            Both websites once registered will provide you an API key.
            Users should then copy the API key and paste it 
            in the respective bars in the settings menu.
            News will need your country location 
            (only morning briefing)
            so Please enter your country's abbreviation.
            Example: au, cz, de, in , sg, us, uk
            Weather will need your city location 
            (when always entering JARVIS)
            so please enter your city's name.
            Example: Delhi, Dubai, New york, London, Singapore, Sydney

            2. Commands to run JARVIS: ------------
            To make JARVIS respond Users will need to enter a Command
            in the input for which JARVIS will scan for keywords
            and provide an answer or information

            Here is a sample list of available Commands:
                ---Hello
                ---How are you
                ---Are you fine
                ---Are you real
                ---What is the time
                ---News about[your input]
                    EX. News about Github.
                ---Get me news headlines
                    NOTE: Type in country's abbreviation in input bar in Newsui.
                ---Send an email
                ---Wikipedia[Query]
                    EX. Wikipedia github.
                ---Who is [Query] / What is [Query]
                    NOTE: JARVIS will get answer from Wikipedia.
                ---Get me stock price
                    NOTE: Query of stock should be abbreviations.
                    NOTE: Stock abbrevatiion should be placed in Settings.
                    EX. TSLA AAPL MSFT IBM GOOG (Place under "StockPrice").
                ---Goodbye
                    NOTE: Command to quit JARVIS.

            J.A.R.V.I.S Copyright(C) 2022 Epicalable LLC. 
            All Rights Reserved.""", title="Help Centre", size=(90, 30))






Audfile = open("Jaraudit.txt", "a")
querytime = (datetime.datetime.now().ctime())
Audfile.writelines(querytime + "-(USER ACTIVATED JARVIS AND INITIALIZED RELATED PROCESSES!!!) \n")

with open("Jarinfo.json") as f:
    contents = json.load(f)
    LoadOutput = contents["Outputscreensize"]
    LoadInput = contents["Inputbarsize"]
sg.theme('DarkGrey8')  # gives window a color
sg.set_options(element_padding=(3, 3))
menu_def = [['&MENU ', ['&Settings', '&ChatLogs', '&Your Tasks','E&xit']],
            ['&HELP', ['&Help', '&Report Issue', '&Version']],
            ['&ABOUT US', ['&Support Us', '&Our Website']], ]
layout = [[sg.Menu(menu_def, tearoff=False)],
          [sg.Text('J.A.R.V.I.S  A.I', size=(135, 1)),
           sg.Text(('(C) Epicalable'), size=(20, 1))],
          [sg.Output(size=(LoadOutput, 38), font=('Helvetica 10'))],
          [sg.Multiline(size=(LoadInput, 2), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('ENTER', size=(11, 2), bind_return_key=True)]]
window = sg.Window('J.A.R.V.I.S GUI', layout, location=(0, 0), icon=r'icon/JarvisBot.ico', font=(
    'Helvetica', ' 13'), default_button_element_size=(8, 2)).Finalize()
window.maximize()


hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    timeing = "JARVIS: Good Morning Sir, here is the current weather in "
    location()
    Weather(timeing)
    Breifing('Morning Briefing')
elif hour >= 12 and hour < 18:
    timeing = "JARVIS: Good Afternoon Sir, here is the current weather in "
    location()
    Weather(timeing)
else:
    timeing = "JARVIS: Good Evening Sir, here is the current weather in "
    location()
    Weather(timeing)

if __name__ == '__main__':
    while True:     # The Infinity Event Loop
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # quit if exit button or X
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(
                querytime + "-(USER TERMINATED JARVIS AND ALL IT'S RELATED PROCESSES!!!) \n")
            Audfile.close()
            print("\nJARVIS: Goodbye sir hope you have a nice day :-)")
            print("\nJ.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.")
            time.sleep(4)
            break

        if event == 'ENTER':
            # THE START OF THE RENDER-WORD ENGINE (C) Epicalable
            que = value['-QUERY-'].rstrip()  # Your input here
            query = ((que.upper()) + " ")
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
                        if "STOCK " in query or "STOCK PRICE" in query:
                            with open("Jarinfo.json") as f:
                                contents = json.load(f)
                                Stocks = contents["StockPrice"]
                            for symbol in Stocks.split():
                                print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
                            Audfile = open("Jaraudit.txt", "a")
                            querytime = (datetime.datetime.now().ctime())
                            Audfile.writelines(
                                querytime + "-(User Have Recieved Stock-Price.) \n")
                            Audfile.close()
                            continue

                        elif "FLIGHT TRACK" in query or "TRACK FLIGHT " in query:
                            try:
                                query = query.replace('FLIGHT TRACK', "")
                                query = query.replace('TRACK FLIGHT ', "")
                                flight_num = query
                                date = date.today().strftime('%Y-%m-%d')
                                url = f"https://aerodatabox.p.rapidapi.com/flights/number/{flight_num}/{date}"

                                headers = { "X-RapidAPI-Key": "17f75df5efmsh9b4ae3bc52aebc4p120b7cjsn63e5ff22f6da",
	                                        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
                                          }
                                response = requests.request("GET", url, headers=headers)
                                format = json.dumps(response.json(), indent=4)
                                print(format)
                            except:
                                print("ERROR: Please Type flight number also")
                                print("Example: Track flight SQ 242")


                        elif "DATE " in query or "TIME " in query:
                            x = datetime.datetime.now()
                            print("JARVIS: The Date and Time is ",
                                  x, " respectively sir.")
                            continue

                        elif "DAY " in query or "YEAR " in query:
                            x = datetime.datetime.now()
                            print("JARVIS: The Date and Time is ",
                                  x, " respectively sir.")
                            continue

                        elif "WIKIPEDIA " in query or "WIKI " in query:
                            query = query.replace('WIKI', "")
                            query = query.replace('WIKIPEDIA', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(User Established Connection With Wikipedia.) \n")
                                Audfile.close()
                            except:
                                print(
                                    "JARVIS: I am having a problem in getting wikipedia please check your internet-connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(ERROR:500, Failed To Establish Connection With Wikipedia.) \n")
                                Audfile.close()
                            continue

                        elif "WHAT IS " in query or "WHO IS " in query:
                            query = query.replace('WHAT', "")
                            query = query.replace('IS', "")

                            query = query.replace('WHO', "")
                            query = query.replace('IS', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "JARVIS: I am having a problem in getting wikipedia please check your internet-connection")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION FAILED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "NEWS ABOUT " in query or "NEWS ON " in query:
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
                                    querytime + "-(User Recieved News From NewsAPI.) \n")
                                Audfile.close()
                                for ar in article:
                                    results.append(ar["title"])
                                for i in range(len(results)):
                                    print(i + 1, '.', results[i])
                            except:
                                print(
                                    "JARVIS: Something went wrong please check if you have a good internet connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(ERROR:776, Connection Failed With NewsAPI. Please Check Your Connection.) \n")
                                Audfile.close()
                                continue

                        elif "HEADLINES " in query:
                            Breifing('News Headlines')

                        elif "THE NEWS " in query:
                            Breifing('News Headlines')

                        elif "SEND AN EMAIL " in query or "SEND A EMAIL " in query:
                            gmail()

                        elif query == "GOODBYE ":
                            Audfile = open("Jaraudit.txt", "a")
                            querytime = (datetime.datetime.now().ctime())
                            Audfile.writelines(
                                querytime + "-(USER TERMINATED JARVIS AND ALL IT'S RELATED PROCESSES!!!) \n")
                            Audfile.close()
                            print("JARVIS: Goodbye sir hope you have a nice day :-)")
                            print(
                                "\nJ.A.R.V.I.S Copyright (C) 2022 Epicalable LLC. All Rights Reserved.")
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

        elif event == 'ChatLogs':
            ChatLog()

        elif event == 'Your Tasks':
            Tasks()

        elif event == 'Support Us':
            sg.popup_no_titlebar("Please star our 'JARVIS-GUI' github repository and also",
                                 "Subscribe and share our 'Epicalable' Youtube channel")
            webbrowser.open("https://github.com/Epicalable/JARVIS", new=1)

        elif event == 'Our Website':
            webbrowser.open(
                "https://epicalable.github.io/epicalable.html", new=1)

        elif event == 'Help':
            Help()

        elif event == 'Report Issue':
            webbrowser.open(
                "https://github.com/Epicalable/JARVIS-GUI/issues", new=1)

        elif event == 'Version':
            sg.popup_no_titlebar('---About J.A.R.V.I.S---',
                                 'Version: 1.0',
                                 'Copyright (C) 2022 Epicalable LLC')

window.close()
