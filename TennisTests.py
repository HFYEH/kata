import unittest

from Tennis import Tennis


class TennisTestCase(unittest.TestCase):
    def setUp(self):
        self.tennis = Tennis("Sharefun", "Tom")

    def test_love_all(self):
        self.score_should_be("love all")

    def test_fifteen_love(self):
        self.first_player_score_times(1)
        self.score_should_be("fifteen love")

    def test_thirty_love(self):
        self.first_player_score_times(2)
        self.score_should_be("thirty love")

    def test_forty_love(self):
        self.first_player_score_times(3)
        self.score_should_be("forty love")

    def test_love_fifteen(self):
        self.second_player_score_times(1)
        self.score_should_be("love fifteen")

    def test_love_thirty(self):
        self.second_player_score_times(2)
        self.score_should_be("love thirty")

    def test_love_forty(self):
        self.second_player_score_times(3)
        self.score_should_be("love forty")

    def test_fifteen_all(self):
        self.first_player_score_times(1)
        self.second_player_score_times(1)
        self.score_should_be("fifteen all")

    def test_thirty_all(self):
        self.first_player_score_times(2)
        self.second_player_score_times(2)
        self.score_should_be("thirty all")

    def test_deuce(self):
        self.given_deuce()
        self.score_should_be("deuce")

    def test_first_player_adv(self):
        self.given_deuce()
        self.first_player_score_times(1)
        self.score_should_be("Sharefun Adv")

    def test_second_player_adv(self):
        self.given_deuce()
        self.second_player_score_times(1)
        self.score_should_be("Tom Adv")

    def test_second_player_win(self):
        self.given_deuce()
        self.second_player_score_times(2)
        self.score_should_be("Tom Win")

    def given_deuce(self):
        self.first_player_score_times(3)
        self.second_player_score_times(3)

    def second_player_score_times(self, times):
        for i in range(times):
            self.tennis.second_player_score()

    def first_player_score_times(self, times):
        for i in range(times):
            self.tennis.first_player_score()

    def score_should_be(self, expected):
        self.assertEqual(expected, self.tennis.score())


if __name__ == '__main__':
    unittest.main()
