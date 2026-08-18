from matplotlib import pyplot as plt


UMPIRE_COUNTRY_DATA = {
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


def calculate():
    umpire_country = {}

    for umpire, country in UMPIRE_COUNTRY_DATA.items():
        if country == "India":
            continue
        if country not in umpire_country:
            umpire_country[country] = 0

        umpire_country[country] += 1

    return umpire_country


def plot(umpire_country):
    plt.figure(figsize=(10, 5))

    plt.bar(umpire_country.keys(), umpire_country.values())

    plt.xticks(rotation=90)
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.title("Number of Umpires by Country")

    plt.tight_layout()

    plt.savefig("../plots/q3_Foreign_umpire_analysis.png")
    plt.show()


def execute():
    umpire_country = calculate()
    plot(umpire_country)

    return umpire_country


execute()