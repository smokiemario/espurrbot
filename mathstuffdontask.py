import math
import fractions

# problem = input('What would you like to find the integral of? ')
problem = '9x^4*2'


def simpleintegral(problem):
    sections = []
    constants = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '/', '.', '(', ')']

    problem = problem.replace('-','+-')
    problem = problem.replace(' ', '')
    additionsections = problem.split('+')
    print(additionsections)

    for section in additionsections:

        problemfixed = section.replace('/', '*/')
        problemparts = section.split('*')

        problemparts2 = []

        print(problemparts)

        # get all the multiplication stuff
        for part in problemparts:

            a = False

            if 'cos' in part:
                print("COS FOUND")
                a = section.find('cos')
                print(a)

            elif 'sin' in part:
                print("Sin FOUND")
                a = section.find('sin')
                print(a)


            elif 'x' in part:
                a = section.find('x')


            if a:
                firstpart = ''
                endpart = ''
                for each in part[:a]:
                    firstpart = firstpart + each
                for each in part[a:]:
                    endpart = endpart + each

                if firstpart != '':
                    firstpart = firstpart.replace('(', '')
                    firstpart = firstpart.replace(')', '')
                    problemparts2.append(firstpart)
                problemparts2.append(endpart)
            else:
                problemparts2.append(part)

        print('Problemparts2')
        print(problemparts2)

        # prep

        constant = 1
        tomultiply = []
        for each in problemparts2:
            constantcheck = True
            for char in each:
                if char not in constants:
                    constantcheck = False
            if constantcheck == True:
                tomultiply.append(each)
                problemparts2.remove(each)

        if len(tomultiply) > 0:
            for each in tomultiply:
                constant = constant * fractions.Fraction(each)

        print(tomultiply)
        print(constant)

        # integrate

        if problemparts2 == []:
            problemparts2 = ['x']
            print("MEOW")
        else:

            for each in problemparts2:
                print(each)
                print("a")

                if 'sin' in each:
                    a = each.find('sin')
                    each = each.replace('sin', 'cos')
                    problemparts2[a] = each
                    constant = constant / -1

                if 'cos' in each:
                    a = each.find('cos')
                    each = each.replace('cos', 'sin')
                    problemparts2[a] = each

                elif 'x^' in each:
                    a = each.find('x^')
                    power = each.replace('x^', '')
                    power = fractions.Fraction(power) + 1
                    power = math.trunc(power)
                    print(power)
                    problemparts2[a] = 'x^' + str(power)
                    constant = fractions.Fraction(constant) / fractions.Fraction(power)

                elif 'x' in each:
                    a = each.find('x')
                    problemparts2[a] = 'x^2'
                    constant = fractions.Fraction(constant) / 2






        print(constant)
        print(problemparts2)


        #create solution part

        constantanswer = fractions.Fraction(constant).limit_denominator()

        if '/' in str(constantanswer):
            constantanswer = f'({constantanswer})'

        answer = constantanswer

        for each in problemparts2:
            answer = str(answer) + each



        sections.append(answer)

    # combine solution parts

    finalanswer = ''
    finalanswer = ' + '.join(sections)
    finalanswer = finalanswer + ' + C'

    return finalanswer


