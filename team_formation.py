def team_formation(score, team, m):
    """
    Calculates the sum of the scores of the team members
    formed on the basis of the window m and number of team
    members.

    Arguments:
        score {list[int]} -- Contains scores of the members.
        team {int} -- Number of members required in a team.
        m {int} -- Window used to choose from score.

    Returns:
        int -- Sum of the scores of the team members.
    """
    # Write your code here
    if team >= len(score):
        return sum(score)
    res = []
    max_scores1_idx = score.index(max(score[:m])
    max_scores2_idx=score.index(max(score[-m-1:])
    print(max_scores1_idx, max_scores2_idx)
    # for i, j in zip(scores1, scores2[::-1]):
    #     if i >= j:
    #         res.append(i)
    #     else:
    #         res.append(j)
    # return sum(res[:team])
