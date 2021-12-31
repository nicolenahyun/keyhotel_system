from bs4 import BeautifulSoup
import pandas as pd

## hotel_review_list.csv 를 읽어와서 데이터프레임을 만드는 함수
def make_df(url_list, num) :

    columns = url_list.iloc[:,num].dropna()
    
    for idx,column in enumerate(columns) :
        columns[idx] = column.split('/')[-1] # url의 고유 ID 가져오기

        df = pd.DataFrame(columns=columns)

    return df

## 소스를 받으면 리뷰 내용들을 찾아서 하나의 문자열로 합친 후 반환하는 함수
def get_reviews(src, df, col) : # src : 소스 , df : 저장될 데이터 프레임, col : 호텔 ID 컬럼
    # print(df)
    col_name = df.columns[col]
    idx = 0
    soup = BeautifulSoup(src, 'lxml')

    review_list_short = soup.find_all('p',attrs={"class":"content"})        # 짧은 리뷰 리스트
    review_list_long = soup.find_all('p',attrs={"class":"content clamp"})   # 더보기 리뷰 리스트

    # 리뷰를 df에 저장 
    print('짧은 리뷰 저장 중')
    for i in range(len(review_list_short)) :     
        df.loc[idx, col_name] = review_list_short[i].get_text()
        idx += 1
        # print('.',end='')

    print('\n긴 리뷰 저장 중')
    for i in range(len(review_list_long)) :
        df.loc[idx, col_name] = review_list_long[i].get_text()   
        idx += 1
        # print('.',end='')

    return df
