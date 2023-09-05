# - Name 변수에서 성씨, 결혼유무 가져오기
# - hint : 성씨 컬럼에 Nan 없어야 함.

import pandas as pd
import re

df_TT = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_TT


data = df_TT['Name']
df_TT_name = pd.DataFrame(data)
print(df_TT_name)


pattern = r'^([A-Za-z]+)'
df_TT_name['Last name'] = df_TT_name['Name'].str.extract(pattern)
print(df_TT_name)


pattern = r'\bMrs\b'
df_TT_name['marry'] = df_TT_name['Name'].str.extract(pattern)
df_TT_name =df_TT_name.dropna()
print(df_TT_name)

# # 이름에서 성을 추출하는 함수
# def extract_last_name(name):
#     # 패턴을 사용하여 성을 추출
#     match = re.search(r'^([^,]+),', name)
#     if match:
#         return match.group(1).strip()  # 성 요소 반환 (앞뒤 공백 제거)
#     else:
#         return ""  # 패턴에 맞는 부분이 없는 경우 빈 문자열 반환

# 'Last Name' 열 생성
# df_TTD['Last Name'] = df_TTD['Name'].apply(extract_last_name)
# print(df_TTD['Last Name'])


# # 이름에서 결혼 여부를 추출하는 함수
# def extract_marital_status(name):
#     if re.search(r'\bMrs\b', name):
#         return '결혼'
#     elif re.search(r'\bMr\b', name):
#         return '미혼'
#     else:
#         return ''  # "Mr"나 "Mrs"가 없는 경우

# # 'Marital Status' 열 생성
# df_TTD['Marital Status'] = df_TTD['Name'].apply(extract_marital_status)

# # 결과 출력
# print(df_TTD[['Name', 'Marital Status']])
