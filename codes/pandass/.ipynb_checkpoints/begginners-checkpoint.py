import pandas as pd

double_list =[
    [1000, '과자','2019-12-31','반품'],
    [2000, '음료', '2020-03-02', '정상'],
    [3000, '아이스크림', '2020-02-03','정상'],
    [1000,'과자','2019-12-31','반품']
    ]
double_list_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(double_list, columns=double_list_columns)
print(df_saledays)

#단일변수 처리 with apply()
def mean_subtraction(cell_value) :
    result = 1750 - cell_value
    return result

mean_subtraction(750)

df_saledays['가격'].apply(mean_subtraction) #각 cell당 평균 차이값

# 다변수 처리  with apply()
def calculate_sum(row):
    result = row['가격'] * 20
    return result

df_saledays['가격합'] = df_saledays.apply(calculate_sum, axis='columns')
print(df_saledays)


# regexpress(정규식)
data = {'Names' : ['김지수','박지민','이태용','최수영']}

df_Name = pd.DataFrame(data)


# print(df_Name)

# pandas 패키지
pattern = r'^([가-힣]{1})'

# df_Name['Names'].str.extract(pattern)

# 'Last_Name' 열 생성 및 성만 추출하여 할당
df_Name['Last_Name'] = df_Name['Names'].str.extract(pattern)

# 'Last_Name' 열만 출력
print(df_Name['Last_Name'])  

# print(df_Name)