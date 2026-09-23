import random

def play():
    print("\n✌️✊🖐️ [2. 가위바위보]")
    choices = ["가위", "바위", "보"]
    player = input("가위, 바위, 보 중 하나 입력: ").strip()
    if player not in choices:
        print("잘못된 입력입니다.")
        return 0
    computer = random.choice(choices)
    print(f"나: {player} vs 컴퓨터: {computer}")
    if player == computer:
        print("🤝 무승부!")
        return 20
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        print("🎉 승리! (+50점)")
        return 50
    else:
        print("❌ 패배!")
        return 0
