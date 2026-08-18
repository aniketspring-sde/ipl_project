import unittest

from main.src.q5_for_test import calculate as calculate_q5
from main.src.q6_for_test import calculate as calculate_q6
from main.src.q7_for_test import calculate as calculate_q7
from main.src.q8_for_test import calculate as calculate_q8


class TestIPL(unittest.TestCase):

    deliveries_file = "tests/test_data/deliveries_test.csv"
    matches_file = "tests/test_data/matches_test.csv"

    def test_q5(self):
        expected_matches_per_season = {
            '2015': 2,
            '2016': 2,
            '2017': 1
        }

        result = calculate_q5(self.matches_file)

        self.assertEqual(
            result,
            expected_matches_per_season
        )

    def test_q6(self):
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

        result = calculate_q6(self.matches_file)

        self.assertEqual(
            result,
            expected_matches_won
        )

    def test_q7(self):
        expected_extra_runs = {
            'Mumbai Indians': 2,
            'Royal Challengers Bangalore': 1
        }

        result = calculate_q7(
            self.matches_file,
            self.deliveries_file
        )

        self.assertEqual(
            result,
            expected_extra_runs
        )

    def test_q8(self):
        expected_economy_rate = {
            'B': 12.0,
            'E': 18.0
        }

        result = calculate_q8(
            self.deliveries_file,
            self.matches_file
        )

        self.assertEqual(
            result,
            expected_economy_rate
        )


if __name__ == '__main__':
    unittest.main()


 # coverage run -m unittest t_ipl.py
# coverage report
# python -m unittest -v t_ipl.py