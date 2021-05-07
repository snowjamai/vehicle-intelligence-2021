---
## Assignment 부분
hybrid_astar.py의 expand() 부분, search(), theta_to_stack_num(), heuristic()부분을 수정하였다.

---
## Hybrid A*의 정의
Hybrid A*란 일반적인 A*알고리즘에 차량의 motion에 대한 정보를 넣어서 만든 알고리즘이다. 해당 알고리즘은 이러한 모션 정보가 들어가 일반적인 A*알고리즘과 다르게 연속성을 갖고있고 실제 운전을 할 때 사용할 수 있지만 결과에 대해 optimality를 보장 할 수 없으며 경로가 존재하더라도 complete하지 않을 수 있다는 단점이 존재한다.


---

## hybrid_astar.py의 expand 함수

1. 현재 차량의 위치 x, y, theta 등을 가져옴
2. 한번에 omega_step씩 차량의 각도를 변경시키며 조향각을 구함
3. 조향각을 구한 뒤 현재위치에서 속도와 조향각을 이용해서 다음으로 갈 수 있는 위치를 구함
4. 해당 위치를 차량이 갈 수 있다면 해당 위치에 대한 cost를 구함
5. 구한 cost와 경로를 next_states에 삽입

---

## hybrid_astar.py의 heuristic 함수

1. 목적지의 x좌표와 현재 x좌표를 빼고 제곱하고 목적지의 y좌표와 현재 y좌표를 빼고 제곱한값을 더해 루트를 씌운값을 반환
2. 해당값은 유클리드 거리를 계산한 식

---

## hybrid_astar.py의 theta_to_stack_num 함수

1. self.dim[0]의 크기를 이용한 interval을 정의
2. 정의한 interval보다 작을때까지 theta값을 줄이며 s_cnt 값을 증가
3. s_cnt가 NUM_THETA_CELL와 같은값이 되면 s_cnt값을 0으로 초기화 
4. theta 값이 interval보다 작은값까지 들어오면 해당 s_cnt값을 반환 
---

## hybrid_astar.py의 search 함수

1. theta_to_stack_num함수를 이용하여 stack 값을 저장
2. 시작점에 대한 값 초기화
3. opend라 하는 list에 초기 시작값 s를 삽입
4. opend라하는 list가 빌때까지 반복
5. opend에 있는 값중 'f'(코스트)가 최소가 되게 정렬
6. opend에서 코스트가 최소인 지점을 now라는 변수에 저장
7. opend에서 뽑은 경로가 도착지라면 경로를 찾은거므로 반복문 종료
8. 도착지가 아닐경우 now경로를 이용하여 expand할 수 있는 경로들을 next_states로 삽입
9. 모든 가능한 경로 next_states에 대해서 각각의 거리를 구함
10. 구한 거리를 통해서 해당 경로가 map안에 존재 가능하면 possible값을 True 불가능하면 False로 설정
11. 만약 해당 경로가 주행 가능한 거리라면 closed값에 해당 경로에 대해 표기를 하고 opend list에 해당 경로 삽입

---

## 느낀점
처음에 과제를 하기전에 A*알고리즘은 많이 구현해본 적이있어 굉장히 쉬울줄알았다. 하지만 실제로 과제를 수행해보니 hybrid A*알고리즘은 다른 부분을 생각해줘야할게 있어 생각보다 시간이 더 오래 걸렸다. 하지만 새로운 알고리즘을 알게되어 굉장히 뿌듯하고 재밌었다.