class GameResult:
    def __init__(self, solved, strikes, balls):
        self.__balls = balls
        self.__strikes = strikes
        self.__solved = solved

    def get_solved(self):
        return self.__solved

    def get_strikes(self):
        return self.__strikes

    def get_balls(self):
        return self.__balls

