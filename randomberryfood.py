import random
import berrydict


berries = []
berrydict = berrydict.getberrydict()

for each in berrydict:
	berries.append(each.get('berry'))
	
berrychoice = random.choice(berries)
berrychoicename = list(berrychoice)
firstletter = berrychoicename[0]
firstletter = firstletter.upper()
endingletters = berrychoicename[1:]
endingletters = ''.join(endingletters)
endingletters = endingletters.lower()
berrychoicename = firstletter + endingletters
berrychoicename = berrychoicename
	
dishes = ['Pie', 'Barbacue', 'Chicken', 'Cake', 'Steak', 'Pork']
dishchoice = random.choice(dishes)
	
foodname = f'{berrychoicename} Berry {dishchoice}'

print(foodname)
