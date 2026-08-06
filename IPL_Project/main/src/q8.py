class Q8:

    def __init__(self):
        self.df = {}


    def economical_bowlers_2015(self,deliveries,matches):

        # Get 2015 match IDs
        match_ids = set()

        for match in matches:

            if match['season'] == '2015':
                match_ids.add(match['id'])


        # Store runs and legal balls for each bowler
        bowlers = {}

        for delivery in deliveries:

            if delivery['match_id'] not in match_ids:
                continue

            bowler = delivery['bowler']

            total_runs = int(delivery['total_runs'])
            wide_runs = int(delivery['wide_runs'])
            noball_runs = int(delivery['noball_runs'])

            if bowler not in bowlers:

                bowlers[bowler] = {
                    'runs': 0,
                    'balls': 0
                }

            # Runs conceded
            bowlers[bowler]['runs'] += total_runs

            # Wide and no-ball are not legal deliveries
            if wide_runs == 0 and noball_runs == 0:
                bowlers[bowler]['balls'] += 1


        # Calculate economy rate
        for bowler in bowlers:

            runs = bowlers[bowler]['runs']
            balls = bowlers[bowler]['balls']

            if balls > 0:

                overs = balls / 6

                economy = runs / overs

                self.df[bowler] = economy


        # Sort by economy rate
        self.df = dict(
            sorted(
                self.df.items(),
                key=lambda item: item[1]
            )[:10]
        )

        return self.df


    def plot(self):

        import matplotlib.pyplot as plt

        bowlers = list(self.df.keys())
        economy = list(self.df.values())

        plt.figure(figsize=(12, 6))

        plt.bar(
            bowlers,
            economy
        )

        plt.xlabel("Bowler")
        plt.ylabel("Economy Rate")
        plt.title("Top 10 Economical Bowlers in 2015")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        plt.show()


    def exc(self,deliveries,matches):

        ans = self.economical_bowlers_2015(deliveries,matches)
        self.plot()
        return ans