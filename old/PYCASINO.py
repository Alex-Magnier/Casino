import casino.old.flip_coin as flip_coin

coin :float = 100.00
print("Welcome to the PYCASINO !")
username :str = input("Please enter your username: ")

def clear ():
    for i in range (50):
        print("\n")

def main_menu(coin, username):
    clear()
    print(f" username: {username}")
    print(f" coins : {coin}")
    print("  _________________________________________________________")
    print(" | Select game                                             |")
    print(" | 1. Blackjack                                            |")
    print(" | 2. Flip Coin                                            |")
    print(" | 3. ?????????                                            |")
    print(" | 4. ?????????                                            |")
    print(" | 5. ?????????                                            |")
    print(" |_________________________________________________________|\n")
    game_id = int(input("Select a game by it's own ID: "))

    if game_id == 1:
        pass
    elif game_id == 2:
        coin += flip_coin.flip_coin_game(coin, username)
        play = input("auto break -- press enter: ")


    return coin

while True:
    coin = main_menu(coin, username)