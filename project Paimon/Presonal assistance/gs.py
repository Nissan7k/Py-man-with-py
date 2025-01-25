import requests
from bs4 import BeautifulSoup

def search_google(query):
    try:
        search_url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        answer_box = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'})
        if answer_box:
            answer = answer_box.text
            return answer
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
query = "what is flower"
search_result = search_google(query)
if search_result:
    print("Here's what I found on Google:", search_result)
else:
    print("Sorry, I couldn't find any information on Google.")

