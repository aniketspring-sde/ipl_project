class Q4:
    def __init__(self):
        self.df ={}

    def team_season_match(self,m_rows):





        for row in m_rows:

            if row['season'] in self.df:

                if row['team1'] in self.df[row['season']]:
                    self.df[row['season']][row['team1']] += 1
                else:
                    self.df[row['season']][row['team1']] = 1

                if row['team2'] in self.df[row['season']]:
                    self.df[row['season']][row['team2']] += 1
                else:
                    self.df[row['season']][row['team2']] = 1



            else:

                self.df[row['season']] = {}

                if row['team1'] in self.df[row['season']]:
                    self.df[row['season']][row['team1']] += 1
                else:
                    self.df[row['season']][row['team1']] = 1

                if row['team2'] in self.df[row['season']]:
                    self.df[row['season']][row['team2']] += 1
                else:
                    self.df[row['season']][row['team2']] = 1




    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np

        seasons = sorted(self.df.keys())

        teams = set()

        for season in self.df:
            teams.update(self.df[season].keys())

        teams = sorted(teams)

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

        plt.xlabel("Season")
        plt.ylabel("Number of Matches")
        plt.title("Matches Played by Each Team in Each Season")

        plt.xticks(rotation=45)

        plt.legend(
            bbox_to_anchor=(1.05, 1),
            loc="upper left"
        )

        plt.tight_layout()
        plt.show()

    def exc(self,m_rows):
        ans = self.team_season_match(m_rows)
        self.plot()
        return ans