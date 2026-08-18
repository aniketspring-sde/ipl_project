import csv

from matplotlib import pyplot as plt

SEASON = "season"
MATCH_ID = "id"
TARGET_SEASON = "2015"

DELIVERY_MATCH_ID = "match_id"
BOWLER = "bowler"
TOTAL_RUNS = "total_runs"
WIDE_RUNS = "wide_runs"
NO_BALL_RUNS = "noball_runs"


def calculate(deliveries_file, matches_file):
    match_ids = set()

    with open(matches_file, "r") as matches_data:
        matches_reader = csv.DictReader(matches_data)

        for match in matches_reader:
            if match[SEASON] == TARGET_SEASON:
                match_ids.add(match[MATCH_ID])

    bowlers = {}

    with open(deliveries_file, "r") as deliveries_data:
        deliveries_reader = csv.DictReader(deliveries_data)

        for delivery in deliveries_reader:

            if delivery[DELIVERY_MATCH_ID] not in match_ids:
                continue

            bowler = delivery[BOWLER]

            total_runs = int(delivery[TOTAL_RUNS])
            wide_runs = int(delivery[WIDE_RUNS])
            noball_runs = int(delivery[NO_BALL_RUNS])

            if bowler not in bowlers:
                bowlers[bowler] = {
                    "runs": 0,
                    "balls": 0
                }

            bowlers[bowler]["runs"] += total_runs

            if wide_runs == 0 and noball_runs == 0:
                bowlers[bowler]["balls"] += 1

    economy_rates = {}

    for bowler in bowlers:
        runs = bowlers[bowler]["runs"]
        balls = bowlers[bowler]["balls"]

        if balls > 0:
            overs = balls / 6
            economy_rate = runs / overs

            economy_rates[bowler] = economy_rate

    economy_rates = dict(
        sorted(
            economy_rates.items(),
            key=lambda item: item[1]
        )[:10]
    )

    return economy_rates


def plot(economy_rates):
    bowlers = list(economy_rates.keys())
    economy = list(economy_rates.values())

    plt.figure(figsize=(12, 6))

    plt.bar(bowlers, economy)

    plt.xlabel("Bowler")
    plt.ylabel("Economy Rate")
    plt.title("Top 10 Economical Bowlers in 2015")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig("../plots/q8_Top_10_economical_bowlers_in_the_year_2015.png")
    plt.show()


def execute():
    matches_file = "../../data/matches.csv"
    deliveries_file = "../../data/deliveries.csv"

    economy_rates = calculate(
        deliveries_file,
        matches_file

    )

    plot(economy_rates)

    return economy_rates


execute()