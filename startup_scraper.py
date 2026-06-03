import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

base_url = "https://quotes.toscrape.com/page/{}/"

for page in range(1, 6):

    print(f"Scraping Page {page}")

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find("span", class_="text").text

        author = quote.find("small", class_="author").text

        tags = ", ".join(
            [tag.text for tag in quote.find_all("a", class_="tag")]
        )

        data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags
        })

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df.to_csv("quotes.csv", index=False)

df.to_json(
    "quotes.json",
    orient="records",
    indent=4
)

print("CSV Saved Successfully")
print("JSON Saved Successfully")
print("Total Records:", len(df))
