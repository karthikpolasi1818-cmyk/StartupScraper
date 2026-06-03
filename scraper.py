import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

pages = [
    "https://news.ycombinator.com/",
    "https://news.ycombinator.com/news?p=2",
    "https://news.ycombinator.com/news?p=3"
]

for url in pages:

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        titles = soup.find_all("span", class_="titleline")

        for title in titles:

            headline = title.text

            link = title.find("a")["href"]

            data.append({
                "Headline": headline,
                "Link": link
            })

    except Exception as e:
        print("Error scraping:", url)
        print(e)

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df.to_csv("startup_news.csv", index=False)

df.to_json(
    "startup_news.json",
    orient="records",
    indent=4
)

print("CSV Saved Successfully")
print("JSON Saved Successfully")
print("Total Records:", len(df))