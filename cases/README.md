<details >
<summary>Titanic From Disater_타이타닉 참사</summary>

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
<summary>Type Of Contract Channel_계약 유형 채널</summary>
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