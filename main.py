#Store number variables for the two numbers
print("Kalkulejtor")
num1 = input('liczba 1: ')
num2 = input('liczba 2: ')

#the sum of the two numbers variable
sum = float(num1) + float(num2)
sum2 = float(num1) - float(num2)
sum3 = float(num1) * float(num2)
sum4 = float(num1) / float(num2)

#what operator to use
choice = input('wybierz, + = dodawanie, - = odejmowanie, * = mnożenie and / = dzielenie: ')
#different sums based on the operators
if choice == '+':
  print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

if choice == '-':
  print('The sum of {0} and {1} is {2}'.format(num1, num2, sum2))

if choice == '*':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum3))

if choice == '/':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum4))