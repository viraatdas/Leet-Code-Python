def stoneGame(piles):
    score = {}
    score['Alex'] = 0
    score['Lee'] = 0
    while piles:
        score['Alex'] += max(piles[0], piles[len(piles) - 1])
        piles.remove(max(piles[0], piles[len(piles) - 1]))

        score['Lee'] += max(piles[0], piles[len(piles) - 1])
        piles.remove(max(piles[0], piles[len(piles) - 1]))i

    if score['Alex'] > score['Lee']:
        return True
    return False
        
