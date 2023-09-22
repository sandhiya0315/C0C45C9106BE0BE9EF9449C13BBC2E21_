class player:
    def play(self):
      print("the player is playing cricket")
    
class batsman(player):
    def play(self):
      print("the batsman is batting")
        
class bowler(Player):
    def play(self):
      print("the bolwer is bowling")
        
batsman=batsman()
bowler=bowler()

batsman.play()
bowler.play()
