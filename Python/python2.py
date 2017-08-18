from random import randint



###(prints groceries in a array with indexes)
# groceries = ['basketball', 'banana', 'apple', 'milk', 'milk' ]
#
# for index in range(len(groceries)):
#     print "%s %s" % (index + 1, groceries[index] )



###(get input from the user four times for groceries)

# for i in range(4):
#   answer = raw_input("what groceries?")


###(asks users for input and print it out)
# items = []
#
# num = raw_input("how many items do you want to add?")

# for index in range(int(num)):
#     answer = raw_input("Which groceries do you want to add?")
#     items.append(answer)
# print item

###(asks user for input of specific amount of groceries, specific groceries items, and a specific quantity of items.Then prints it)

#
# groceries = []
#
# num = raw_input("how many items do you want to add?")
#
# for i in range(int(num)):
#     answer = raw_input("Which groceries do you want to add?")
#     quantity = raw_input("What quantity?")
#     final = answer + " " + quantity + " in quantity"
#     groceries.append(final)
#
#
# for index in range(len(groceries)):
#     print "%s. %s" % (index+1, groceries[index])


###(asks user for input but doesnt print right away, restricts milk with if statement, and prints indexes)
# groceries = []
#
# for i in range(4):
#     item = raw_input("Which groceries do you want to add?")
#     groceries.append(item)
#     if item == "milk":
#         print "milk is dumb"
#         print "!!!"
#
#
# for index in range(len(groceries)):
#     print "%s. %s" % (index+1, groceries[index])


###((write a program to play a simple number game, it picks a random number, if its wrong it tells you bigger or smaller))

###(using a for loop)
# random_number = randint(0,5)
#
# for i in range(5):
#     answer = int(raw_input("pick a number:"))
#     if answer == random_number:
#         print "correct"
#     if answer > random_number:
#         print "number is too big"
#     if answer < random_number:
#         print "number is too small"

###(using a while loop)
# won = False
#
# random_number = randint(0,10)
#
# while won == False:
#     answer = int(raw_input("pick a number:"))
#     if answer == random_number:
#         print "correct"
#         won = True
#     elif answer > random_number:
#         print "number is too big"
#         won = False
#     elif answer < random_number:
#         print "number is too small"
#         won = False


#get alphabet code from harsh
