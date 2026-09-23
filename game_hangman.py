import random

def play():
    print("\n🔤 [3. 행맨]")
    words = ["python", "blaze", "fire", "developer", "arcade"]
    target = random.choice(words)
    guessed = set()
    chances = 5
    while chances > 0:
        display = "".join([c if c in guessed else " _ " for c in target])
        print(f"\n단어: {display} | 남은 기회: {chances}")
        if " _ " not in display:
            print(f"🎉 정답입니다! 단어: {target}")
            return 80
        guess = input("알파벳 입력: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            continue
        if guess in target:
            guessed.add(guess)
            print("✨ 정답에 포함된 글자입니다!")
        else:
            chances -= 1
            print("❌ 틀렸습니다.")
    print(f"💀 실패! 정답은 '{target}'이었습니다.")
    return 0
