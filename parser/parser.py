import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.krsu.edu.kg/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='news-column-block')
    movies = []

    for item in items:
        movies.append(
            {
                'link': URL + item.find('a').get('href'),
                'title': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_='views-field views-field-field-data-publikacii').find('div').get_text(),
                'image': URL + item.find('div', class_='field-content news-img').find('img').get('src')
            }
        )
    return movies


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        movies1 = []

        for page in range(0, 1):
            html = get_htm


            l(f'https://www.krsu.edu.kg/', params=page)
            movies1.extend(get_data(html.text))
        return movies1
    else:
        raise Exception('Error in parser func........')
