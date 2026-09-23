import random

def play():
    print("\n⚔️ [4. 텍스트 RPG] 고블린 토벌")
    player_hp = 30
    monster_hp = 25
    while player_hp > 0 and monster_hp > 0:
        print(f"❤️ 내 체력: {player_hp} | 👾 고블린: {monster_hp}")
        action = input("1. 공격  2. 도망 : ")
        if action == "1":
            dmg = random.randint(5, 12)
            monster_hp -= dmg
            print(f"🔥 고블린에게 {dmg}의 데미지!")
            if monster_hp > 0:
                m_dmg = random.randint(3, 8)
                player_hp -= m_dmg
                print(f"💥 고블린의 공격! {m_dmg}의 데미지 받음.")
        elif action == "2":
            print("🏃 도망쳤습니다.")
            return 10
    if player_hp > 0:
        print("🏆 승리! (+70점)")
        return 70
    print("💀 전사했습니다...")
    return 0
