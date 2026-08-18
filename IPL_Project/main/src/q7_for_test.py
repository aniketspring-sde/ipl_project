import csv
from matplotlib import pyplot as plt


SEASON = "season"
MATCH_ID = "id"
DELIVERY_MATCH_ID = "match_id"
BOWLING_TEAM = "bowling_team"
EXTRA_RUNS = "extra_runs"
TARGET_SEASON = "2016"


def calculate(matches_file, deliveries_file):
    match_ids = set()
    extra_runs_by_team = {}

    with open(matches_file, newline="", encoding="utf-8") as matches_data:
        matches_reader = csv.DictReader(matches_data)

        for match in matches_reader:
            if match[SEASON] == TARGET_SEASON:
                match_ids.add(match[MATCH_ID])

    with open(deliveries_file, newline="", encoding="utf-8") as deliveries_data:
        deliveries_reader = csv.DictReader(deliveries_data)

        for delivery in deliveries_reader:
            if delivery[DELIVERY_MATCH_ID] not in match_ids:
                continue

            team = delivery[BOWLING_TEAM]
            extra_runs = int(delivery[EXTRA_RUNS])

            if team not in extra_runs_by_team:
                extra_runs_by_team[team] = 0

            extra_runs_by_team[team] += extra_runs

    return extra_runs_by_team


def plot(extra_runs_by_team):
    teams = list(extra_runs_by_team.keys())
    extra_runs = list(extra_runs_by_team.values())

    plt.figure(figsize=(12, 6))

    plt.bar(teams, extra_runs)

    plt.xlabel("Team")
    plt.ylabel("Extra Runs")
    plt.title("Extra Runs Conceded per Team in 2016")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def execute():
    matches_file = "../../data/matches.csv"
    deliveries_file = "../../data/deliveries.csv"

    extra_runs_by_team = calculate(
        matches_file,
        deliveries_file
    )

    plot(extra_runs_by_team)

    return extra_runs_by_team


