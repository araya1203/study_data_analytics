<details >
<summary>Titanic From Disater_타이타닉 참사 DDA</summary>
from dataset : https://www.kaggle.com/competitions/titanic/data

### DDA 분석
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | ---|
|PassengerId| 유니크id | | unique id의 경우 데이터로 사용 불가 판단 | 
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 생존과 죽음의 두가지 종류이기 때문에 범주형으로 판단됨|
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형), 등급이 부여된 티켓이기 때문에 범주형으로 판단됨 |
| sex | Sex | | 범주형(명목형) |
| Age | Age in years | | 수치형(이산형) | 
| sibsp | # of siblings / spouses aboard the Titanic | | 범주형(순서형), 형제자매의 특정 수치이며 범주별 빈도를 분석해야 함  |
| parch | # of parents / children aboard the Titanic | |범주형(순서형), 범주형으로 빈도를 파악해야 함 |
| ticket | Ticket number | | 범주형(순서형) |
| fare | Passenger fare | | 수치형(이산형), 각 요금별 승객의 수를 파악하는데 사용할 수 있음 |
| cabin | Cabin number | | 범주형(순서형)|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(명목형) |


</details>


<details >
<summary>Type Of Contract Channel_계약 유형 채널 DDA</summary>
from dataset : https://blog.naver.com/data_station/222493245799

### DDA 분석
| Variable |Definition | Key | 데이터 분류   | 분석가 의견 |
|---|---|---|---|---|
| id | 각 레코드의 고유 식별자 |  | 범주형(명목형)  | unique id의 경우 데이터로 사용 불가 판단  |
| type_of_contract  | 계약 유형    | 렌탈, 멤버십 | 범주형(명목형) | 각 계약 유형사이의 순서의 정보가 없음으로 명목형 |
| type_of_contract2 | 다른 유형의 계약 |       |범주형(명목형) | 명확한 순서가 나타나있지 않기때문에 명목형|
| channel  | 계약을 획득한 경로  |       |범주형(명목형)| 서로 비교할 수 없는 의미적인 관계이기에 명목형|
| datetime          | 레코드의 날짜와 시간  |       | 수치형(연속형)| 날짜이기 때문에 연속형으로 판단됨 |
| Term              | 계약 기간 (달)   |       |수치형(연속형) |  |
| payment_type      | 지불 방식   |       | 범주형(명목형) |  |
| product           | 계약과 관련된 제품   | K1 ~ k6 |범주형(명목형)| 각 제품 유형은 서로 다른 범주로 분류, 서로 비교 할 수 없는 의미적 관계  |
| amount            | 계약과 관련된 금액  |       | 수치형(이산형) |   |
| state             | 계약의 주 또는 지역  |       |범주형(명목형) |   |
| overdue_count     | 계약이 연체된 횟수  |       | 수치형(이산형)| 연체된 횟수를 파악해야 함|
| overdue           | 현재 계약이 연체 중인지 여부 |  있음, 없음     | 범주형(명목형)|  연체 여부의 유무만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음|
| credit rating     | 고객의 신용 등급  | 1.0 ~ 10.0      |범주형(명목형)| 데이터 확인결과 연산이 가능한 의미적인 순서가 아니기에 순서가 의미 없는 명목형 데이터|
| bank              | 계약과 연관된 은행 |       | 범주형(명목형)|   |
| cancellation      | 계약이 취소되었는지 여부  | 정상, 해약 | 범주형(명목형)| 취소 여부만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음 |
| age               | 고객의 나이  |       | 수치형(이산형) |   |
| Mileage           | 계약과 연관된 주행 거리  |       | 수치형(연속형)| 주행거리는 연속적인 데이터를 갖음|


</details>

# Data analytics

## 📚 STACKS
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/> <img
src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"/> <img
src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/> <img
src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/> <img 
src="https://img.shields.io/badge/Jupyter Notebook-F37626?style=for-the-badge&logo=Jupyter Notebook&logoColor=white"/><img
src="https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=Anaconda&logoColor=white"/> <img 
src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"/> <img 
src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/> <img 
src="https://img.shields.io/badge/Google Cloud-4285F4?style=for-the-badge&logo=Google Cloud&logoColor=white"/>

##  시각화(visuallizations)
- 데이터 시각화는 데이터 분석 결과를 시각적으로 명확하게 표현하고 의사소통 하는 것

<details >
<summary> 시각화 라이브러리 </summary>
<br> 
- pandas : 데이터 분석과 데이터 조작을 위한 파이썬 라이브러리
- matplotlib : 파이썬의 데이터 시각화 및 그래프 작성 라이브러리
       matplotlib.pyplot: Matplotlib의 서브 모듈, 서브 모듈은 Matplotlib를 사용하여 그래프를 생성하고 다양한 그래픽 요소를 조작하는 데 유용한 함수와 기능을 제공 
- seaborn : 파이썬의 데이터 시각화 라이브러리 중 하나이고 Matplotlib에 기반하며, 데이터 시각화를 보다 쉽고 아름답게 수행할 수 있도록 도와주는 고수준 인터페이스를 제공
</details>

| 제목 | 작성소스 | 설명 |  비고|
|---|---|---|---|
| 기본 시각화 | [simples](./codes/visuallizations/simples.ipynb) | matplotlib.pyplot Scatter Plot | 
| scatterplot | [classfications_scatter](./codes/visuallizations/classfications_scatter.ipynb) | scatterplot 두 클래스 변수를 한 plot에 표현 (title, label, legend), plot(데이터 포인트를 선으로 연결)| 
| UsingCharts | [UsingCharts](./codes/visuallizations/UsingChart_TypeOfContractChannel.ipynb) | 목표변수와 설명변수의 관계를 시각화 | 


## Pandas
- 데이터 분석과 데이터 조작을 위한 파이썬 라이브러리

<details >
<summary> pandas 라이브러리에서 DataFrame 또는 Series 객체의 정보 확인하는 메서드 </summary>

#### 데이터 정보 확인
- .head() :  DataFrame 또는 Series의 처음 몇 개의 행을 확인함, .head(n) 형식으로 호출하여 원하는 행의 수를 지정
- .tail() :  DataFrame 또는 Series의 마지막 몇 개의 행을 확인함, .tail(n) 형식으로 호출하여 원하는 행의 수를 지정
- .info() : 기본 정보를 표시하는 메서드, 데이터프레임의 크기, 열(컬럼)의 데이터 유형, 결측치 유무 및 메모리 사용량과 같은 정보를 요약함.
- .describe() : 통계적 요약 정보를 표시하는 메서드, 주요 통계량, 평균, 중위수, 표준 편차, 최솟값, 최댓값 등을 요약하여 제공함.
- .describe(include='object') : 통계적 요약 정보를 문자열(문자형) 데이터 열(컬럼)에 대해서만 표시하는 메서드
          count: 비어 있지 않은 값의 개수
          unique: 고유한 값의 개수
          top: 가장 자주 나타나는 값
          freq: 가장 자주 나타나는 값의 빈도를 보여줌.
- .value_counts() : 고유한 값의 빈도를 계산하여 반환하는 메서드, 범주형 데이터의 빈도를 계산하거나, 어떤 열(컬럼)의 고유한 값이 어떻게 분포하는지를 이해하는 데 사용함.
- .shape :  DataFrame의 행 및 열 수를 확인하고 (행 수, 열 수)의 형식으로 반환함. 2차원 데이터 구조
- .columns : DataFrame의 열 이름을 확인하하고 열 이름을 리스트로 반환함.
- .index: DataFrame의 행 인덱스를 확인하고 행 인덱스 정보를 반환함.
- .unique(): Series 객체에서 고유한 값을 확인하고 주로 범주형 데이터의 고유한 값 목록을 가져올 때 사용함.

#### TimeSeries
- .to_datetime() : 날짜와 시간 정보를 포함하는 데이터를 Pandas의 datetime 객체로 변환하는 데 사용함. 
- .dt.year: datetime 열에서 연도(Year)를 추출
- .dt.month: datetime 열에서 월(Month)을 추출
- .dt.day: datetime 열에서 일(Day)을 추출
- .dt.hour: datetime 열에서 시간(Hour)을 추출
- .dt.weekday: datetime 열에서 요일(Weekday)을 추출 (0은 월요일, 6은 일요일)

#### 데이터 형(type) 변환
- .astype(str) : DataFrame 또는 Series의 데이터 유형을 문자열(string)로 변환하는 데 사용

#### 연산(Operation)
- .apply() : 함수를 적용하여 DataFrame 또는 Series의 각 요소에 대해 연산을 수행하는 데 사용
</details>

| 제목 | 작성소스 | 설명 |  비고|
|---|---|---|---|
| 데이터 정보 확인_1 | [데이터 정보 확인_1](./codes/pandass/BreastCancerWiscon.ipynb) | DataFrame 형태 확인, 기본 정보, 통계정 요약 정보 (수치형, 문자형))  |.shape .info() .describe() .describe(include=object) |
| 데이터 정보 확인_2 | [데이터 정보 확인_2](./codes/pandass/TitanicFromDisaster.ipynb) | 행 확인 , 고유한 값 확인 | .head(n) .tail().unique() |
| TimeSeries | [TimeSeries](./codes/pandass/DeliveryList_TimeSeries.ipynb) | 날짜와 시간 데이터 다루기|.to_datetime() |
| RecurrenceOfSurgery | [RecurrenceOfSurgery](./codes/pandass/RecurrenceOfSurgery_Timeseries_with.ipynb) |주차별/요일별 입원/퇴원 추이 시각화| 데이터타입, 시각화 종류 파악|
| apply | [apply](./codes/pandass/ResurrenceOfSurgery_apply_quest.ipynb) |체중,신장의 데이터를 활용하여 BMI 시각화| .apply()|
| preprocess | [preprocess](./codes/pandass/preprocess.ipynb) |전처리를 통해 결측치, 이상치 제거|
| merge | [merge](./codes/pandass/merge.ipynb) | 데이터를 조인하여 병합하는 법|


## Sellenium
- 웹 브라우저를 이용하는 자동화 프로그램인 'Selenium'을 이용하여 크롤링 하기
  
| 제목 | 작성소스 | 설명 |
|---|---|---|
| 기본 정보 | [begginers](./codes/gatheringdatas/seleniums/begginers.ipynb) | 웹페이지 창 닫고 열기, screenshot| |
| find| [find](./codes/gatheringdatas/seleniums/emartmalls_find.ipynb) | find, bundle lish  with for문 | find_elements_by_css_selector|
| Login| [Login](./codes/gatheringdatas/seleniums/github_events_except.ipynb) | 로그인 기능 구현  | |
| pagination| [pagination](./codes/gatheringdatas/seleniums/emartmalls_paginations.ipynb) | pagination 구현  | |
| 앱 리뷰(single) | [googlestore_healthcare](./codes/gatheringdatas/seleniums/googlestore_heathcare_single.ipynb) | single  | |
| 앱 리뷰(loops) | [loops](./codes/gatheringdatas/seleniums/googlestore_heathcare_loops.ipynb) | loops  | |
| 앱 리뷰 스크롤링| [loops_complete](./codes/gatheringdatas/seleniums/googlestore_heathcare_loops_complete.ipynb) | loops with for 문 | 각 제품(앱)에 들어가서 리뷰를 스크롤링 |
| pagedown| [pagedown](./codes/gatheringdatas/seleniums/begginers_pagedown.ipynb) | 마우스 스크롤 pagedown 기능 구현 |  |
| 스크롤링| [pagedown_스크롤링](./codes/gatheringdatas/seleniums/begginers_ready.ipynb) | 마우스 스크롤 기능 구현 | while문을 이용 |


## 정규표현식 (Regex) 
- 정규 표현식(regular expression)은 문자열에서 특정한 규칙을 가지는 문자열의 집합을 찾아내기 위한 검색 패턴
- ref : https://regexr.com/
  
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| Regex | [Regex](./codes/pandass/begginners.ipynb) | 정규표현식 예시 | |
| Regex_pandass | [Regex_pandass](./codes/pandass/begginners.py) | 정규표현식을 pandas에서 사용 방법 | |
| Regex_in_pandass | [Regex_in_pandass](./codes/pandass/TitanicFromDisaster_regexp_quest.py) | Regex in pandass | |


## 자연어 처리(NLP)
- NLP(Natural Language Processing, 자연어 처리)는 인공지능의 한 분야로서 머신러닝을 사용하여 텍스트와 데이터를 처리하고 해석
- 자연어의 의미를 분석하여 컴퓨터가 처리할 수 있도록 하는 일
  
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| wordcloud | [wordcloud](./codes/NLP/wordcloud_simple.ipynb) | 기본 자연어 처리 | | 
| wordcloud_regexp | [wordcloud_regexp](./codes/NLP/wordcloud_regexp.ipynb) |Regex을 이용하여 글자 전처리 | | 
| wordcloud_regexp | [wordcloud_regexp](./codes/NLP/wordcloud_regexp.ipynb) |Regex을 이용하여 글자 전처리 | | 
| 한글 형태소 분석기 | [morpheme_analyzer](./codes/NLP/morpheme_analyzer.ipynb) |한글 형태소 분석기 Okt | |
| withmecab | [withmecab](./codes/NLP/wordcloudwithmecab.ipynb) | withmecab | |
| tokenizers | [tokenizers](./codes/NLP/tokenizers.ipynb) | 불용어 처리 | 
| bestTopicnumber | [bestTopicnumber](./codes/NLP/LDA_gensim_bestTopicnumb.ipynb) | 최적의 토픽 단어 수 | 
| healthapp_PreProcess | [healthapp_PreProcess](./codes/NLP/healthapp_review_preprocess.ipynb) | 전처리|
| healthapp_LDA | [healthapp_LDA](./codes/NLP/healthapp_review_LDA.ipynb) | LDA |


## 감성분석
- 감성 분석(Sentiment Analysis)이란 텍스트에 들어있는 의견이나 감성, 평가, 태도 등의 주관적인 정보를 컴퓨터를 통해 분석하는 과정
  
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| sentiment_analyze_dictionary | [sentiment_analyze_dictionary](./codes/NLP/sentiment_analyze_dictionary.ipynb) | 감성 사전에 의한 감성 분석 | 
| sentiment_analyze_mechinelearing | [sentiment_analyze_mechinelearing](./codes/NLP/sentiment_analyze_mechinelearning.ipynb) | 머신러닝에 의한 감성 분석 | 
| LDA_gensim | [LDA_gensim](./codes/NLP/LDA_gensim.ipynb) | gensim 이용하여 LDA | 
| LDA_sklearn | [LDA_sklearn](./codes/NLP/LDA_sklearn.ipynb) | sklearn 이용하여 LDA | 

## MongoDB
- 오픈소스 비관계형 데이터베이스 관리 시스템(DMBS)
  
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| commend | [commend](./codes/gatheringdatas/mongodb/command.txt) | mongoDB의 명령어 정리 | |
| find| [findwithpandas](./codes/gatheringdatas/mongodb/findwithpandas.ipynb) | find with pandas | |
| insertMany |[insertManywithpandas](./codes/gatheringdatas/mongodb/insertManywithpandas.ipynb) | insertManywithpandas | |
| updates | [updates](./codes/gatheringdatas/mongodb/updates.py) | python으로 mongoDB update  | |
| updatewithpandas | [updatewithpandas](./codes/gatheringdatas/mongodb/updatewithpandas.ipynb) | update with pandas  | |

## MySQL
- 오픈소스 관계형 데이터베이스 관리 시스템(RDBMS)
  
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| connect_mysql | [connect_mysql](./codes/gatheringdatas/mysql/selectswithpandas.py) | pandas를 이용해서 mysql연결| |



## QUEST 
<details >
<summary> QUEST 진행 사항</summary>


### 자연어 처리 QUEST 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| mecab_quest | [mecab_quest](./codes/NLP/healthapp_review_LDA.ipynb) | 불용어 처리 | |

### 감성분석 QUEST 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| navermovierating | [navermovierating](./codes/NLP/navermovierating_mechinelearning.ipynb) |  머신러닝 이용 감성 분석, 타 사이트 댓글 이용 성능 확인| 

