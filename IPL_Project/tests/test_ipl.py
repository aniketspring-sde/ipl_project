import unittest

from main.src.q5 import Q5
from main.src.q6 import Q6
from main.src.q7 import Q7
from main.src.q8 import Q8
from tests.test_fetch_data import TestFetchData


class TestIPL(unittest.TestCase):

    dt_rows = TestFetchData().fetch_deliveries_test()
    mt_rows = TestFetchData().fetch_matches_test()

    # def __init__(self, methodName: str = "runTest"):
    #     super().__init__(methodName)
    #     self.expected_matches_per_year = {}





    def test_one(self):
        self.expected_matches_per_year = {
            '2015': 2,
            '2016': 2,
            '2017': 1
        }
        q5 = Q5()

        self.assertEqual(q5.exc(self.mt_rows), self.expected_matches_per_year)
    def test_two(self):
        expected_matches_won = {
            '2015': {
                'Mumbai Indians': 1,
                'Royal Challengers Bangalore': 1
            },
            '2016': {
                'Kolkata Knight Riders': 1,
                'Sunrisers Hyderabad': 1
            },
            '2017': {
                'Rising Pune Supergiant': 1
            }
        }

        self.assertEqual(Q6().exc(self.mt_rows), expected_matches_won)

    def test_three(self):
        extra_runs_2016 = {
            'Mumbai Indians': 2,
            'Royal Challengers Bangalore': 1
        }

        self.assertEqual(Q7().exc(self.mt_rows,self.dt_rows), extra_runs_2016)

    def test_four(self):
        expected_economy_2015 = {
            'B': 12.0,
            'E': 18.0
        }

        self.assertEqual(Q8().exc(self.dt_rows,self.mt_rows), expected_economy_2015)





if __name__ == '__main__':
    unittest.main()