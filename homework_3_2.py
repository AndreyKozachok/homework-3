import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return []
    if max > 1000:
        return []
    if min > max:
        return []
    if quantity > max - min:
        return []
    s = set()
    while len(s) < quantity:
        x = random.randrange(min, max)
        s.add(x)
        print(s, x)
    return sorted(s)
get_numbers_ticket(5, 20, 10)








