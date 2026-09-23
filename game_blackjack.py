import random

def play():
    print("\n🃏 [5. 미니 블랙잭]")
    def draw(): return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11])
    player = [draw(), draw()]
    dealer = [draw(), draw()]
    while True:
        print(f"내 카드: {player} (합계: {sum(player)})")
        if sum(player) > 21:
            print("💥 버스트! 21 초과 패배.")
            return 0
        if input("카드를 더 받으시겠습니까? (y/n): ").lower() != 'y':
            break
        player.append(draw())
    while sum(dealer) < 17:
        dealer.append(draw())
    print(f"딜러 카드: {dealer} (합계: {sum(dealer)})")
    if sum(dealer) > 21 or sum(player) > sum(dealer):
        print("🎉 승리! (+60점)")
        return 60
    elif sum(player) == sum(dealer):
        print("🤝 무승부! (+20점)")
        return 20
    print("❌ 패배!")
    return 0
