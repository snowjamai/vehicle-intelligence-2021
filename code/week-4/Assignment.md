---
## Assignment 부분
particle_filter.py의 update_weights() 부분과 resample()부분을 수정하였다.

---
## Particle_Filter의 정의
전 주에 실습했던 EKF와 같이 noise가 존재하는 observation들에 대해 필터를 사용하여 실제 위치를 추정하는 필터이다. 
Particle Filter는 측정 범위안에 random한 particle을 뿌리고 각각의 particle 에서 랜덤하게 움직인 거리를 추정하는 prediction 단계를 거치고, 예측된 particle의 위치와 센서로 측정된 observation 위치를 이용하여 particle의 weight를 업데이트한다.
각 particle들의 weight가 업데이트 된 후에는 weight가 큰 particle들을 복사하여 전과 particle의 크기가 같게 resampling한다.
위와 같은 과정을 반복하며 agent의 위치 추정이 가능하다.

---

## Particle Filter의 update_weights 함수
1. 예측된 particles(self.particles)에서 하나의 파티클 p를 뽑음
2. 뽑은 p에 대해서 sensor 인지 가능한 거리 내에 있는 Landmark를 저장하는 CanSeeLandmark라는 변수의 list를 선언
3. 차량에서 관측된 observations의 pos 정보를 map의 위치로 바꾸어 저장하는 TransformObserve라는 변수의 list를 선언  
4. 인자로 받은 map_landmarks에서 id와 pos를 이용하여 p와의 거리를 측정하여 센서 측정 가능 거리 내에 있으면 CanSeeLandmark에 해당 id와 pos를 저장
5. 인자로 받은 observations에서 측정된 위치를 map 위치로 바꾸기 위한 식을 적용하여  TransformObserve에 저장
6. CanSeeLandmark가 비어있다면 해당 p는 의미가 없으므로 다음 particle로 넘김
7. 좌표 변환한 TransformObserve와 CanSeeLandmark의 id와 매칭하여 associate_landmark로 반환
8. associate_landmark의 각 landmark 정보와 particle과의 거리 차이를 이용한 정규 분초 함수로 particle의 weight를 구함
---

## Particle Filter의 resample 함수
1. self.particle을 weights 라는 변수로 깊은 복사
2. particle의 갯수를 N에 저장
3. 길이가 N인 랜덤 배열 positions 생성
4. 길이가 N이며 0으로 초기화된 indexes 배열 새성
5. np.cumsum을 이용해 cumulative_sum에 합 구함
6. systematic resampling을 사용하여 weight에 대한 업데이트 진행
---

## 느낀점
이번 숙제는 굉장히 어려웠다. 특히 파티클 함수에 대한 weight update에 대해서는 비교적 쉽게 접근하여 구현할 수 있었지만, resample 부분에서 막혀 구글링을 통해 여러 자료를 찾아보았다. 
하지만, 찾아보니 resample 방법이 비교적 다양하였고 같은 방법임에도 코드가 달라 해당 과제에 맞춰 바꾸기가 쉽지 않았다. 하지만 해당 과제를 진행하며 파티클 필터에 대한 이해도가 높아진거 같아 뿌듯한 과제였다.