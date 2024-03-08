import random
import berrydict

print('')
print('')

berrydict = berrydict.getberrydict()

questiontypes = ['info', 'color', 'type']

questiontype = random.choice(questiontypes)

if questiontype == 'info':
	
	answerchoices = []
	correctanswer = random.choice(berrydict)
	answerchoices.append(correctanswer.get('berry'))
	
	info = ['info1', 'info2', 'info3']
	information = correctanswer.get(random.choice(info))
	
	
	
	while len(answerchoices) < 5:
		answerchoice = random.choice(berrydict)
		answerchoice = answerchoice.get('berry')
		if answerchoice not in answerchoices:
			answerchoices.append(answerchoice)
	random.shuffle(answerchoices)
	
	
	print(f'''What berry does this description refer to?
{information}
Answer choices: {answerchoices[0]}, {answerchoices[1]}, {answerchoices[2]}, {answerchoices[3]}, or {answerchoices[4]}''')
		
		
elif questiontype == 'color':
	answerchoices = []
	correctanswer = random.choice(berrydict)
	color = correctanswer.get('color')
	
	answerchoices.append(correctanswer.get('berry'))
	
	while len(answerchoices) < 5:
		answerchoice = random.choice(berrydict)
		answerchoicename = answerchoice.get('berry')
		answercolor = answerchoice.get('color')
		if answerchoicename not in answerchoices and answercolor != color:
			answerchoices.append(answerchoicename)
	random.shuffle(answerchoices)
	
	
	print(f'''Which of these berries are {color}:
Answer choices: {answerchoices[0]}, {answerchoices[1]}, {answerchoices[2]}, {answerchoices[3]}, or {answerchoices[4]}''')
		
		
		
elif questiontype == 'type':
	answerchoices = []
	correctanswer = random.choice(berrydict)
	type = correctanswer.get('type')
	
	answerchoices.append(correctanswer.get('berry'))
	
	while len(answerchoices) < 5:
		answerchoice = random.choice(berrydict)
		answerchoicename = answerchoice.get('berry')
		answertype = answerchoice.get('type')
		if answerchoicename not in answerchoices and answertype != type:
			answerchoices.append(answerchoicename)
	random.shuffle(answerchoices)
	
	
	print(f'''Which of these berries are associated with the type "{type}":
Answer choices: {answerchoices[0]}, {answerchoices[1]}, {answerchoices[2]}, {answerchoices[3]}, or {answerchoices[4]}''')
		
		
		
		
		
		
			
answer = input('Your answer?: ')
correctanswer = correctanswer.get('berry')
if answer.lower() == correctanswer:
	print('correct!') 
else:
	print('incorrect')
	print(f'The correct answer was {correctanswer}')
		
	
