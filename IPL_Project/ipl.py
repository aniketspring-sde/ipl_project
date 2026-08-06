from main.src.fetch_data import FetchData
from main.src.q1 import Q1
from main.src.q2 import Q2
from main.src.q3 import Q3
from main.src.q4 import Q4
from main.src.q5 import Q5
from main.src.q6 import Q6
from main.src.q7 import Q7
from main.src.q8 import Q8


def main():
    fetch_data = FetchData()

    deliveries = fetch_data.fetch_deliveries()
    matches = fetch_data.fetch_matches()



    Q1().exc(deliveries)
    Q2().exc(deliveries)
    Q3().exc()
    Q4().exc(matches)
    Q5().exc( matches)
    Q6().exc(matches)
    Q7().exc(matches, deliveries)
    Q8().exc(deliveries, matches)

if __name__ == "__main__":
    main()