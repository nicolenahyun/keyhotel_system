import pandas as pd

df_info = pd.read_csv('info_dataset/info.xlsx', encoding='utf8', index_col=0, errors='ignore')
df_0 = pd.read_csv('review_dataset/reveiw0.csv', encoding='utf8', index_col=0, errors='ignore')
df_1 = pd.read_csv('review_dataset/reveiw1.csv', encoding='utf8', index_col=0, errors='ignore')
df_2 = pd.read_csv('review_dataset/reveiw2.csv', encoding='utf8', index_col=0, errors='ignore')
df_3 = pd.read_csv('review_dataset/reveiw3.csv', encoding='utf8', index_col=0, errors='ignore')
df_4 = pd.read_csv('review_dataset/reveiw4.csv', encoding='utf8', index_col=0, errors='ignore')
df_5 = pd.read_csv('review_dataset/reveiw5.csv', encoding='utf8', index_col=0, errors='ignore')
df_6 = pd.read_csv('review_dataset/reveiw6.csv', encoding='utf8', index_col=0, errors='ignore')
df_7 = pd.read_csv('review_dataset/reveiw7.csv', encoding='utf8', index_col=0, errors='ignore'
df_8 = pd.read_csv('review_dataset/reveiw8.csv', encoding='utf8', index_col=0, errors='ignore')

df_0.head()