def snack_game(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif 11 in [a, b, c] and a + b + c <= 31:
        return a + b + c - 10
    else:
        return "too much(BUST)"
print(snack_game(5, 6, 7))
print(snack_game(9, 9, 9))
print(snack_game(11, 9, 9))