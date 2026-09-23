import random
import time

def play():
    print("\n⌨️ [6. 스피드 타자]")
    sentences = ["Fire burns brighter in the dark.", "Python is fast and fun.", "Practice makes perfect."]
    target = random.choice(sentences)
    print(f"제시문: {target}")
    input("준비되면 엔터를 누르세요...")
    start = time.time()
    user_input = input("입력: ")
    elapsed = round(time.time() - start, 2)
    if user_input == target:
        score = max(100 - int(elapsed * 10), 20)
        print(f"🎉 성공! 소요시간: {elapsed}초 (+{score}점)")
        return score
    print("❌ 오타 발생!")
    return 0
