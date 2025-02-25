
bills = [200, 100, 50, 20, 10]
coins = [5, 2, 1, 0.5, 0.2, 0.1]

amount = float(input("Please enter the amount of money you want to break down: "))
print(f"{amount} soles are equivalent to:")

for bill in bills:
    if amount >= bill:
        bill_amount = amount // bill
        amount = amount % bill
        print(f"{int(bill_amount)} S/{bill} bills")

for coin in coins:
    if amount >= coin:
        coin_amount = amount // coin
        amount = round(amount % coin, 1)
        if coin >= 1:
            print(f"{int(coin_amount)} S/{coin} coins")
        else:
            print(f"{int(coin_amount)} S/{int(coin * 100)}-cents coins")    