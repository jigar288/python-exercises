from random import randint

###PRINT RANDOM FRUITS

#
#
def pf(choices):
    return (choices[randint(0, len(choices) - 1)])

### printing out random items of an array using a external function(pf) from above

# fruits = ["apple", "orange", "bananan", "pear", "kiwi" ]
# print pf(fruits)


### PASSWORD GENERATOR WITH 8 CHARACTERS

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

def password(letters):
    print "%s%s%s%s%s%s%s%s" % (pf(letters), pf(letters),pf(letters),pf(letters),pf(letters),pf(letters),pf(letters),pf(letters))

password(letters)
#




### Addition calculator

# def ps(number1, number2):
#     print number1 + number2
#
# ps(5, 5)

###printing random items with %s out of an array

# tasks = ["homework", "basketball practice", "cardio", "presentation", "work"]
# execues = ["because I overslept", "because I had friends over", "because I went to the movies"]
#
# print "I didn't do my %s %s"  % (tasks[randint(0, len(tasks) - 1)], execues[randint(0, len(execues) - 1)])


###printing out a sentence with %s based on raw_input

#name = raw_input('Enter your name: ');
#cssiYear = raw_input('What is the current year?: ')
#language = raw_input('What language are you learning?: ')
#university = raw_input('What university are you attending next year?: ')


#print "Hello %s, nice to meet you. You are attending the %s CSSI session. Currently you're learning %s. Next year you will be attending %s" % (
#name, cssiYear, language, university)
