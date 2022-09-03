import requests
from bs4 import BeautifulSoup
from .models import News


def get_vehicle_news():
    """
    get vehicle news from http://feeds.feedburner.com/autonews/BreakingNews
    """
    news = []
    try:
        print("Getting vehicle news...")
        url = "http://feeds.feedburner.com/autonews/BreakingNews"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='xml')
        items = soup.find_all("item")
        for item in items:
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            creator = item.creator.text
            description = item.description.text
            vehicle_news = {
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "creator": creator,
                "description": description,
            }
            news.append(vehicle_news)
        print("Finished getting vehicle news...")
        print("--------------------------------")

    except Exception as e:
        print("Error getting vehicle news: " + str(e))

    return save_vehicle_news(news)


def save_vehicle_news(vehicle_news):
    """
    save vehicle news
    """
    print(" Start saving vehicle news...")
    for news_article in vehicle_news:
        try:
            News.objects.create(
                title=news_article['title'],
                link=news_article['link'],
                pub_date=news_article['pub_date'],
                creator=news_article['creator'],
                description=news_article['description'],
            )
        except Exception as e:
            print(f'Failed to save vehicle news: {e}')
            break
    return print(" Finishing saving vehicle news...")



