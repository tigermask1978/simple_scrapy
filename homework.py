from bs4 import BeautifulSoup

with open('./index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div.container > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select('body > div.container > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div.container > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    rate_nums = Soup.select('body > div.container > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    rate_stars = Soup.select('body > div.container > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2) ')




info = []
for image, title, price, rate_num, rate_star in zip(images, titles, prices, rate_nums, rate_stars):
    data = {
        'image': image.get('src'),
        'title': title.get_text(),
        'price': price.get_text(),
        'rate_num': rate_num.get_text(),
        'rate_stars': len(rate_star.find_all('span', class_='glyphicon glyphicon-star'))
    }
    info.append(data)
    print data , '\n'
