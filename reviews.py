from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

import method       # method.py가 같은 폴더에 있어야 됩니당

## 여기 이전에 했던 거처럼 0~8번 자동으로 넣어주게 해도 좋아요. 이거는 숫자 일일이 넣어야 됩니다.
num = int(input('input number : '))

# url csv 파일 읽어오는 부분
url_list = pd.read_csv('hotel_review_list.csv', index_col = 0)

# 각 컬럼의 길이 구하기
numofhotel = url_list.iloc[:,num].notnull().sum()

# 내보낼 df 생성 (row : 리뷰, col : ID)
# ID : 호텔 url 맨 뒤 숫자부분
df = method.make_df(url_list, num)

# 입력된 column 의 url을 훑으며 크롤링 시작
for idx in range(numofhotel) :

    # 진행상황 출력
    print('-'*60)
    print(f'read page {idx}/{numofhotel}')

    # '/reviews' 를 붙여 url 완성
    url = url_list.iloc[idx,num] + '/reviews' 
    print(f'url : {url}') 

    # chromedriver 옵션 설정
    options = Options()
    user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
    options.add_argument('user-agent=' + user_agent)    # 유저의 접속인 것처럼 속이기 
    options.add_argument("headless")        # 창 띄우고 싶으면 주석처리.    

    # chromedriver 실행 후 url 정보 받기
    driver = webdriver.Chrome(options=options, executable_path='chromedriver')
    driver.get(url = url)

    # 스크롤 맨 밑까지 내리는 작업
    print('스크롤 내리는 중')
    while True :
        print('.',end='')
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
        time.sleep(2)        ## 스크롤 내리는 로딩시간이 길면 숫자 좀 늘려주세요!

        new_height = driver.execute_script("return document.body.scrollHeight")        

        if new_height == last_height :
            break        
    print('')

    # 크롤링 시작
    print('start crawling...')
    src = driver.page_source    # 소스를 가져와서 리뷰 데이터 긁어올 것임    
    
    # 데이터프레임에 크롤링 정보 저장
    df = method.get_reviews(src, df, idx) # method 파일 참조하여 리뷰 수집
    print('done!')

    ## tmp
    if idx % 10 == 1 :
        df.to_csv(f'./reveiw_list{num}.csv', encoding="utf-8-sig")    
        print('tmp saved')    

# 모든 작업 종료 후 파일 내보내기
df.to_csv(f'./reveiw_list{num}.csv', encoding="utf-8-sig")
print('Complete!!')

