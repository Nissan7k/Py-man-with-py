import requests	 
import internet as irt
import output_module as om

def get_news():
    if irt.check_internet_connection():    
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "6c93e5d77c7c4bc0b87e914527c4c972"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will 
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            
            # printing all trending news
            om.output(str(i + 1)+ ".) "+ results[i])
        
        return "these were the top news of today!"

    else:
        return "Please check your internet connection"

