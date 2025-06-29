import requests
from bs4 import BeautifulSoup

print(requests.__version__)
print("my scraper is running")

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    quotes =soup.find_all("div",class_="quote")
    result=[]
    for quote in quotes:
        text=quote.find("span",class_="text").get_text()
        author=quote.find("small",class_="author").get_text()
        result.append({"quote":text,"author":author})
    return result

if __name__ == "__main__":
    data=scrape_quotes()
    for item in data:
        print(f"{item['quote']}-{item['author']}")

    