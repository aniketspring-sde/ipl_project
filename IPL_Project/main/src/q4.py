import csv
import numpy as np
from matplotlib import pyplot as plt


SEASON = "season"
TEAM_1 = "team1"
TEAM_2 = "team2"


def calculate(matches_file):
    team_season_matches = {}

    with open(matches_file, newline="", encoding="utf-8") as matches_data:
        matches_reader = csv.DictReader(matches_data)

        for match in matches_reader:
            season = match[SEASON]
            team_1 = match[TEAM_1]
            team_2 = match[TEAM_2]

            if season not in team_season_matches:
                team_season_matches[season] = {}

            if team_1 not in team_season_matches[season]:
                team_season_matches[season][team_1] = 0

            if team_2 not in team_season_matches[season]:
                team_season_matches[season][team_2] = 0

            team_season_matches[season][team_1] += 1
            team_season_matches[season][team_2] += 1

    return team_season_matches


def plot(team_season_matches):
    seasons = sorted(team_season_matches.keys())

    teams = set()

    for season in team_season_matches:
        for team in team_season_matches[season]:
            teams.add(team)

    teams = sorted(teams)

    bottom = np.zeros(len(seasons))

    plt.figure(figsize=(15, 7))

    for team in teams:
        match_counts = []

        for season in seasons:
            if team in team_season_matches[season]:
                match_counts.append(team_season_matches[season][team])
            else:
                match_counts.append(0)

        plt.bar(
            seasons,
            match_counts,
            bottom=bottom,
            label=team
        )

        bottom = bottom + np.array(match_counts)

    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Matches Played by Each Team in Each Season")

    plt.xticks(rotation=45)

    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()

    plt.savefig("../plots/q4_matches_played_by_team_by_season.png")
    plt.show()


def execute():
    matches_file = "../../data/matches.csv"

    team_season_matches = calculate(matches_file)

    plot(team_season_matches)

    return team_season_matches


execute()