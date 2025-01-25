
import time_module as tm
import output_module as om
import database as db
import datetime as dt

def greet():

    previous_date = db.get_last_seen()
    
    todays_date = tm.get_date()
    db.update_last_seen_date(todays_date)

    if previous_date == todays_date:
        om.output("Welcome back!")
    
    else:
        hour = int(tm.get_hour())

        if hour >= 0 and hour <= 12:
            om.output("Good Morning!")
        elif hour >= 12 and hour <= 17:
            om.output("Good Afternoon!")
        else:
            om.output("Good Evening!")
