import urllib.request
import wikipedia as wiki


def check_internet_connection():
    try:
        urllib.request.urlopen('http://google.com')
        return True 
    except:
        return False
    
def check_on_wiki(query):
    query = query.lower()
    query = query.replace("who is", "")
    query = query.replace("who was", "")
    query = query.replace("what is", "")
    query = query.replace("what was", "")
    query = query.replace("do you know", "")
    query = query.replace("tell me", "")
    query = query.replace("tell me about", "")
    query = query.replace("Which is", "")
    
    query = query.strip()
    
    try:
        data = wiki.summary(query, sentences=2)
        return data
    except Exception as e:
        return ""

# check_on_wiki("who is edolf hitler")
