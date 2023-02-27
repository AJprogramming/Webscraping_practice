from bs4 import BeautifulSoup
import requests

pract_website="https://subslikescript.com/movie/Titanic-120338"
result=requests.get(pract_website)
content=result.text

soup= BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box=soup.find('article', class_='main-article')


# We can put 'soup', but if we but 'box' instead it'll now we only want content within that area of our search
title=box.find('h1').get_text()
# print(title)


#to put the information in a data frame we need to add 'strip' and 'seperator' in the get_text 
transcript=box.find('div', class_='full-script').get_text(strip=True, separator=" ")
print(title)
print(transcript)

with open(f'{title}.txt', 'w', encoding='utf=8') as file:
    file.write(transcript)