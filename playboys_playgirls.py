#game heads or tails 
# create a game where a player randomly chooses ++++
# create a seperate list with names of players and their scores should be assigned to the list after the game 
# then this leaderboard has to be created in the descending order like a real leaderboard
import random 
import csv

player_1  = 0
player_2 = 0
player_3 = 0
player_4 = 0
player_5 = 0
counter = 0 
while counter < 10:
    x = random.randint(1,2)
    y = random.randint(1,2)
    if x == y:
        player_1 += 1
        counter = counter + 1
    else:
            counter = counter + 1 

while counter < 20:
    x = random.randint(1,2)
    y = random.randint(1,2)
    if x == y:
        player_2 += 1
        counter = counter + 1
    else:
            counter = counter + 1 

while counter < 30:
    x = random.randint(1,2)
    y = random.randint(1,2)
    if x == y:
        player_3 += 1
        counter = counter + 1
    else:
            counter = counter + 1 

while counter < 40:
    x = random.randint(1,2)
    y = random.randint(1,2)
    if x == y:
        player_4 += 1
        counter = counter + 1
    else:
            counter = counter + 1 

while counter < 50:
    x = random.randint(1,2)
    y = random.randint(1,2)
    if x == y:
        player_5 += 1
        counter = counter + 1
    else:
            counter = counter + 1 
list_of_players = [{"first_name":"Karl","last_name":player_1},
                   {"first_name":"Eren","last_name":player_2},
                   {"first_name":"John","last_name":player_3},
                   {"first_name":"Huel","last_name":player_4},
                   {"first_name":"Karin","last_name":player_5}
] 
with open('playboys_playgirls.csv', mode='w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'score'])
    scoreboard = list_of_players[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=scoreboard)
    for row in list_of_players:
        writer.writerow(row)

