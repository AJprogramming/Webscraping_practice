from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
pract_website = f'{root}/movies'
result=requests.get(pract_website)
content=result.text

soup= BeautifulSoup(content, 'lxml')
# print(soup.prettify())

soup.find('article', class_= "main-article")

box = soup.find('article', class_='main-article')
# find_all gives us a list

links = []

for i in box.find_all('a', href=True):
    links.append(i['href'])

print(links)

for i in links:
    pract_website = f'{root}/{i}'
    result=requests.get(pract_website)
    content=result.text
    soup= BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_='main-article')
    
    title=box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=" ")
    
    with open(f'{title}.txt', 'w', encoding='utf=8') as file:
        file.write(transcript)
        



# # print(title)


# #to put the information in a data frame we need to add 'strip' and 'seperator' in the get_text 
# transcript = box.find('div', class_='full-script').get_text(strip=True, separator=" ")
# print(title)
# print(transcript)

# with open(f'{title}.txt', 'w', encoding='utf=8') as file:
#     file.write(transcript)
# # We can put 'soup', but if we but 'box' instead it'll now we only want content within that area of our search
# title=box.find('h1').get_text()
# # print(title)


# # #to put the information in a data frame we need to add 'strip' and 'seperator' in the get_text 
# # transcript=box.find('div', class_='full-script').get_text(strip=True, separator=" ")
# # print(title)
# # print(transcript)

# with open(f'{title}.txt', 'w', encoding='utf=8') as file:
#     file.write(transcript)