class Tennis(object):
    def __init__(self, first_player_name, second_player_name):
        self.second_player_name = second_player_name
        self.first_player_name = first_player_name
        self.second_player_score_times = 0
        self.score_lookup = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }
        self.first_player_score_times = 0

    def score(self):
        if self.is_deuce():
            return "deuce"
        if self.is_score_same():
            return self.all_score()
        if self.is_adv():
            return self.adv_score()
        if self.is_win():
            return self.win_score()
        return self.lookup_score()

    def lookup_score(self):
        return f"{self.score_lookup[self.first_player_score_times]} {self.score_lookup[self.second_player_score_times]}"

    def is_adv(self):
        return self.is_ready() and abs(self.first_player_score_times - self.second_player_score_times) == 1

    def is_win(self):
        return self.is_ready() and abs(self.first_player_score_times - self.second_player_score_times) == 2

    def is_ready(self):
        return self.first_player_score_times > 3 or self.second_player_score_times > 3

    def win_score(self):
        return f"{self.adv_player()} Win"

    def adv_score(self):
        return f"{self.adv_player()} Adv"

    def adv_player(self):
        return self.first_player_name if self.first_player_score_times > self.second_player_score_times else self.second_player_name

    def is_deuce(self):
        return self.is_score_same() and self.first_player_score_times >= 3

    def all_score(self):
        return f"{self.score_lookup[self.first_player_score_times]} all"

    def is_score_same(self):
        return self.first_player_score_times == self.second_player_score_times

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1
