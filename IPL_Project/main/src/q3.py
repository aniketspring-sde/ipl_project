from matplotlib import pyplot as plt


class Q3:
    def __init__(self):
        self.umpire_country_data = {
                                    "Aleem Dar": "Pakistan",
                                    "Asad Rauf": "Pakistan",
                                    "Kumar Dharmasena": "Sri Lanka",
                                    "Rod Tucker": "Australia",
                                    "Richard Illingworth": "England",
                                    "Marais Erasmus": "South Africa",
                                    "Nigel Llong": "England",
                                    "Bruce Oxenford": "Australia",
                                    "Simon Taufel": "Australia",
                                    "Chris Gaffaney": "New Zealand",
                                    "Paul Reiffel": "Australia",
                                    "S Ravi": "India",
                                    "C Shamshuddin": "India",
                                    "Anil Chaudhary": "India",
                                    "Nitin Menon": "India",
                                    "CK Nandan": "India",
                                    "AK Chaudhary": "India",
                                    "S Asnani": "India",
                                    "VA Kulkarni": "India",
                                    "BNJ Oxenford": "Australia",
                                    "HDPK Dharmasena": "Sri Lanka",
                                    "BF Bowden": "New Zealand",
                                    "RE Koertzen": "South Africa",
                                    "SJ Davis": "Australia",
                                    "M Erasmus": "South Africa",
                                    "RK Illingworth": "England",
                                    "NJ Llong": "England",
                                    "SD Fry": "Australia",
                                    "O Nandan": "India",
                                    "K Srinath": "India",
                                    "KN Ananthapadmanabhan": "India",
                                    "UV Gandhe": "India",
                                    "YC Barde": "India",
                                    "CB Gaffaney": "New Zealand",
                                    "A Nand Kishore": "India"
                                }
        self.ump_country = {}


    def umpire_country(self):
        for item in self.umpire_country_data.items():
            # if item[1] != 'India':
            #   if item[1] in self.ump_country:
            #     self.ump_country[item[1]] += 1
            #   else:
            #     self.ump_country[item[1]] = 1

            if item[1] in self.ump_country:
                self.ump_country[item[1]] += 1
            else:
                self.ump_country[item[1]] = 1



    def plot(self):
        plt.figure(figsize=(10, 5))

        plt.bar(self.ump_country.keys(), self.ump_country.values())

        plt.xticks(list(self.ump_country.keys()), rotation=90)

        plt.show()

    def exc(self):
        self.umpire_country()
        self.plot()



