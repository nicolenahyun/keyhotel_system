# 라이브러리 불러오기
import pandas as pd
import numpy as np
# 텍스트 전처리
import re
# 경고
import warnings
warnings.filterwarnings("ignore")
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


# 파일 임포트
df_2 = pd.read_csv('review_dataset/reveiw_list2.csv', encoding='utf8', index_col=0)

# 특수 문자 제거
def cleanText(text):
    text = re.sub('[^A-Za-z0-9가-힣]', ' ', str(text))
    return text

# DataFrame의 각각 요소에 함수 일괄 적용하기 : applymap(Function name)
df_2 = df_2.applymap(cleanText);

# 키워드 추출
ids = list(df_2.columns)
reviews = [" ".join(list(df_2[i].astype(str))) for i in ids]
    
organized_df = pd.DataFrame(columns=["id", "review"])

for i in range(len(ids)):
    organized_df = organized_df.append(
        {"id": ids[i], "review": reviews[i]}, ignore_index=True
    )

organized_df.head()

# review 컬럼만 리스트로 저장
text=''
reviews=[]
for each_review in organized_df['review']:
    reviews.append(each_review)


# 키워드 길이 지정
n_gram_range = (1, 1)

# 리뷰하나씩 키워드로 분리(count-vectorizer)
a= len(reviews) # 불용어 제거한 리뷰

token_review_list=[]

for i in range(0,a): # 리뷰하나당 처리하기위해 for문 
    review_vectorized = CountVectorizer(ngram_range=n_gram_range).fit([reviews[i]])
    token_review = review_vectorized.get_feature_names()
    
    token_review_list.append(token_review) # 하나의 리스트를 만들어서 df에 추가해야함.
organized_df['review_keyword']=token_review_list # 토큰 단위로 나누어진 리뷰저장

organized_df.head(10)

# 임베딩
# 키워드 임베딩 모델 생성
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# 키워드 임베딩
review_embedded_list = []
count_embedded_list = []

for i in range(0, a):
  embedding_review = model.encode([reviews[i]])
  review_embedded_list.append(embedding_review)

for i in organized_df['review_keyword']:
  embedding_count = model.encode(i)
  count_embedded_list.append(embedding_count)

# 코사인 유사성
top_n = 5

a = len(review_embedded_list)
distances = []
keywords = []

for i in range(0,a):
  distance = cosine_similarity(review_embedded_list[i], count_embedded_list[i])
  keyword = [organized_df['review_keyword'][i][index] for index in distance.argsort()[0][-top_n:]]

  distances.append(distance)
  keywords.append(keyword)

  distances[0].argsort()
  distances[0].argsort()[0][-top_n:]
  keywords[0]

  organized_df['keyword'] = keywords

  organized_df.to_csv("review2.csv")