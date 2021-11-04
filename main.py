print("오징어 게임에 오신 것을 환영합니다.")
print("홀짝 게임을 시작합니다.")

import random
a = random.randint(1, 10)

# 참가자가 가진 구슬의 개수
marble = 10

while marble > 0 :
    # 구슬의 개수를 알려줌
    print("당신의 구슬의 개수 : {}개".format(marble))

    try: # 숫자를 제외한 것을 입력했을 때 오류 해결
        bet = int(input("구슬 몇 개를 베팅하시겠습니까? : "))
    except:
        print("숫자만 입력하세요.")
        continue
    
    if bet > marble :
        print("갖고 있는 구슬의 개수보다 많습니다.")
        print("다시 입력하세요")
        continue

    my = input("홀 혹은 짝을 입력하세요 : ")
    if my == "홀" or my == "짝" :
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
            marble = marble + bet # marble += bet
            if marble >= 20 :
                print("당신이 승리했습니다.")
                print("축하합니다.")
                break
            else :
                print("당신의 남은 구슬의 개수 : {}개".format(marble))
        
        else :
            print("오답입니다.")
            marble = marble - bet
            if marble > 0 :
                print("당신의 남은 구슬의 개수 : {}개".format(marble))
            else :
                print("빵!!")
    else :
        print("잘못 입력 다시 입력해라")
    