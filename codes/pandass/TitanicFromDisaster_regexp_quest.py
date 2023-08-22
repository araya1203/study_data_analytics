# - Name 변수에서 성씨, 결혼유무 가져오기
# - hint : 성씨 컬럼에 Nan 없어야 함.


import pandas as pd

file_path = 'C:/Users/04-02/Develops/study_data_analytics/datasets/TitanicFromDisaster_train.csv'

# CSV 파일을 DataFrame으로 읽어옵니다.
df = pd.read_csv(file_path)


# 성씨 추출 함수
def extract_last_name(name):
    return name[0]

# 결혼 여부 추출 함수
def extract_marital_status(cancellation):
    return "결혼" if cancellation == "없음" else "미혼"

# 'Name' 열에서 성씨와 결혼 여부를 추출하여 새로운 열로 추가합니다.
df['성씨'] = df['bank'].apply(extract_last_name)
df['결혼유무'] = df['cancellation'].apply(extract_marital_status)

# 결과 출력
print(df[['성씨', '결혼유무']])