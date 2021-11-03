print("오징어 게임에 오신 것을 환영합니다.")
print("홀짝 게임을 시작합니다.")

# 구슬로 홀짝 게임 규칙
# 상대방이 구슬의 개수를 정한다.

# a = 5
# 10개 이하의 무작위 수로 입력
#1
# import random
# a = random.randrange(1, 10)
#2
import random
a = random.randint(1, 10)

# print(a)
# 내가 홀 또는 짝을 얘기한다.

# my = "홀"
# 고정되어 있는 값을 사용자가 입력
my = input("홀 혹은 짝을 입력하세요 : ")
# print(my)
# 만약 내가 얘기한 홀과 짝 중에 맞으면 맞다
# 틀리면 틀렸다
# 상대방의 구슬의 개수에서 2로 나누어 나머지가 0이면 짝
# 나머지가 1이면 홀
dab = ""
print("구슬의 개수 :",a)

if a % 2 == 0 :
    print("구슬은 짝입니다.")
    dab = "짝"
else :
    print("구슬은 홀입니다.")
    dab = "홀"

if my == dab :
    print("정답입니다.")
else :
    print("빵!!")