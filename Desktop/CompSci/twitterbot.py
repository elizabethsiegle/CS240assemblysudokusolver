import random

possibleKings = ['king', 'queen', 'Elvis impersonator']
possibleVerbs = ['dead', 'sleeping', 'dying', 'singing']

king = random.choice(possibleKings)
dead = random.choice(possibleVerbs)

print 'The ' + king + ' is ' + dead + '. Long live the ' + king + '.'

