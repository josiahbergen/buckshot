from src.entities import Player, Shotgun
from src.items import Item

class GameState:

    def __init__(self):
        self.player = Player(Player.Role.PLAYER)
        self.dealer = Player(Player.Role.DEALER)
        self.player.opponent = self.dealer
        self.dealer.opponent = self.player
        self.turn = self.player
        self.shotgun = Shotgun()
        self.round = 0

    def new_game(self):
        print("NEW GAME")
        self.turn = self.player

        self.player.lives = Player.MAX_LIVES_MAP[self.round]
        self.dealer.lives = Player.MAX_LIVES_MAP[self.round]

        for i in range(3):
            winner = self.play_round(i)
            if winner.role == Player.Role.DEALER:
                print("THE DEALER HAS WON THE GAME")
                return
        print("THE PLAYER HAS WON THE GAME")

    def play_round(self, round: int):
        print(f"Round {round} started.")
        self.round = round
        self.player.lives = Player.MAX_LIVES_MAP[self.round]
        self.dealer.lives = Player.MAX_LIVES_MAP[self.round]
        self.shotgun.load_shells(round)

        print(f"Shotgun: {self.shotgun.get_shell_display()}")

        while self.player.lives > 0 and self.dealer.lives > 0:

            if len(self.shotgun.shells) == 0:
                print("The shotgun is empty. Refilling...")
                self.shotgun.load_shells(round)
                print(f"Shotgun: {self.shotgun.get_shell_display()}")
                self.turn = self.player

            print(f"{self.turn.name}'s turn. Lives: {self.dealer.lives} - {self.player.lives}")
            self.play_turn()
            self.next_turn()
        
        winner = self.player if self.player.lives > 0 else self.dealer
        print(f"Round {round} ended. Winner: {winner.name}")
        return winner

    def play_turn(self):
        while True:
            move = self.get_valid_input("What would you like to do? (i)tem, (s)hotgun: ", ["i", "s"])
            if move == "i":
                self.use_item()
            elif move == "s":
                self.use_shotgun()
                break

    def use_item(self):
        item = self.get_valid_input("What item would you like to use? (b)eer, (c)igarettes, (h)andcuffs, hand(s)aw, (m)agnifying glass: ", ["b", "c", "h", "s", "m"])
        match item:
            case "b":
                self.shotgun.rack()
                print("The shotgun has been racked.")
            case "c":
                self.turn.lives = min(self.turn.lives + 1, Player.MAX_LIVES_MAP[self.round])
                print("You have regained 1 life.")
                print(f"Lives: {self.dealer.lives} - {self.player.lives}")
            case "h":
                self.turn.opponent.skip_next_turn = True
                print(f"{self.turn.opponent.name} will skip their next turn.")
            case "s":
                self.shotgun.damage = 2
                print("The shotgun will deal 2 damage this turn.")
            case "m":
                print(f"Checking the chamber: {self.shotgun.check_chamber()}")

    def use_shotgun(self):
        target = self.get_valid_input(f"Who would you like to shoot? (y)ourself, ({self.turn.opponent.name.lower()[:1]}){self.turn.opponent.name.lower()[1:]}: ", ["y", self.turn.opponent.name.lower()[:1]])
        if target == "y":
            self.shoot(self.turn)
        elif target == self.turn.opponent.name.lower()[:1]:
            self.shoot(self.turn.opponent)

    def shoot(self, target: Player):
        if self.shotgun.shells[0] == 0:
            print("Blank.")
            self.shotgun.rack()
            return
        print(f"BANG! The {target.name} has been shot.")
        target.lives -= self.shotgun.damage

        self.shotgun.damage = 1
        self.shotgun.rack()

    def next_turn(self):
        self.turn = self.turn.opponent
        if self.turn.skip_next_turn:
            print(f"{self.turn.name}'s turn is being skipped.")
            self.turn.skip_next_turn = False
            self.turn = self.turn.opponent
            return

    def get_valid_input(self, prompt: str, valid_options: list[str]):
        while True:
            move = input(prompt)
            if move in valid_options:
                return move
            else:
                print("Please enter a valid option.")
    

