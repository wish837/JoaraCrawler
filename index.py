from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import json

ID = json.load(open('config.json', 'r'))['ID']
PW = json.load(open('config.json', 'r'))['PW']

print('***********[조아라 다운로더]***********')
NOVEL_BEGIN = input('다운로드할 소설 첫 화의 URL을 입력해주세요\n: ') 
NOVEL_END = int(input('다운로드할 소설의 마지막 화수를 입력해주세요\n: '))
NOVEL_NAME = input('저장할 텍스트 파일 제목을 입력해주세요\n: ')

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.joara.com/login')
time.sleep(random.uniform(1, 4))
driver.find_element_by_name('userId').send_keys(ID)
time.sleep(random.uniform(1, 4))
driver.find_element_by_name('passwd').send_keys(PW)
time.sleep(random.uniform(1, 4))
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()
time.sleep(random.uniform(1, 4))

NOVEL_PAGE = 0

while NOVEL_PAGE < NOVEL_END:
    driver.get(NOVEL_BEGIN)
    time.sleep(random.uniform(1, 4))

    NOVEL_PAGE += 1

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    f = open(f'{NOVEL_NAME}.txt', 'a', encoding='UTF8')
    for i in soup.select('.text-wrap'):
        f.write(i.get_text())

    time.sleep(random.uniform(15, 25))

    if NOVEL_PAGE == 1:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/a[2]').click()
        time.sleep(random.uniform(1, 3))
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[2]/div').click()
        time.sleep(random.uniform(1, 3))
        driver.find_element_by_xpath('//*[@id="react-confirm-alert"]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.uniform(1, 3))
    else:
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[2]/div').click()
        time.sleep(random.uniform(1, 3))
        driver.find_element_by_xpath('//*[@id="react-confirm-alert"]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.uniform(1, 3))
        
print('***********[다운로드가 완료되었습니다!]***********')