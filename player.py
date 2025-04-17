class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.position = 0
        self.double_counter = 0
        # self.in_jail = False

    def __str__(self):
        return f"Player {self.name} with symbol {self.symbol}"