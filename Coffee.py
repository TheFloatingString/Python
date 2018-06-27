def coffeeType(quantity, quality, country):
    is_safe = True

    if country.lower() == 'antarctica':
        print("DO NOT CONSUME THIS COFFEE!!!")
        is_safe = False

    if quality.lower() == 'ketchup':
        print("MAXINE HAS WARNED YOU NOT TO DRINK THIS COFFEE....")
        print("But lAURENCE WOULD DRINK IT :D XD")
        is_safe = False

    for i in range(200):
        print("I LOVE COFFEE!!!")

    return is_safe