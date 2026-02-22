amount_due = 50
insert_coin = 0

print("Amount due: 50 cents")
while amount_due > 0:
    while True:
        insert_coin = int(input("Insert coin (5, 10, 25): "))
        if insert_coin not in [5, 10, 25]:
            print("Invalid coin. Please insert 5, 10, or 25 cents.")
            continue
        else:
            break
    amount_due -= insert_coin
    print(f"Inserted Coin: {insert_coin}")
    if amount_due > 0:
        print(f"Amount due: {amount_due}")

print("Change Owned: 0")