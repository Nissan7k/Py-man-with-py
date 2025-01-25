import output_module as om
import time_module as tm
import input_module as im
import database as db
from internet import check_internet_connection, check_on_wiki
import assistant_detail as ad
import speak_module as sm
import web_job as wj
import random
import news
# import music_player as mp
# import location as loc


def process(query):
 
    
    ans = db.get_ans_from_memory(query)
    
    
    
    if ans == "get time details":
        return(tm.get_time())
    
    elif ans == "check internet connection":
        if check_internet_connection():
            return "Internet is connected"
        else:
            return "Internet is not connected"
        
    elif ans == "tell date":
        return "Today is " + tm.get_date()
    
    elif ans == "welcome":
        reply = {
            1 : "Your Welcome",   
            2 : "It was my pleasure!",
            3 : "Mention not",
            4 : "Welcome!",   
        }
        random_number = random.randint(1,4)
        return reply[random_number]

    elif ans == "on speak":
        result = db.speech_on()
        if db.speak_is_on():
            # sm.speak("Speech turned on")  # Speak only if speech is on
            pass
        return "Speech turned on"



    elif ans == "off speak":
            return db.speech_off()
    
    elif ans == "get news":
        return news.get_news()

    elif ans == "name":
        return "My name is paimon"
    
    elif ans == "information":
        return "I am Paimon, a basic digital assistant created by group Nkaps"
    
    elif ans == "open facebook":
        wj.open_facebook()
        return "opening facebook"
    
    elif ans == "open google":
        wj.open_google()
        return "opening google"
    
    # elif ans == "get location":
    #     a =loc.get_current_location()
    #     return "current location is: (latitude, longitude)" + a

    elif "open" in ans:
        query = query.replace("open", "")
        query = query.strip()
        wj.open_browser(query)
        return "opening " + str(query)  
    
    elif "marriage" in ans:
        reply = {
            1 : "I appreciate the sentiment, but I must kindly decline.",   
            2 : " I don't possess personal emotions",
            3 : "I'm not capable of forming personal relationships or marriage",
        }
        random_number = random.randint(1,3)
        return reply[random_number]

    elif "hi reply" in ans:
        reply = {
            1 : "Hello!, How may I help you?",   
            2 : "Hey!, what's up?",
            3 : "Hi!, How may I help you?",
            4 : "Hey!, How may I help you?",
            5 : "Hi!, what's up?"
        }
        random_number = random.randint(1,5)
        return reply[random_number]

    elif "confession" in ans:
        reply = {
            1 : "I love you too",   
            2 : "I am flattered to hear",
            3 : "Sorry, I don't have feeling",
            4 : "I knew, you loved me",
        }
        random_number = random.randint(1,4)
        return reply[random_number]



    elif "health condition" in ans:
        reply = {
            1 : "I am Fine, How are you?",   
            2 : "I am fine, Thank you for your concern",
            3 : "Always fine!",
            4 : "Never better than this",
            5 : "Fine!, what about you?"
        }
        random_number = random.randint(1,5)
        return reply[random_number]

    elif "fine user" in ans:
        reply = {
            1 : "Ohh, ok",   
            2 : "good to hear",
            3 : "ok, then how may i help you",
        }
        random_number = random.randint(1,3)
        return reply[random_number]

    elif "not fine user" in ans:
        reply = {
            1 : "Ohh, get well soon",   
            2 : "I will pray for your recovory",
            3 : "Ohh, Please visit doctor",
            4 : "Then, you should go for check up",
            5 : "Drink turmeric water"
        }
        random_number = random.randint(1,5)
        return reply[random_number]         
        

    elif ans == "change name":    
        om.output("What do you want to name me?")
        temp = im.take_input()
        if temp == ad.name:
            om.output("Can't change, it's my previous name!")
        else:
            db.update_name(temp)
            ad.name = temp
            return "Sure now I will call myself " + temp
        
    else:
        ans = check_on_wiki(query)
        if ans != "":
            om.output("Here's what I found on web")
            return ans 

        else:   
            om.output("I dont know, can you please tell me what it is!")
            ans = im.take_input()
            if "it means" in ans:
                    ans = ans.replace("it means", "")
                    ans = ans.strip()
                    
                    value = db.get_ans_from_memory(ans)
                    if value == "":
                        return "can't help with this one"
                    else:
                        db.insert_qns_and_ans(query, value)
                        return "Thanks, I will remember it"
            else:
                    return "Can't help with this"
                    
