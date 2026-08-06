class Q6:

    def __init__(self):
        self.df = {}


    def team_season_wins(self,m_rows):



        for row in m_rows:

            season = row['season']
            winner = row['winner']


            if season not in self.df:
                self.df[season] = {}


            if winner == '':
                continue


            if winner in self.df[season]:
                self.df[season][winner] += 1
            else:
                self.df[season][winner] = 1

        return self.df

    def plot(self):

        import matplotlib.pyplot as plt
        import numpy as np

        seasons = sorted(self.df.keys())

        # Get all teams
        teams = set()

        for season in self.df:
            teams.update(self.df[season].keys())

        teams = sorted(teams)

        # Starting position of each stacked bar
        bottom = np.zeros(len(seasons))

        plt.figure(figsize=(15, 7))

        for team in teams:

            values = []

            for season in seasons:
                values.append(
                    self.df[season].get(team, 0)
                )

            plt.bar(
                seasons,
                values,
                bottom=bottom,
                label=team
            )

            bottom += np.array(values)

        plt.xlabel("Year")
        plt.ylabel("Number of Matches Won")
        plt.title("Number of Matches Won per Team per Year")

        plt.xticks(rotation=45)

        plt.legend(
            title="Team",
            bbox_to_anchor=(1.05, 1),
            loc="upper left"
        )

        plt.tight_layout()
        plt.show()

    def exc(self,m_rows):
        ans = self.team_season_wins(m_rows)
        self.plot()
        return ans