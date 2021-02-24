import datetime
import random
import time


points = {}
player_1 = input("Player one: ")
player_2 = input("Player two: ")
points[player_1] = 0
points[player_2] = 0
rounds = int(input("Rounds: "))
while rounds % 2 != 0:
    print("Sorry, you have to give me an even number!")
    rounds = int(input("Rounds: "))
turn = random.randint(0, 1)
for r in range(0, rounds):
    if turn == 0:
        print("It's {}'s turn!".format(player_1))
    else:
        print("It's {}'s turn!".format(player_2))
    time.sleep(0.5)
    print("Get ready..")
    time.sleep(random.randint(1,12))
    then = datetime.datetime.now()
    t = input("GO!! ")
    now = datetime.datetime.now()
    diff = then-now
    reaction_time = round(abs(diff.total_seconds()), 2)
    if turn == 0:
        points[player_1] += reaction_time
        turn += 1
    else:
        points[player_2] += reaction_time
        turn -= 1
    print("Reaction time: {} seconds".format(reaction_time))
winner = min([points[player_1], points[player_2]])
print("The winner is..")
time.sleep(0.5)
print(player_1+"!")