import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for page in range(1, 11):

    print(f"Scraping Page {page}")

    url = f"https://quotes.toscrape.com/page/{page}/"

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        quotes = soup.find_all(
            "div",
            class_="quote"
        )

        for quote in quotes:

            text = quote.find(
                "span",
                class_="text"
            ).text.strip()

            author = quote.find(
                "small",
                class_="author"
            ).text.strip()

            data.append({
                "Quote": text,
                "Author": author
            })

    except Exception as e:

        print("Error:", e)

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df.to_csv(
    "quotes.csv",
    index=False
)

df.to_json(
    "quotes.json",
    orient="records",
    indent=4
)

print("CSV Saved Successfully")
print("JSON Saved Successfully")
print("Total Records:", len(df))