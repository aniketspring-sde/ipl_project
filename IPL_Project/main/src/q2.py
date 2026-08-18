import csv
from matplotlib import pyplot as plt


BATTING_TEAM = "batting_team"
BATSMAN = "batsman"
BATSMAN_RUNS = "batsman_runs"
RCB = "Royal Challengers Bangalore"


def calculate(deliveries_file):
    rcb_runs = {}

    with open(deliveries_file, newline="", encoding="utf-8") as deliveries_data:
        matches_reader = csv.DictReader(deliveries_data)

        for match in matches_reader:
            if match[BATTING_TEAM] == RCB:
                batsman = match[BATSMAN]
                runs = int(match[BATSMAN_RUNS])

                if batsman not in rcb_runs:
                    rcb_runs[batsman] = 0

                rcb_runs[batsman] += runs

    top_batsmen = dict(
        sorted(
            rcb_runs.items(),
            key=lambda batsman_runs: batsman_runs[1],
            reverse=True
        )[:10]
    )

    return top_batsmen


def plot(rcb_runs):
    plt.figure(figsize=(10, 5))

    plt.bar(rcb_runs.keys(), rcb_runs.values())

    plt.xticks(rotation=90)
    plt.xlabel("Batsmen")
    plt.ylabel("Runs")
    plt.title("Top 10 RCB Batsmen by Runs")

    plt.tight_layout()
    plt.savefig("../plots/q2_top_10_rcb_batsmen.png")
    plt.show()


def execute():
    deliveries_file = "../../data/deliveries.csv"

    rcb_runs = calculate(deliveries_file)
    plot(rcb_runs)

    return rcb_runs


execute()