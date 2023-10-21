# Define the base Player class
class Player:
    def play(self):
        print("The player is playing cricket")

# Define the Batsman class, derived from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting")

# Define the Bowler class, derived from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")


batsman = Batsman()
bowler = Bowler()


batsman.play()
bowler.play()
