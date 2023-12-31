
## 묘사 데이터 분석(DDA, Descriptive Data Analysis)
데이터 기본정보 파악 : 데이터 구조 및 특성 확인
분석 계획 수립 : 분석 목적. 과제 정의, 목표 변수 및 설명변수 정의
데이터 전처리 : 결측치, 이상치 등 처리


## RecurrenceOfSurgery_Doctors_DDA

- 분석 제공 대상: 의사
- 목표 변수 : '수술시간'

| 변수명         | 변수설명                        | 데이터 분류                      |  분석가 의견                    | 
|--------------|---------------------------------------------|-------------------------------|-------------------------------| 
| 간질성폐질환 | 환자의 폐에 대한 간질성 질환 여부   | 범주형-명목형(0,1)          | 여부만을 나타내는 데이터                | 
| 심혈관질환   | 환자의 심혈관 질환 여부            | 범주형-명목형 (0,1)          | 여부만을 나타내는 데이터                   | 
| 연령         | 환자의 나이                       | 수치형-연속형 (39,40,42..)| 연령은 소수점 단위로 변화할 수 있는 데이터 | 
| 과거수술횟수 | 환자의 과거 수술 횟수              | 수치형-이산형 (0,1,2)        |  정수 데이터값을 가지는 데이터   | 
| 수술기법     | 사용된 수술 기법                  | 범주형-명목형 (TELD) | 분류를 목적으로 하는 데이터  | 
|수술시간 | 환자의 수술 시간 | 수치형-이산형| 	정수 데이터값을 가지는 데이터     | 
