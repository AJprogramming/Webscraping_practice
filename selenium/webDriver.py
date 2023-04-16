from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.audible.com/search"
path = r'C:\Users\artea\Downloads\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

allMatchesButton = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
allMatchesButton.click()


dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)


matches = driver.find_elements_by_tag_name('tr')

date = []
homeTeam = []
score = []
awayTeam = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    homeTeam.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    awayTeam.append(match.find_element_by_xpath('./td[4]').text)


df = pd.DataFrame({
    'date' : date,
    'homeTeam' : homeTeam,
    'score' : score,
    'awayTeam' : awayTeam
})

df.to_csv('footballData.csv', index=False)
print(df)
driver.quit()