from src.state import GameState

if __name__ == "__main__":

    print("===========================")
    print("     BUCKSHOT ROULETTE    ")
    print("  Created by Andrew Mrak  ")
    print("     and Josiah Bergen    ")
    print("===========================")

    debug = input("\nPress Enter to begin. ")
    game = GameState(debug=True if debug == "d" else False)
    game.new_game()
