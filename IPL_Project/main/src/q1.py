import csv
from matplotlib import pyplot as plt


BATTING_TEAM = "batting_team"
TOTAL_RUNS = "total_runs"


def calculate(deliveries_file):
    total_runs = {}

    with open(deliveries_file, "r") as deliveries_data:
        matches_reader = csv.DictReader(deliveries_data)

        for match in matches_reader:
            batting_team = match[BATTING_TEAM]
            runs = int(match[TOTAL_RUNS])

            if batting_team not in total_runs:
                total_runs[batting_team] = 0

            total_runs[batting_team] += runs

    return total_runs


def plot(total_runs):
    plt.figure(figsize=(10, 5))

    plt.bar(total_runs.keys(), total_runs.values())

    plt.xticks(rotation=90)
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.title("Total Runs by Each Team")

    plt.tight_layout()
    # plt.savefig("q1.png")
    plt.show()


def execute():
    deliveries_file = "../../data/deliveries.csv"

    total_runs = calculate(deliveries_file)
    plot(total_runs)

    return total_runs


execute()