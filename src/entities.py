import random

class Player:

    class Role:
        PLAYER = 0
        DEALER = 1

    MAX_LIVES_MAP = [2, 4, 6]

    def __init__(self, role: Role):
        self.role = role
        self.name = "PLAYER" if role == Player.Role.PLAYER else "DEALER"
        self.opponent = None
        self.lives = 3
        self.skip_next_turn = False


class Shotgun:

    ROUNDS = [
        [2, 4],
        [3, 5],
        [6, 8],
    ]

    def __init__(self):
        self.shells = None
        self.damage = 1

    def load_shells(self, round: int):
        self.num_shells = random.randint(self.ROUNDS[round][0], self.ROUNDS[round][1])
        self.shells = [1] * (self.num_shells // 2) + [0] * (self.num_shells // 2)
        random.shuffle(self.shells)

    def get_shell_display(self):
        sorted_shells = sorted(self.shells, reverse=True)
        rounds = " ".join("X" if shell == 1 else "-" for shell in sorted_shells)
        return f"[ {rounds} ]"
    
    def rack(self):
        self.shells.pop(0)

    def check_chamber(self):
        return "[ X ]" if self.shells[0] == 1 else "[ - ]"