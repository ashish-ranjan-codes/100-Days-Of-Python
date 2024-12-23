# Calculate Love Score for 2 persons if their name containe letters from TRUE or LOVE

def love_calculator(boy, girl):
    combinedName = boy + girl
    word1 = 'true'
    word2 = 'love'

    score1 = 0
    score2 = 0

    for ch in word1:
        score1 += combinedName.count(ch)

    for ch in word2:
        score2 += combinedName.count(ch)
    
    print(f"{score1}{score2}")


boy = input("Enter boy's name: ").lower()
girl = input("Enter girl's name: ").lower()

love_calculator(boy, girl)