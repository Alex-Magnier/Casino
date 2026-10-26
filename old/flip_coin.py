import casino.old.coin_gestion as coin_gestion
import random as rd

def flip_coin_game (coin :float, username :str):
    bet = float(input("How much coin do you want to bet: "))
    if coin_gestion.is_enougth_coin(coin, bet) == False:
        print("Bet to high, not enought coins")
        return coin
    is_win = rd.randint(0,1)
    if is_win == 0:
        print(f'{username} won {bet*2} coins !')
        return round(bet, 2)
    else:
        print(f'{username} loose {bet} coins :/')
        return -bet