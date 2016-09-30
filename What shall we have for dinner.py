#! /usr/bin/env python3

#What's for dinner?

import random
import time

dinnerList = [
'Makhani Curry',
'Tacos',
'Burritos',
'Burgers',
'Hotdogs',
'Pesto Pasta',
'Bruschetta',
'Pizza',
'Hummous',
'Indiannnnn',
'Egg fried rice',
'Something Vietnamese',
'SUUUSHIIIIII!!!',
'Blowtorched-Cheese Topped Sushi',
'Avocado on Toast',
'Lasagne',
'Macaroni Cheese',
'Apple Pie',
'Fiorentina Pizza',
'Dumplings',
'That fried burger \'meat\' + grilled chilli sandwich that Mark Weins ate in Turkey',
'Brownies',
'Enchilladas! With quorn mince and baked beans and cheese and jalapenos etc.',
'Quesodillas',
'Bake a loaf',
'Pho',
'Roast Dinz',
'Soup',
'Summer Rolls',
'Stir Fry',
'EGGGGGGG SANDWICHHHHH',
'Nachos with guacamole!'
]

talkList = [
'How aboutttt...',
'Consider this:',
'What about...',
'Let\'s think about...',
'What about...',
'I fancy...',
'OMGGGG!!!!',
'I\'m in the mood for',
'You\'re thinking about',
'Let\'s haveeeee...',
'Tell you what sounds good...'
]

def mainMenu():
    mainMenuChoice = ''
    while mainMenuChoice != '1' or mainMenuChoice != '2':
        mainMenuChoice = input('1) Dinner Suggestions \n2) Edit Dinner List\n')
        if mainMenuChoice == '1':
            dinnerSuggester()
        elif mainMenuChoice == '2':
            listEditMenu()

def listEditMenu():
    listOptions = ''
    while listOptions != '1' or listOptions != '2' or listOptions != '3' or listOptions != '4':
        listOptions = input('1) Add Food Item \n2) Delete Food Item \n3) View Food List \n4) Back\n')
        if listOptions == '1':
            foodItem  = input('Food Name: ')
            dinnerList.append(foodItem)
            print(foodItem + ' added to food list.\n')
            time.sleep(1)
        if listOptions == '2':
            foodItem  = input('Delete Food Name: ')
            if foodItem in dinnerList:
                dinnerList.remove(foodItem)
                print(foodItem + ' removed from food list.\n')
                time.sleep(1)
            else: print('Could not find ' + foodItem + ' in food list :(\n')
        if listOptions == '3':
            for i in dinnerList:
                print(i)
            print('**END OF LIST**\n\n')
        if listOptions == '4':
            mainMenu()
            

        

    

def dinnerSuggester():
    input('Press enter to get a meal suggestion!\n')
    randomFoodIndex = random.randint(0, (len(dinnerList) - 1))
    randomTalkIndex = random.randint(0, (len(talkList) - 1))
    print(str(talkList[randomTalkIndex]) + ' ' + str(dinnerList[randomFoodIndex]) + '! \n')
    while True:
        time.sleep(1)
        input('Press enter try again...\n')
        randomFoodIndex = random.randint(0, (len(dinnerList) - 1))
        randomTalkIndex = random.randint(0, (len(talkList) - 1))
        print(str(talkList[randomTalkIndex]) + ' ' + str(dinnerList[randomFoodIndex]) + '! \n')

print('\n\nLEWPORTSOFT PRESENTS:\n\nMEAL SUGGESTION GENERATOR V1.0\n\n\n')

mainMenu()


