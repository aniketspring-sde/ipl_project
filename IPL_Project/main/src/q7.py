class Q7:

    def __init__(self):
        self.df = {}


    def extra_runs_2016(self,matches,deliveries):



        # Get all match IDs from 2016
        match_ids = set()

        for match in matches:

            if match['season'] == '2016':
                match_ids.add(match['id'])

        # Calculate extra runs
        for delivery in deliveries:

            if delivery['match_id'] not in match_ids:
                continue

            team = delivery['bowling_team']
            extra_runs = int(delivery['extra_runs'])

            if team in self.df:
                self.df[team] += extra_runs
            else:
                self.df[team] = extra_runs

        return self.df

    def plot(self):

        import matplotlib.pyplot as plt

        teams = list(self.df.keys())
        extra_runs = list(self.df.values())

        plt.figure(figsize=(12, 6))

        plt.bar(
            teams,
            extra_runs
        )

        plt.xlabel("Team")
        plt.ylabel("Extra Runs")
        plt.title("Extra Runs Conceded per Team in 2016")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()
        plt.show()

    def exc(self,matches,deliveries):

        ans = self.extra_runs_2016(matches, deliveries)
        self.plot()
        return ans