from datetime import datetime, date

def get_time():     
    now = datetime.now()
    current_time = now.strftime(" %H hour and %M minute")
    return("Current time is " + current_time)

def get_hour():     
    now = datetime.now()
    return (now.strftime("%H"))

def get_date():
    return str(date.today())
    