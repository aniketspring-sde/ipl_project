import csv
from matplotlib import pyplot as plt


SEASON = "season"
WINNER = "winner"


def calculate(matches_file):
    team_season_wins = {}

    with open(matches_file, newline="", encoding="utf-8") as matches_data:
        matches_reader = csv.DictReader(matches_data)

        for match in matches_reader:
            season = match[SEASON]
            winner = match[WINNER]

            if season not in team_season_wins:
                team_season_wins[season] = {}

            if winner == "":
                continue

            if winner not in team_season_wins[season]:
                team_season_wins[season][winner] = 0

            team_season_wins[season][winner] += 1

    return team_season_wins


def plot(team_season_wins):
    seasons = sorted(team_season_wins.keys())

    teams = set()

    for season in team_season_wins:
        for team in team_season_wins[season]:
            teams.add(team)

    teams = sorted(teams)

    bottom = [0] * len(seasons)

    plt.figure(figsize=(15, 7))

    for team in teams:
        match_wins = []

        for season in seasons:
            if team in team_season_wins[season]:
                match_wins.append(team_season_wins[season][team])
            else:
                match_wins.append(0)

        plt.bar(
            seasons,
            match_wins,
            bottom=bottom,
            label=team
        )

        for index in range(len(bottom)):
            bottom[index] += match_wins[index]

    plt.xlabel("Year")
    plt.ylabel("Number of Matches Won")
    plt.title("Number of Matches Won per Team per Year")

    plt.xticks(rotation=45)

    plt.legend(
        title="Team",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()
    plt.savefig("../plots/q6_matches_won_per_team_per_year_in_IPL.png")
    plt.show()


def execute():
    matches_file = "../../data/matches.csv"

    team_season_wins = calculate(matches_file)

    plot(team_season_wins)

    return team_season_wins


execute()