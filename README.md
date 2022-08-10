# EatShare-AI

## model = kobert

dataset label => 0~8 (2^3) / 0~26 (3^3)
탄단지

### [기초대사량 계산기](https://u-health.dobong.go.kr/hcal/metabolism.asp)
근데 여기서의 기초대사량은 최소한의 칼로리를 나타냄

따라서 아래 식을 따름
### activate는 활동 지수 이며 적음(25), 보통(30), 많음(40)으로 분류한다
## 권장 섭취 칼로리 계산
$$ (cm - 100) * 0.9 * activate $$


## 탄단지 비율
- 이상적인 탄단지 비율 = 4:4:2
- 다이어트 시 = 3:4:2
- 운동량이 많은 사람 = 5:3:2

## 탄단지 계산
- 탄 : 권장 섭취 칼로리 * 탄수화물 비율 / 40
- 단 : 권장 섭취 칼로리 * 단백질 비율 / 40
- 지 : 권장 섭취 칼로리 * 지방 비율 /90

ex: 키 160, 활동지수가 보통(30)이며 다이어트와 운동량이 많지 않음.
- 탄단지 비율 = 4:4:2
- 권장 섭취 칼로리 = (160-100) * 0.9 * 30 = 1620
- 탄 162g, 단 162g, 지 36g
