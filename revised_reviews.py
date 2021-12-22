import pandas as pd
import numpy as np

num = 0
for num in range(9) :

    raw_df = pd.read_csv(f'review_dataset/reveiw_list{num}.csv',index_col=0)
    new_df = pd.DataFrame(columns=['hotel','star','review'])

    ids = raw_df.columns
    for id in ids :    
        reviews = raw_df.loc[:,id]

        for review in reviews :
            if pd.isnull(review) :
                break

            new_df.loc[len(new_df), 'hotel'] = id
            new_df.loc[len(new_df) - 1, 'review'] = review
            
        print(f'{num}번 파일 id : {id} done!')

    new_df.to_csv(f'./revised_review{num}.csv', encoding="utf-8-sig")
    print(f'reveiw_list{num}.csv DONE!' )
    print('='*50)

