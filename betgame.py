import random as rd
"""
Eu pretendia usar numpy.random pra gerar os aleatórios, mas não tinha certeza de como 
fazer e a documentação do numpy (scipy) estava offline, aí não tive como conferir. 
Procurei algumas coisas no StackOverflow, mas tudo que encontrei linkava pra 
documentação oficial do scipy.
"""

def play_round(rolls, score, floor, round_update, roll_update):
    step = 0

    for j in range(0, rolls):
        if rd.randint(0, 1000) == 1:
            step = 0

        roll = rd.randint(1, 6)

        if step < 0:
            step = 0

        if(roll == 6):
            roll = rd.randint(1, 6)
            step += roll

            if roll_update == 'y':
                print('You rolled a 6! You earned a bonus roll!\nBONUS ROLL: You rolled a ' + str(roll) + ' and advanced ' + str(roll) + ' steps! You are now on floor ' + str(step+floor))
                
        elif roll == 1 or roll == 2:
            if roll_update == 'y':
                print('You rolled a ' + str(roll) + ' and decreased 1 step! You are now on floor ' + str(step+floor))
            step -= 1

        else:
            if roll_update == 'y':
         	   print('You rolled a ' + str(roll) + ' and increased 1 step! You are now on floor ' + str(step+floor))
            step += 1

    score.append(step)

    if round_update == 'y':
        print ("You advanced " + str(step) + " steps and got to floor " + str(step + floor) + "!\n")

rounds = int(input('How many rounds would you like to play?\n'))
rolls = int(input('How many times will you roll the dice a round?\n'))
floor = int(input('In which floor are you going to start playing?\n'))

round_update = 'f'
roll_update = 'f'

while(round_update != 'y' and round_update != 'n'):
    round_update = input('Would you like to see updates for each round? [y/n]\n')

while(roll_update != 'y' and roll_update != 'n'):
    roll_update = input('Would you like to see updates for each roll? [y/n]\n')

score = list()
rd.seed()

for i in range(0, rounds):
  play_round(rolls, score, floor, round_update, roll_update)

print ("\n\n!!!BEST ROUND!!!\nIn your best round you advanced " + str(max(score)) + " steps, which led you to floor " + str(max(score) + floor))