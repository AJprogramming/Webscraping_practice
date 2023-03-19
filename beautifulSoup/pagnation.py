# pagnation will allows to scrape from different pages

from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
pract_website = f'{root}/movies_letter-A'
result = requests.get(pract_website)
content = result.text

soup= BeautifulSoup(content, 'lxml')
# print(soup.prettify())

pagination = soup.find('ul', class_="pagination")
pages = pagination.find_all('li', class_="page-item")
# for this given example site we want the only the page numbers not the arrows so we must do this below
last_page = pages[-2].text

# I need to add 1 to the int(last_page) or else it'll give me one last page than what I asked for
links = []

for page in range(1, int(last_page)+1)[:2]:
    result = requests.get(f'{pract_website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')


    for i in box.find_all('a', href=True):
        links.append(i['href'])

    for i in links:
        try:
            result=requests.get(f'{root}/{i}')
            content=result.text
            soup= BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article')
            title=box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=" ")
            
            with open(f'{title}.txt', 'w', encoding='utf=8') as file:
                file.write(transcript)
        except:
            print("-------Link isn't working---------")
            print(i)
