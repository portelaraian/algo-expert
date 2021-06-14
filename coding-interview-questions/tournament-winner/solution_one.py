# O(N) Time Complexity | O(K) Space Complexity
# where N is the number of competitions and
# K is the number of teams
def update_scores(team, current_winner, team_winners):
    if team_winners == {}:
        current_winner = team

    if team not in team_winners.keys():
        team_winners[team] = 0

    team_winners[team] += 3

    if team_winners[team] > team_winners[current_winner]:
        current_winner = team

    return current_winner, team_winners


def tournamentWinner(competitions, results):
    current_winner = None
    team_winners = {}

    for idx, match in enumerate(competitions):
        # Away won
        if results[idx] == 0:
            current_winner, team_winners = update_scores(
                match[1],
                current_winner,
                team_winners
            )
        else:
            current_winner, team_winners = update_scores(
                match[0],
                current_winner,
                team_winners
            )

    return current_winner
