import math
import random
#task 1
print("Hello")
Name = input("What is your name?")
print ( "Hello,",Name)
#task 2
Circle = float(input( 'Please enter your favorite circle size (radius):'))
print ( "Circumference", 2 * Circle * math.pi )
#task 3
Rectangle = input( 'Please enter your favorite rectangle size (width,height):')
a = Rectangle.split()
x, y = map(float,a )
print ( "Perimeter =",(x+y)*2 )
print ( "Area =",x * y )
#task 4
numbers = input( 'Please enter your favorite numbers (3 numbers):')
num = numbers.split()
s1, s2, s3 = map(int, num )
sum = s1 + s2 + s3
product = s1 * s2 * s3
average = sum/3
print (' Sum, product, and average:', sum, product, average )
#task 5
talent = float(input( 'Please enter your favorite talent:'))
pound  = float(input( 'Please enter your favorite pound:'))
lot    = float(input( 'Please enter your favorite lot:'))
ta = talent * 20
pa = ta + pound
la = pa * 32 + lot
grams = la * 13.3
print ("The weight in modern units:", int(grams/1000),"kilograms", "and",round (grams%1000, 2),"grams" )
#task 6
Helo = input( 'Would you like to have combinations of numbers for a combination lock ?')
if Helo == "yes":
    to_hop_1 = [0,1,2,3,4,5,6, 7, 8, 9]
    to_hop_2 = [1,2,3,4,5,6]
    random_1 = random.sample(to_hop_1, 3)
    random_2 = random.sample(to_hop_2, 4)
    print (random_1)
    print (random_2)