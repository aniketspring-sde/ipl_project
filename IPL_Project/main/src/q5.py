import csv
from matplotlib import pyplot as plt


SEASON = "season"


def calculate(matches_file):
    matches_per_season = {}

    with open(matches_file, newline="", encoding="utf-8") as matches_data:
        matches_reader = csv.DictReader(matches_data)

        for match in matches_reader:
            season = match[SEASON]

            if season not in matches_per_season:
                matches_per_season[season] = 0

            matches_per_season[season] += 1

    return matches_per_season


def plot(matches_per_season):
    plt.figure(figsize=(10, 5))

    plt.bar(
        matches_per_season.keys(),
        matches_per_season.values()
    )

    plt.xticks(rotation=90)
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Number of Matches Played in Each Season")

    plt.tight_layout()

    plt.savefig("../plots/q5_matches_played_per_year_for_all_the_years_in_IPL.png")
    plt.show()


def execute():
    matches_file = "../../data/matches.csv"

    matches_per_season = calculate(matches_file)

    plot(matches_per_season)

    return matches_per_season


execute()