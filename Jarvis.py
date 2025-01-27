
import datetime
import tkinter as tk
from tkinter import *
import random
import json
import requests
import torch
import torch.nn as nn
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()



class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
    
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def quit():
    global root
    root.destroy()

class Exset():

    def __init__(self):
        self.settings()

    def settings(self):
        setting = tk.Toplevel(root)
        setting.title("SETTINGS")
        setting.geometry("480x360")
        setting.resizable(False, False)
        setting.configure(bg='gray37')
        setting.wm_attributes("-topmost",True)
        Label(setting, text = "Settings Window", bg='gray37').grid(row=0)
        Label(setting, text='NewsApiKey: ', bg='gray37').grid(row=2)
        Label(setting, text='OpenWeatherApiKey: ', bg='gray37').grid(row=3)
        Label(setting, text='Current Country: ', bg='gray37').grid(row=4)
        Label(setting, text='Current City: ', bg='gray37').grid(row=5)
        self.e1 = Entry(setting)
        self.e2 = Entry(setting)
        self.e3 = Entry(setting)
        self.e4 = Entry(setting)
        self.e1.grid(row=2, column=1)
        self.e2.grid(row=3, column=1)
        self.e3.grid(row=4, column=1)
        self.e4.grid(row=5, column=1)

        button = tk.Button(setting, text="Enter", command= self.retrieve_setting)
        root.bind('<Return>', lambda event=None: button.invoke())
        button.grid(row=6,column=1)


    def retrieve_setting(self):
        i=self.e1.get() 
        ii=self.e2.get()
        v=self.e3.get() 
        vv=self.e4.get()
        dictionary = {
                "!CAUTION!": "PLEASE REFRAIN from TAMPERING with the BELOW DATA!!!",
                "NewsApiKey": i,
                "OpenWeatherKey": ii,
                "Country": v,
                "City": vv
        }
        json_object = json.dumps(dictionary, indent=4)
        with open("Jarsettings.json", "w") as outfile:
            outfile.write(json_object)



    

def Weather(timeing):
    try:
        key = "b190a0605344cc4f3af08d0dd473dd25"
        Place = "Singapore"
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
            we = " Temperature: "+str(current_temp)+"°C"+"\n Humidity: "+str(current_humidiy)+"%"+"\n Description: "+str(weather_description)
            textbox.insert(tk.END,timeing + Place + ":\n")
            textbox.insert(tk.END,we)
        else:
            textbox.insert(tk.END,"JARVIS: Please check your city in the settings as this is invalid.")
    except:
        textbox.insert(tk.END,"JARVIS: I am having a problem in getting live weather please check your internet-connection.")


def Breifing():
    str = 'general business science health technology entertainment sports'
    JNews = "4c2159b38736423cb393853bda9e642f"
    country = "us"
    headers = {'Authorization': JNews}
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'

    try:
        headers = {'Authorization': JNews}
        top_headlines_url = 'https://newsapi.org/v2/top-headlines'
        splits = str.split()
        for split in splits:
            textbox.insert(tk.END,"\n" + split.upper() + ":--"+"\n")
            headlines_payload = {'category': split, 'country': country}
            open_news_page = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload).json()
            article = open_news_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                e = i + 1 <= 9
                z= results[i] +'\n'
                textbox.insert(tk.END,z)
                if e == False:
                    break
    except:
        textbox.insert(tk.END,"JARVIS: Something went wrong!!!" +
              "\nJARVIS: Please check if you have a good internet connection and have given a valid category and location.")


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        textbox.configure(state="normal")
        timeing = "JARVIS: Good Morning Sir, here is the current weather in "
        Weather(timeing)
        Breifing()
        textbox.insert(tk.END,"\n")
        textbox.configure(state="disabled")
    elif hour >= 12 and hour < 18:
        textbox.configure(state="normal")
        timeing = "JARVIS: Good Afternoon Sir, here is the current weather in "
        Weather(timeing)
        textbox.insert(tk.END,"\n\n")
        textbox.configure(state="disabled")
    else:
        textbox.configure(state="normal")
        timeing = "JARVIS: Good Evening Sir, here is the current weather in "
        Weather(timeing)
        textbox.insert(tk.END,"\n\n")
        textbox.configure(state="disabled")


def jarsearch(sentence):
    while True:
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)
        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    out= "JARVIS: " + str(random.choice(intent['responses'])) + "\n\n"
                    textbox.configure(state="normal")
                    textbox.insert(tk.END, out)
                    textbox.configure(state="disabled")
        else:
            textbox.configure(state="normal")
            textbox.insert(tk.END,("JARVIS: Sorry sir unfortunately I couldn't process what you were trying to say.\n."))
            textbox.configure(state="disabled")



def retrieve_input():
    inputValue=myentry.get("1.0","end-1c")
    textbox.configure(state="normal")
    textbox.insert(tk.END,"User: " + inputValue.capitalize())
    textbox.configure(state="disabled")
    myentry.delete('1.0', END)
    inputValue = inputValue.lower()
    inputValue = inputValue+" "

    if "date " in inputValue or "time " in inputValue:
        textbox.configure(state="normal")
        x = datetime.datetime.now()
        z = ("JARVIS: The Date and Time is {dat} respectively sir.\n").format(dat=x)
        textbox.insert(tk.END,z)
        textbox.configure(state="disabled")

    elif "latest news " in inputValue:
        textbox.configure(state="normal")
        Breifing()
        textbox.insert(tk.END,"\n\n")
        textbox.configure(state="disabled")

    elif "headlines " in inputValue:
        textbox.configure(state="normal")
        Breifing()
        textbox.insert(tk.END,"\n\n")
        textbox.configure(state="disabled")

    elif "whats going on " in inputValue:
        textbox.configure(state="normal")
        Breifing()
        textbox.insert(tk.END,"\n\n")
        textbox.configure(state="disabled")

    else:
        jarsearch(inputValue)



root = tk.Tk()
root.title('JARVIS AI')
root.geometry("1200x720")
root.resizable(False, False)
root.configure(bg='gray37')
########
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label = "Settings", command = Exset)
file.add_command(label = "Quit", command = quit)  
menubar.add_cascade(label = "Menu", menu = file)  
########
myLabel = tk.Label(root, text = "JARVIS AI (C) EPICALABLE")
myLabel.pack()

textbox = tk.Text(root, bg="gray12", fg="azure", height=40, width=165, font=('Arial',10))
textbox.pack()
textbox.configure(state="disabled")
greeting()
myentry = tk.Text(root , bg="gray12", fg="azure", width=145, height=2,font=('Arial',10))
myentry.pack(padx=19,side=tk.LEFT)

button = tk.Button(root, bg="gray12", fg="azure", width=40, text="Enter", command=lambda: retrieve_input(), font=('Arial',10))
root.bind('<Return>', lambda event=None: button.invoke())
button.pack(padx=19,side=tk.RIGHT)

root.config(menu=menubar)  
root.mainloop()