import csv


class FetchData:
    def __init__(self):
        pass


    def fetch_deliveries(self):
        with open("data/deliveries.csv", "r") as file:
            d_rows = csv.DictReader(file)

            return list(d_rows)


    def fetch_matches(self):

        with open("data/matches.csv", "r") as file:
            m_rows = csv.DictReader(file)

            return list(m_rows)


