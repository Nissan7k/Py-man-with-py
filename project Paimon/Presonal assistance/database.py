import sqlite3
import internet as it
# import output_module as om
# from internet import check_internet_connection


def create_connection():

    connection = sqlite3.connect("memory.db")
    return connection


def get_qns_and_ans():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM questionsAndAnswers")

    return cur.fetchall()


def insert_qns_and_ans(qns, ans):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO questionsAndAnswers values('"+qns+"', '"+ans+"')"
    cur.execute(query)
    con.commit()

    

def get_ans_from_memory(qns):
    rows = get_qns_and_ans()
    if "open" in qns:
        return "open"
    
    if rows is not None:
        ans = ""
        for row in rows:
            if row[0] and row[0].lower() in qns.lower():
                ans = row[1]
                break
        return ans
    
def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT val FROM memory WHERE name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]

def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set val = '"+new_name+"' where name = 'assistant_name' "
    cur.execute(query)
    con.commit()
    
def update_last_seen_date(lastDate):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set val = '"+str(lastDate)+"' where name = 'last_seen_date' "
    cur.execute(query)
    con.commit()


def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT val FROM memory WHERE name = 'last_seen_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])


def speech_on():
    if (it.check_internet_connection()):
        con = create_connection()
        cur = con.cursor()
        query = "update memory set val = 'on' where name == 'speech' "
        cur.execute(query)
        con.commit()
        
        return("Speech turned on")

    else: 
        return("Sorry! No internet connection")
    
def speech_off():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set val = 'off' where name == 'speech' "
    cur.execute(query)
    con.commit()
    return("Speech turned off")
    
    
def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT val FROM memory WHERE name == 'speech'"
    cur.execute(query)
    rows = cur.fetchall()

    if str(rows[0][0]) == "on":  
        return True
    else:
        return False
