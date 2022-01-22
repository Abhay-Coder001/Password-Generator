#import random for random numbers
import random
#Write all the keys which we can randomly choose to make our password
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "1234567890"
Symbol = "@#$%^&*()_+|"
#For strong password we need some lower and upper case letter some number or some symbols within length 9
all = lower + upper + NUMBER + Symbol
length = 9
password = "".join(random.sample(all,length))
print("The Password You Generated is :  ",password)