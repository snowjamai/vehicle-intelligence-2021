---
# main.py (line 11 ~ 60)


1. 차량의 위치에 대한 표준편차를 1, 제어에 대한 표준편차 1, 나무를 발견할 표준편차 1, 시간당 움직일 거리에 대한 표준편차도 1 로 설정

2. 맵의 크기는 25로 설정하고 각 나무들이 있는 위치는 [3,9,14,23]으로 설정

3. 차량이 스텝당 거리 1씩 이동한다 할때 관측 가능한 나무들의 거리는 observations라는 list의 값과 같음

4. initialize_priors라는 함수로 사전 확률을 구함

---

# markov_localizer.py

### initialize_priors 함수
1. 인자로 받은 map_size만큼 0으로 초기화된 priors 생성

2. 인자로 받은 landmarks에 대해 차량의 위치에 대한 표준편차(position_stdev)가 1이므로 차량의 위치가 나무 주변에 있을 때 차량이 존재가능한 위치는 나무의 위치 p에서 position_stdev만큼 뺀값부터 더한값까지 가능

3. 차량의 위치로 가능한 모든 위치들을 positions에 넣음

4. 초기 차량이 있을 확률은 어디든 동일하니 전체 확률 1 에서 각 positions만큼 나눈값이 positions에 들어있는 각 값에 대한 확률

5. 각 확률들을 positions에 있는 위치 p에 대해 priors[p]에 더해줘서 초기 차량이 있을 위치 구함

---
# main.py (line 63 ~ 77)

5. map_size만큼 0으로 초기화된 posteriors 생성

6. 차량의 나무 관측 사실을 바탕으로 추정 위치를 구하기 위해 motion_model이라는 함수를 이용하여 추정 위치에 대한 확률 구함

---
# markov_localizer.py

### motion_model 함수
1. 구하고 싶은 위치에 대한 확률 position_prob 를 0으로 초기화시킴

2. 모든 맵에 대해 탐색을 하며 다음으로 이동 가능한 위치를 i로 선정

3. 모든 i와 함수의 인자로 받은 position과의 normal distribution을 이용해(norm_pdf 함수) 전이확률 tr_pr(transition probability)을 구함 (차량은 스텝당 1씩 이동하고 제어에 대한 표준편차가 1이므로 m = 1, stdev = control_stdev 가 됨 )을 구함

4. norm_pdf 함수로 구한 position에서 각 위치 i에서의 normal distribution의 확률값과 사전확률로 구한 차량의 위치가 해당 위치에 존재할 확률을 곱하여 차량의 이동에 대한 위치 확률을 구함

---
# main.py (line 78 ~ 79)
7. landmark와 떨어진 거리를 토대로 관측 가능한 범위를 구함 ()

---
# markov_localizer.py

### estimate_pseudo_range 함수
1. pseudo_ranges라는 빈 list 생성
2. 전체 landmark에 대해 인자로 받은 position p에 대한 거리를 구함
3. 차량은 차량의 앞에 있는 landmark만 관측 가능하므로, dist가 0보다 큰 거리만 pseudo_range라는 list에 append 해줌
---

#main.py (line 84 ~ 86)
8.  obsercation_prob를 구하기 위해 observation_model 함수를 사용

---
# markov_localizer.py

### observation_model 함수
1. pseudo_range의 길이는 pseudo_position에서의 landmark와의 거리를 의미
2. observations의 길이는 차량이 실제 관측한 거리 의미
3. observations의 길이가 0 이라면 확률은 알수 없음
4. observations의 길이가 pseudo_ranges보다 길수는 없음(observation은 관측값이고, pseudo_ranges는 pseudo position에서 landmark에 대한 거리차이이므로)
5. obsercations의 관측값 평균이 pseudo_ranges[i]이고 표준편차가 stdev인 가우시안 분포에서 observations[i]가 관측되었을 때의 확률들을 모두 곱하여 distance_prob를 생성

---
#main.py (line 90 ~ 106)
9.  각 위치 pseudo_position에대한 사후 확률 posteriors를 구하기 위해 앞에서 구한 motion_prob * observation_prob 해줌
10. 구한 사후확률에 대한 분포를 normalize_distribution 함수를 이용하여 normalize 해줌
11. 사전 확률을 사후 확률로 update함
12. 구한 사후 확률을 graph라는 list에 append
---

#main.py (line 108 ~ )
13. 앞에서 append한 graph를 이용하여 화면에 그래프를 그려 표시
---