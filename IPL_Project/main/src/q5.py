from matplotlib import pyplot as plt


class Q5():
    def __init__(self):
        self.matches = {}


    def match(self,m_rows):


        for row in m_rows:

            if row['season'] in self.matches:
                self.matches[row['season']] += 1
            else:
                self.matches[row['season']] = 1

        return  self.matches

    def plot(self):
        plt.figure(figsize=(10, 5))

        plt.bar(self.matches.keys(), self.matches.values())

        plt.xticks(list(self.matches.keys()), rotation=90)

        plt.show()

    def exc(self, m_rows):
        ans = self.match(m_rows)
        self.plot()
        return ans