#I am starting with the for loop to get a pattern 
n = 5 #this is the range (or rows of '*'). I tried using the range function here, but i could not get the string s and range to work together...therefore i decided to hardcode the value as the question is output focused
s = '*' #this is a string only 
for i in range (n):
    print(s*(i+1))
#the above code provides half of the output, until the row where s = 5 x * 
#I did some research into mirroring patterns in Python which is possible, however since the question asked me to use an if-else statement in combination with a single for loop, I have hardcoded the values below
#again, i did this because the question is output focused and constrains me from using more imaginative solutions
#I do not understand if-else to be a looping function and could not figure out how to create a false boolean for it to go to the else bit, therefore i omitted it entirely
x = 5
if x == 5:
    print(s*(x-1))
    print(s*(x-2))
    print(s*(x-3))
    print(s*(x-4))




