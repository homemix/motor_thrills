import requests
from bs4 import BeautifulSoup
from .models import News, Vehicle, Company


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


def get_vehicle_details():
    """
    get vehicle details by url
    from be forward company: https://www.beforward.jp
    Categories for vehicle details= {
    2: Honda,
    3: Nissan,
    94: Subaru etc
    }
    """
    vehicles = []
    #  company ID for be forward is 2
    company = Company.objects.filter(pk=2).first()
    try:
        print("Getting vehicle details...")
        url = "https://www.beforward.jp/stocklist/make=94/sar=steering/sortkey=n/steering=Right/tp_country_id=27"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        vehicle_details = soup.find_all("tr", {"class": "stocklist-row"})

        vehicle = {}

        for vehicle_detail in vehicle_details:
            vehicle_make_models = vehicle_detail.find_all("p", {"class": "make-model"})
            vehicle_specs = vehicle_detail.find_all("table", {"class": "basic-spec-row"})
            vehicle_images = vehicle_detail.find_all("td", {"class": "stocklist-col photo-col"})
            vehicle_price = vehicle_detail.find_all("div", {"class": "price-col-vehicle-link-area"})
            for prices in vehicle_price:
                price = prices.find("span", {"class": "price"}).text
                vehicle['price'] = price

            for vehicle_image in vehicle_images:
                image = vehicle_image.find('img').get('src')[2:]
                vehicle['image'] = f'https://{image}'

            for spec in vehicle_specs:
                millage = spec.find('td', {"class": "basic-spec-col basic-spec-col-bordered mileage"}).find('p', {
                    "class": "val"}).text
                transmission = spec.find('td', {"class": "basic-spec-col basic-spec-col-bordered trans"}).find('p', {
                    "class": "val"}).text
                engine = spec.find('td', {"class": "basic-spec-col basic-spec-col-bordered engine"}).find('p', {
                    "class": "val"}).text
                millage = " ".join(millage).strip()
                engine = " ".join(engine).strip()

                vehicle['millage'] = millage
                more_info = f'millage: {millage} engine: {engine} transmission: {transmission}'
                vehicle['more_info'] = more_info

            for vehicle_make_model in vehicle_make_models:
                vehicle_name = vehicle_make_model.find('a', attrs={'class': 'vehicle-url-link'}).text
                name_cleaned = " ".join(vehicle_name.split())
                YOM = name_cleaned.split(' ')[0]
                make = name_cleaned.split(' ')[1]
                name = ' '.join([str(elem) for elem in name_cleaned.split(' ')[2:]])

                vehicle['YOM'] = YOM
                vehicle['make'] = make
                vehicle['name'] = name
                vehicle['company'] = company

                # print(f'name:{name} YOM: {YOM} image:{image} price:{price} make:{make} millage:{millage}')
                vehicle_save = Vehicle(name=name, YOM=YOM, image=f'https://{image}',
                                       price=price, make=make,
                                       millage=millage,
                                       more_info=more_info, company=company)

                vehicle_save.save()

            # vehicles.append(vehicle)

        print("Finished getting vehicle details...")
        print("--------------------------------")
        # for info in vehicles:
        #     print(info)

    except Exception as e:
        print("Error getting vehicle details: " + str(e))

    # return save_vehicle_info(vehicles)


def get_vehicle_details1():
    """
    Get vehicle details from https://autocj.co.jp/
    :return: list of vehicle details
    """
    vehicle_company2 = []
    #  company ID for auto cj   is 1
    company = Company.objects.filter(pk=3).first()
    try:
        vehicle = {}
        print("Getting vehicle details...")
        url = "https://autocj.co.jp/used_cars?maker=6"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="xml")
        vehicle_details = soup.find_all("li", {'class': 'l-vblock'})
        for vehicle_detail in vehicle_details:
            vehicle_yom_models = vehicle_detail.find('div', {"class": 'v-detail'}).find("h2")
            vehicle_more_details = vehicle_detail.find_all("table", {'class': 'v-table'})
            vehicle_price = vehicle_detail.find("div", {'class': 'v-price'}).find('div').text
            price = vehicle_price.split(' ')[2:][1]
            vehicle_image = vehicle_detail.find("div", {'class': 'v-img'}).find('a').find('img')['src']
            image = f'https://autocj.co.jp{vehicle_image}'
            vehicle['price'] = price
            vehicle['image'] = image
            for vehicle_more_detail in vehicle_more_details:
                more_details_trs = vehicle_more_detail.find("tbody").find_all('tr')
                more_details = more_details_trs[1].find_all('td')
                more_details_info = [i.text for i in more_details]
                millage = more_details_info[6]
                more_info = more_details_info[1]
                vehicle['millage'] = millage
                vehicle['more_info'] = more_info

            yom_models = vehicle_yom_models.find_all("a", href=True)
            yom_model = ''.join([i.text for i in yom_models])
            # print(yom_model)
            YOM = yom_model.split(' ')[0]
            make = yom_model.split(' ')[1]
            name = ' '.join([str(elem) for elem in yom_model.split(' ')[2:]])

            vehicle['name'] = name
            vehicle['YOM'] = YOM
            vehicle['make'] = make
            vehicle['company'] = company
            # print(f' YOM: {YOM} make: {make} name: {name} millage: {millage} price: {price}')

            vehicle_save = Vehicle(name=name, YOM=YOM, image=image,
                                   price=price, make=make,
                                   millage=millage,
                                   more_info=more_info, company=company)

            vehicle_save.save()

        print("Finished getting vehicle news...")
        print("--------------------------------")

        # for info in vehicle_company2:
        #     print(info)

    except Exception as e:
        print("Error getting vehicle details: " + str(e))

    # return save_vehicle_info(vehicle_company2)


def save_vehicle_info(vehicles):
    """
    save vehicle information to the database
    """
    print(" Start saving vehicle information to the database...")
    for vehicle in vehicles:
        try:
            Vehicle.objects.create(
                name=vehicle['name'],
                YOM=vehicle['YOM'],
                image=vehicle['image'],
                price=vehicle['price'],
                make=vehicle['make'],
                millage=vehicle['millage'],
                more_info=vehicle['more_info'],
                company=vehicle['company'],
            )
        except Exception as e:
            print(f'Failed to saving vehicle information to the database..."): {e}')
            break
    return print(" Finishing saving vehicle information to the database...")
