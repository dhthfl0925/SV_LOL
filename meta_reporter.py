from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup
import openpyxl




# 새로운 워크북 만들기
wb = openpyxl.Workbook()
# 현재 시트 선택
sheet = wb.active
# 헤더 추가하기
sheet.append(['observ_num',"vic", "line", "kill", "death",'assist'])



#step2.검색할 키워드 입력
# query = input('검색할 키워드를 입력하세요: ')
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
#step3.크롬드라이버로 원하는 url로 접속

# driver = webdriver.Edge(r'C:\Users\drone\Desktop\webdriver\msedgedriver')
driver = webdriver.Chrome(r'C:\Users\drone\Desktop\webdriver\chromedriver', chrome_options=options)
user_name_list = ['만기퇴소 최성원','정형우','무감점딜링머신','민 졈','생각좀하고 해줘','티모와잭스','이현웅','품 젊','권민수데기장군']
observ_num = 0
for user_name in user_name_list :
    url = f'https://www.op.gg/summoners/kr/{user_name}'
    driver.get(url)
    # time.sleep(3)


    #step5.뉴스 탭 클릭
    try:
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div[2]/div[1]/ul/li[2]/button').click()
        
        time.sleep(1)
        for z in range(1,21):
            driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{z}]/div/div[2]/button').click()
            time.sleep(1)
            for a in range(1,3):
                match_result = driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{z}]/div[2]/div[1]/table[{a}]/thead/tr/th[1]/span').text
                print('\n',match_result)
                for b in range(1,6):
                    match_history_kda = driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{z}]/div[2]/div[1]/table[{a}]/tbody/tr[{b}]/td[6]/div[1]').text
                    print(match_history_kda, end=' ')
                    observ_num += 1
                    if match_result == '승리':
                        vic = 1
                    else:
                        vic = 0
                    
                    # line = b
                    if b == 1:
                        line = 'top'
                    elif b == 2:
                        line = 'jg'
                    elif b == 3:
                        line = 'mid'
                    elif b == 4:
                        line = 'adc'
                    elif b == 5:
                        line = 'sup'

                    match_history_kda = match_history_kda.split('/')
                    kill = int(match_history_kda[0])
                    death = int(match_history_kda[1])
                    assist = int(match_history_kda[2].split('(')[0])

                    sheet.append([observ_num,vic,line,kill,death,assist])
    except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('예외가 발생했습니다.', e)
        pass
        # time.sleep(100)


# observation number/ 승패 / 라인 / k / d / a 



wb.save("sv_lol.xlsx")



# # click button
# /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div/div[2]/button
#      match_result
    # /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[1]/thead/tr/th[1]/span
    # /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[2]/thead/tr/th[1]/span
#     # my team
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[1]/tbody/tr[1]/td[6]/div[1]
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[1]/tbody/tr[2]/td[6]/div[1]
#     ...
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[1]/tbody/tr[5]/td[6]/div[1]
#     # enemy
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[2]/tbody/tr[1]/td[6]/div[1]
#     ...
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div[2]/div[1]/table[2]/tbody/tr[5]/td[6]/div[1]



# /html/body/div[1]/div[5]/div[2]/div[3]/li[2]/div/div[2]/button
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[2]/div[2]/div[1]/table[1]/tbody/tr[1]/td[6]/div[1]
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[2]/div[2]/div[1]/table[1]/tbody/tr[2]/td[6]/div[1]
#     ...
#     /html/body/div[1]/div[5]/div[2]/div[3]/li[2]/div[2]/div[1]/table[2]/tbody/tr[5]/td[6]/div[1]
# /html/body/div[1]/div[5]/div[2]/div[3]/li[3]/div/div[2]/button
# /html/body/div[1]/div[5]/div[2]/div[3]/li[4]/div/div[2]/button
# ...
# /html/body/div[1]/div[5]/div[2]/div[3]/li[20]/div/div[2]/button

# /html/body/div[1]/div[5]/div[2]/div[3]/li[1]/div/div[2]/button

# real
# /html/body/div[1]/div[6]/div[2]/div[3]/li[1]/div/div[2]/button