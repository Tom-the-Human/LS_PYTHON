def high_scores_in_round(scores):
    return [score for score in scores
            if all(points > 4 for points in score)]

rounds = [[6, 8], [2, 9], [15, 11], [4, 100]]
print(high_scores_in_round(rounds)) # [[6, 8], [15, 11]]