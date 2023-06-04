import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://broadway.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="releases-item")
    broadway_film = []

    for item in items:
        broadway_film.append(
            {
                "title_url": URL + item.find("a").get("href"),
                "title_text": item.find("div", class_="releases-item__info").get_text(),
                "image": URL
                + item.find("div", class_="releases-item__poster gradient_1").find("img").get("src"),
            }
        )

    return broadway_film


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        broadway_film1 = []
        for page in range(0, 1):
            html = get_html(f"https://broadway.kg/", params=page)
            broadway_film1.extend(get_data(html.text))
        return broadway_film1
        # print(f'\n{manas_film1}\n')
    else:
        raise Exception("Parse Error......")


# parser()
