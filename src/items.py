from src.state import Player

class Item:

    class Type:
        BEER = (0, "BEER", "RACKS THE SHOTGUN. EJECTS CURRENT SHELL.")
        CIGARETTES = (1, "CIGARETTE PACK", "TAKES THE EDGE OFF. REGAIN 1 CHARGE.")
        HANDCUFFS = (2, "HANDCUFFS", "OPPONENT SKIPS THE NEXT TURN.")
        HANDSAW = (3, "HAND SAW", "SHOTGUN DEALS 2 DAMAGE.")
        MAGNIFYING_GLASS = (4, "MAGNIFYING GLASS", "CHECK THE CURRENT ROUND IN THE CHAMBER.")

    def __init__(self, owner: Player):
        self.name = None
        self.description = None
        self.owner = owner
        self.type = None

    def play(self):
        print(f"{self.owner.name} has played a card: {self.name}.")
