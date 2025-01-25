import webbrowser

def open_facebook():
    webbrowser.open("http://facebook.com")
    
def open_google():
    webbrowser.open("http://google.com")
    
def open_browser(browser):
    webbrowser.open("http://"+browser+".com")