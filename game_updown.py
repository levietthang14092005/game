import random

def play():
    print("\n🎯 [1. UP & DOWN] 1~100 사이의 숫자를 맞추세요!")
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("숫자 입력: "))
            attempts += 1
            if guess < secret:
                print("⬆️ UP!")
            elif guess > secret:
                print("⬇️ DOWN!")
            else:
                print(f"🎉 정답! {attempts}번 만에 맞추셨습니다.")
                return max(100 - (attempts * 10), 10)
        except ValueError:
            print("숫자만 입력해 주세요.")
