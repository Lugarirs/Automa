import requests
import json
import xml.etree.ElementTree as ET
from datetime import datetime

# BBC News RSS Feed (free, no API key needed)
RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"

def fetch_headlines():
    print(f"Fetching headlines from BBC News RSS...")

    response = requests.get(RSS_URL, timeout=10)
    response.raise_for_status()

    # Parse XML
    root = ET.fromstring(response.content)
    channel = root.find("channel")

    headlines = []
    for item in channel.findall("item"):
        title = item.findtext("title", "").strip()
        link  = item.findtext("link", "").strip()
        pub_date = item.findtext("pubDate", "").strip()
        description = item.findtext("description", "").strip()

        if title:
            headlines.append({
                "title": title,
                "link": link,
                "published": pub_date,
                "description": description
            })

    return headlines


def save_to_json(headlines):
    output = {
        "scraped_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source": "BBC News RSS",
        "total": len(headlines),
        "headlines": headlines
    }

    with open("headlines.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(headlines)} headlines to headlines.json")


if __name__ == "__main__":
    headlines = fetch_headlines()
    save_to_json(headlines)
