#! /usr/bin/env python3

#What's for dinner?

import random
import time
import json
import wave
import sys
#Yeah I know this list is surplus to requirements but whatever I'm keeping it here as a backup
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
'Enchilladas! With quorn mince and baked beans and cheese and jalapenos etc',
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

with open('dinnerList.txt', 'r') as dinnerListFile:
    dinnerList = json.load(dinnerListFile)

def mainMenu():
    mainMenuChoice = ''
    while mainMenuChoice != '1' or mainMenuChoice != '2':
        mainMenuChoice = input('\n1) Dinner Suggestions \n2) Edit Dinner List \n3) Exit\n')
        if mainMenuChoice == '1':
            dinnerSuggester()
        elif mainMenuChoice == '2':
            listEditMenu()
        elif mainMenuChoice == '3':
            sys.exit()

def listEditMenu():
    listOptions = ''
    while listOptions != '1' or listOptions != '2' or listOptions != '3' or listOptions != '4':
        listOptions = input('\n1) Add Food Item \n2) Delete Food Item \n3) View Food List \n4) Back\n')
        
        if listOptions == '1': #Add food item
            foodItem  = input('\nFood Name: ')
            dinnerList.append(foodItem)
            with open('dinnerList.txt', 'w') as dinnerListFile:
                json.dump(dinnerList, dinnerListFile)
            print(foodItem + ' added to food list.\n')
            time.sleep(1)
            
        if listOptions == '2': #Delete food item
            foodItem  = input('\nDelete Food Name (case sensitive): ')
            if foodItem in dinnerList:
                dinnerList.remove(foodItem)
                with open('dinnerList.txt', 'w') as dinnerListFile:
                    json.dump(dinnerList, dinnerListFile)
                print(foodItem + ' removed from food list.\n')
                time.sleep(1)
            else: print('Could not find ' + foodItem + ' in food list :(\n')
            
        if listOptions == '3': #Print dinner list
            print('\n')
            for i, n in enumerate(dinnerList):
                print(i, n)
            
        if listOptions == '4': #Back
            mainMenu()
            

        

    

def dinnerSuggester():
    input('\nPress enter to get a meal suggestion!\n')
    randomFoodIndex = random.randint(0, (len(dinnerList) - 1))
    randomTalkIndex = random.randint(0, (len(talkList) - 1))
    print(str(talkList[randomTalkIndex]) + ' ' + str(dinnerList[randomFoodIndex]) + '! \n')
    while True:
        time.sleep(1)
        anotherSuggestion = input('\nPress enter try again, or type \'b\' to go back:\n').lower()
        if anotherSuggestion == 'b':
            False
            print('\n')
            mainMenu()
        randomFoodIndex = random.randint(0, (len(dinnerList) - 1))
        randomTalkIndex = random.randint(0, (len(talkList) - 1))
        print(str(talkList[randomTalkIndex]) + ' ' + str(dinnerList[randomFoodIndex]) + '! \n')
        

print('\n\nLEWPORTSOFT PRESENTS:\n\nMEAL SUGGESTION GENERATOR v2.0\n')

mainMenu()
#dinnerSuggester()

