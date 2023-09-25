class Player:
  def Play(self):
      print("The Player is Playing football.")
    
class fielder(Player):
    def Play(self):
        print("The feilder is       fielding.")
        
class defender(Player):
  
    def Play(self):
        print("The defender is defending.")
                 
fielder = fielder()
defender =defender()


fielder.Play()
defender.Play()