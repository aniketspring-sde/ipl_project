from matplotlib import pyplot as plt


class Q2():
    def __init__(self):
        self.rcb={}

    def batsman_rcb(self,d_rows):



        for row in d_rows:
            if(row['batting_team'] == 'Royal Challengers Bangalore'):
                if row['batsman'] in self.rcb:
                    self.rcb[row['batsman']] += int(row['batsman_runs'])
                else:
                    self.rcb[row['batsman']] = 0

        self.rcb[row['batsman']] += int(row['batsman_runs'])
        rcb_f = dict(sorted(self.rcb.items(), key=lambda x: x[1], reverse=True))
        self.rcb = dict(list(rcb_f.items())[:10])


    def plot(self):
        plt.figure(figsize=(10, 5))

        plt.bar(self.rcb.keys(), self.rcb.values())

        plt.xticks(list(self.rcb.keys()), rotation=90)

        plt.show()

    def exc(self,d_rows):
        self.batsman_rcb(d_rows)
        self.plot()
