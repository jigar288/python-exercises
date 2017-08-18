arr = [2, 6, 3, 8, 4]

arr[0]

emoji_dic = {
':)': 'happy',
'<3': 'heart',
':(': 'unhappy',
'lol': 'laughing out loud'

}

#ask for an emoji to define
#print out the def if matched
#print out none if not matched

ask = raw_input("What do you want to look up?")

if ask in emoji_dic:
    print emoji_dic[ask]
else:
    print "emoji not available"
#
# print emoji_dic['<3']
# print "checking for <3"
# print '<3' in emoji_dic
# print "checking for :p"
# print ':p' in emoji_dic
