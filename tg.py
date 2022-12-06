import requests
from bs4 import BeautifulSoup as bs


def telegram(username):
    try:
        base_url = f"https://telegram.dog/{username}"  
        r = requests.get(base_url).text
       
        soup = bs(r,"lxml")
       
        members_count = soup.find("div",class_="tgme_page_extra").text.replace(" ","").split("subscribers")[0]
      
        channel_name = soup.find("div", class_="tgme_page_title").text.replace("\n","")
       
        if soup.find("div", class_="tgme_page_description") is None:
            description=""
        else:    
            description=soup.find("div", class_="tgme_page_description").text
      
        dp = soup.find("img",class_="tgme_page_photo_image")['src']
      
        
        data = {}
        data['name'] = channel_name #Can be used as public group also
        data['subs'] = members_count
        data['description'] = description
        data['image'] = dp
        return data
    except Exception as e:
        return {"status":"400","error":"Username not found!!"}
