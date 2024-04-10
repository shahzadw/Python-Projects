number_counter = 0 #this variable is used to store the count of the number of numbers which starts at 0
total = 0 #this variable is used to store running total
number =float(input("please enter a number: ")) #i have used float here to allow the user flexibility to add decimal based numbers if they so wish
while number != -1:
    number_counter +=1
    total += number
    number =float(input("please enter a number: "))
if number_counter == 0:
    number_counter = 1 #i have assigned a value of 1 to the number counter for when it is 0 to avoide math error i.e. division by 0
average_of_numbers_bar_neg_1 =total/number_counter
print (average_of_numbers_bar_neg_1)






    
