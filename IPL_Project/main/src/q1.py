from matplotlib import pyplot as plt


class Q1:
    def __init__(self):
        self.total_runs = {}
        # self.d_rows = FetchData().fetch_deliveries()


    def run_teams(self, d_rows):

        # d_rows = FetchData().fetch_deliveries()

        for row in d_rows:
            if row['batting_team'] in self.total_runs:
                self.total_runs[row['batting_team']] += int(row['total_runs'])
            else:
                self.total_runs[row['batting_team']] = 0
                self.total_runs[row['batting_team']] += int(row['total_runs'])

        return self.total_runs




    def plot(self):
        plt.figure(figsize=(10, 5))

        plt.bar(self.total_runs.keys(), self.total_runs.values())

        plt.xticks(list(self.total_runs.keys()), rotation=90)

        plt.show()

    def exc(self,d_rows):
        ans = self.run_teams(d_rows)
        self.plot()
        return ans