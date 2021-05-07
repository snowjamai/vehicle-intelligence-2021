---
## Assignment 부분
1. GNB 폴더의 classifier.py의 train()함수와 predict() 함수를 수정하였다.
2. BP 폴더의 vehicle.py의 choose_next_state() 함수를 수정하였다.
3. BP 폴더의 cost_functions.py의 goal_distance_cost()함수와 inefficiency_cost()함수를 수정하였다.

---
## Hybrid Approach를 이용한 경로 예측
Hybrid Approach란 Model-based approach와 Data-driven approach를 합친 알고리즘이다. 해당 알고리즘은 
Model-based approach로서 계산으로 얻은 평균과 분산과 Data-driven approach로서
주변 차량의 주행 데이터로 차량들의 행동에 대한 평균과 분산에 대해 가우시안 나이브 베이즈를 이용하여 차량의 주행 경로를 얻는 알고리즘이다.

---

## classifier.py의 train 함수
1. 데이터에 대해 차선을 유지하는 keep, 왼쪽으로 가는 left, 오른쪽으로 가는 right로 나눔
2. 각 label에 대한 list를 가지고 있으며 각 차량의 행동에 대해 label에 맞게 각각의 데이터를 list에 저장
3. 각각의 저장된 list들을 np의 평균과 표준편차를 구하는 함수를 사용하기 위해 np.array로 변환
4. 변환된 각각의 array들을 통해 각 차량의 각 행동에 대한 표준 편차 및 평균을 구함

---

## classifier.py의 predict 함수
1. 각 행동에 대한 값을 1로 초기화
2. 각 행동에 대해 주어진 가우시안 함수를 이용하여 나올 수 있는 확률 구함
3. 구한 확률을 바탕으로 어떤 행동을 할지를 예측

---

## vehicle.py의 choose_next_state 함수
1. 가능한 모든 state들에 대해 주변차량들의 예측된 위치들을 이용하여 자차의 trajectory를 구함
2. 해당 trajectory에서 얻는 cost를 계산하여 cost라는 리스트의 0번째 인덱스에는 state, 1번째 인덱스에는 앞에서 구한 cost를 삽입
3. 모든 state들에 대한 cost 계산이 완료된 후 가장 작은 cost를 갖는 state를 추출
4. 추출된 state를 이용하여 차량의 경로를 반환

---

## vehicle.py의 goal_distance_cost 함수

1. 출발지부터 도착지까지 절반까지는 가장 빠른 차선을 이용하여 주행을 함
2. 도착지에 가까워 질수록 현재 차선에서 도착지까지의 거리와 가려고하는 차선에서 도착지까지의 거리의 합이 작을수록 cost를 높게 설정

---

## vehicle.py의 inefficiency_cost 함수

1. 출발지부터 도착지까지 절반까지는 가장 빠른 차선을 이용하여 주행을 함
2. 도착지에 가까워 질수록 현재 차선에서 도착지까지의 거리와 가려고하는 차선에서 도착지까지의 거리의 합이 클수록 cost를 높게 설정
3. cost를 작게하기 위해 도착지의 lane으로 운전

---
## 느낀점
이번 숙제는 굉장히 어려웠다. 시뮬레이션으로 한다는것은 굉장히 흥미로웠지만 나와있는 답이 아닌, 스스로 무언가를 생각하고 해당 코딩을 한다는것이 매우 어렵고 힘들게 느껴졌던것같다. 하지만 재미있었고 실제로 해당 시뮬레이션이 제대로 동작하는것을 보니 뿌듯함도 느꼈다.