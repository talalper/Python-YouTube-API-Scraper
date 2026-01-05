# YouTube Song Searcher (OOP Project)
Project Description
A Python-based desktop application developed as part of an Object-Oriented Programming course. 
The app allows users to search for any song or artist (in Hebrew or English), displays the top 5 results, and opens the selected video directly in the browser.

Key Features
* Automated Search: Uses Selenium in headless mode to navigate YouTube and BeautifulSoup to parse and extract video titles and URLs.
* Interactive GUI: A custom-designed interface built with Tkinter, featuring a user-friendly search box and result selection.
* Smart Parsing: Processes search results into a list of dictionaries for efficient data management.

Technical Architecture
The project is built using a Class-based approach (YouTubeDisplayProgram) to maintain OOP principles.

Main Functions:
* get_html_content: Handles the web-driver logic and page loading.
* update_list: Parses HTML content and populates the UI listbox.
* user_select: Manages the selection logic and triggers the browser event.

Installation
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt
3. Run main.py.
