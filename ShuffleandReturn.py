import random
def randome(woord1, woord2, woord3, woord4):
    randomised1 = ''.join(random.sample(woord1, len(woord1)))
    randomised2 = ''.join(random.sample(woord2, len(woord2)))
    randomised3 = ''.join(random.sample(woord3, len(woord3)))
    randomised4 = ''.join(random.sample(woord4, len(woord4)))
    print(randomised1)
    print(woord1)
    print("")
    print(randomised2)
    print(woord2)
    print("")
    print(randomised3)
    print(woord3)
    print("")
    print(randomised4)
    print(woord4)
    print("")

randome("Ik", "zit", "op", "voetbal")