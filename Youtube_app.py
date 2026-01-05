import webbrowser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import Tk, Button, Label, Entry, StringVar, Listbox, END, SINGLE

#variable name
SLEEP_TIME = 2 #time that we wait until the page open
YOUTUBE_URL = "https://www.youtube.com" #youtube url must be in the beginning
SEARCH_URL = "https://youtube.com/results?search_query=" #the url address that we are looking for
TITLE_REQUEST_FROM_USER = "Enter the song name:" #what we are asking from the user as a title

WINDOW_OPEN_TITLE = "YouTube Song Search" #the title of the window that open
WINDOW_FRAME_SIZE = "300x300" #the size of the window that open
WINDOW_BACKGROUND_COLOR = "white" #the window background

INPUT_FRAME_COLOR = "white" #the frame color
TITLE_FONT = "Arial" #the font for the title
TITLE_SIZE = 14 #the size of the title

INPUT_FONT = "David" # the input font
INPUT_F0NT_SIZE = 10 # the input font size
INPUT_BOX_SIZE = 20 # the size of the box

BUTTON_LABEL = "ENTER" #the request from the user that show on the button
BUTTON_FONT = "Ariel" #the button font
BUTTON_FONT_SIZE = 10 #the button size
BUTTON_BACKGROUND = "white" #the color of the background of the button
BUTTON_FONT_COLOR = "Black" #the font color

OPTIONS_FONT = "David" #the options font
OPTIONS_FONT_SIZE = 12 #the options size font
OPTIONS_WINDOW_SIZE = 50 #the window size
OPTION_WINDOW_HIGH_SIZE = 10 #the high of the options window


class YouTubeDisplayProgram:
    def __init__(self, window_size):
        self.window_size = window_size

    # Function to fetch HTML content using Selenium
    def get_html_content(self, search_url):
        #useing Selenium in order to get access to YouTube
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(search_url)
        time.sleep(SLEEP_TIME) #Wait for the page to open
        element = driver.find_element(By.CSS_SELECTOR, "html")
        html = element.get_attribute("outerHTML")
        driver.quit()
        return html

    # Function to parse the HTML and update the listbox
    def update_list(self, html, listbox):
        # getting the url by using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.select('h3:has(a)') #getting the YOUTUBE video title
        lst_of_options = []  # Empty list for the songs options
        listbox.delete(0, END)  # Clear the listbox before populating

        for k, link in enumerate(links):  # k is the index and link is the clip
            txt = link.text.strip() #get the text from the link
            a = link.select("a")[0]['href'] # get the url from the link
            lst_of_options.append({'name': txt, 'url': a})
            listbox.insert(END, txt)  # Add the song name to the listbox
            if k == 5: # limit the result to 5 options
                break
        return lst_of_options

    """Function to handle the user's selection and open the song URL
    The function get the list of options(listbox) and the 
    list with the song name(lst_of_options)"""
    def user_select(self, listbox, lst_of_options):
        if listbox.curselection(): # if the user choose option from the list
            index = listbox.curselection()[0] #get the index of the selection
            song_url = YOUTUBE_URL + lst_of_options[index]['url'] #get the full url
            webbrowser.open_new(song_url)

    """Function to handle the search process and update the listbox with results
    The function get the user's song name input(entry_song_name), searching on youtube (user can't see it), 
    and updates the listbox with 5 options"""

    def search_and_open(self, entry_song_name, listbox):
        search = entry_song_name.get() #get the input from the user
        search_url = SEARCH_URL + str(search) #bulding the full url
        html = self.get_html_content(search_url) #useing the fanction that getting the youtube video
        lst_of_options = self.update_list(html, listbox) #getting the HTML and update the listbox with the parsed song options
        """using lambda to pass the necessary arguments"""
        listbox.bind('<<ListboxSelect>>', lambda choose: self.user_select(listbox, lst_of_options))


    # Function to create and display the GUI
    def create_gui(self):
        # Using GUI
        root = Tk()

        root.title(WINDOW_OPEN_TITLE)
        root.geometry(WINDOW_FRAME_SIZE)
        root.configure(bg=WINDOW_BACKGROUND_COLOR)

        # Create a frame
        frame = tk.Frame(root, bg=INPUT_FRAME_COLOR)
        frame.pack(pady=20)

        # Label for the song name with bold font
        song_name = Label(frame, text=TITLE_REQUEST_FROM_USER, bg=WINDOW_BACKGROUND_COLOR, font=(TITLE_FONT, TITLE_SIZE, 'bold'))
        song_name.pack(pady=10)

        # Entry field for the song name
        our_var1 = StringVar()
        entry_song_name = Entry(frame, textvariable=our_var1, font=(INPUT_FONT, INPUT_F0NT_SIZE), width=INPUT_BOX_SIZE)
        entry_song_name.pack(pady=10)

        # Button to the search
        print_button = Button(frame, text=BUTTON_LABEL, command=lambda: self.search_and_open(entry_song_name, listbox), font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg=BUTTON_BACKGROUND, fg=BUTTON_FONT_COLOR)
        print_button.pack(pady=10)

        # Listbox to display song options
        listbox = Listbox(frame, selectmode=SINGLE, font=(OPTIONS_FONT, OPTIONS_FONT_SIZE), width=OPTIONS_WINDOW_SIZE, height=OPTION_WINDOW_HIGH_SIZE)
        listbox.pack(pady=10)
        root.mainloop()


if __name__ == '__main__':
    program = YouTubeDisplayProgram(WINDOW_FRAME_SIZE)
    program.create_gui()