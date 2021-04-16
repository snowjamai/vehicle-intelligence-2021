---
## Assignment 부분
kalman_filter.py의 update_ekf(line 26 ~ 51)의 부분을 주석에 맞게 추가하였다.


---
## EKF 정의

Extended Kalman Filter의 약자이며 이름 그대로 Kalman Filter에서 확장된 개념을 가진다.
KF(Kalman Filter)는 선형 가우시안 모델을 따르는 경우에 사영되며, EKF는 비선형 가우시안 모델을 따를때 사용된다.

이 둘다 agent의 state를 추정하기 위해 사용되는 방법들이며 먼저 control에 대한 agent의 state prediction을 한 후, observation을 통한 prediction에 대한 correction으로 state를 update 해간다.


---

## EKF 의 update_ekf 함수
1. agent의 위치 및 속도에 대한 변수 self.x를 이용하여 자코비안 행렬 Hj 생성
2. 수식 계산을 통해 S와 K를 구함
3. rho, phi, rhodot을 구하여 입력 z와의 차를 이용해 y를 구함
4. 구한 y의 phi 값은 [-np.pi, np.pi]이므로 이에 맞게 줄임
5. 구한 값들을 바탕으로 새로운 추정 self.P를 구함

---

## 느낀점
개념으로 배우기만 할때에는 정확하게 와닿지 않았지만 해당 코드를 통한 구현을 직접 실행해 보면서 원리를 이해하며 직접 구현해볼 수 있었던 좋은 시간이 됬던것 같다. 