class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    @classmethod
    def get_player_count(cls):
        return cls.player_count

p1 = Player("Rahul345", 25)
p2 = Player("Harsh253", 99)
p3 = Player("Nisha001", 17)

print(Player.get_player_count())