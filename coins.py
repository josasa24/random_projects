# Calculates minimum number of coins needed to make a given amount

coins = [1, 5, 10, 25]

def coin_converter(coins, amount):
    start_amount = amount
    coins.sort(reverse=True)
    total_coins = 0

    if amount < 0:
        raise ValueError("Please enter an amount that is greater than or equal to zero.")
    for coin in coins:
        while amount >= coin:
            total_coins += 1
            amount -= coin
    return print(f"You need {total_coins} coins to make {start_amount}.")

coin_converter(coins, 24)