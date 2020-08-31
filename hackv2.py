from textblob import TextBlob as tb
from datetime import date
import matplotlib.pyplot as plt
import math

spent = ['spent', 'bought', 'used']
earned = ['earned', 'got', 'made', 'received']
stats = []
sumStats = []
#CHANGE THE VARIABLE BELOW TO YOUR BALANCE
balance = 0
nouns = []
workverb = []
deadWords = ['dollar', 'dollars']
earnOrSpend = False
today = date.today()
today1 = today.strftime("%m/%d/%y")

print('Hello, and welcome to your virtual money management system!')
user1 = input('Please enter your first name: ')

def moneyManager():
    global balance, earnOrSpend
    findBalance()
    print('To log an expense or profit, use the format in the examples below.')
    print('I spent 30 dollars on clothes at Target.')
    print('I earned 20 dollars by mowing lawns.')
    input1 = tb(input('Log here: '))

    for tag in input1.tags:
        word = tag[0]
        speechtype = tag[1]
        # Checks
        if speechtype == 'CD':
            stats.append(word)
            sumStats.append(word)
        if speechtype == 'VBG':
            workverb.append(word)
        if speechtype == 'NN' or speechtype == 'NNS' or speechtype == 'NNP':
            nouns.append(word)
            if word in deadWords:
                nouns.remove(word)
        # Deciders
        if speechtype == 'VBD' and word in earned:
            stats.append('+')
            sumStats.append('+')
            earnOrSpend = False
        if speechtype == 'VBD' and word in spent:
            stats.append('-')
            sumStats.append('-')
            earnOrSpend = True

    finalstats = f'{stats[0]}{stats[1]}'
    balance = int(balance) + int(finalstats)
    if earnOrSpend == False:
        updateBalance()
        updateTime()
        userfile = open(f'{user1}.txt', 'a')
        userfile.write(f'Date: {today1} , Gain/Loss: {finalstats} , How: {workverb[0]} {nouns[0]}' + "\n")
    if earnOrSpend == True:
        updateBalance()
        updateTime()
        userfile = open(f'{user1}.txt', 'a')
        userfile.write(f'Date: {today1} , Gain/Loss: {finalstats} , Location: {nouns[1]} , Item: {nouns[0]}' + "\n")

    stats.clear()
    workverb.clear()
    nouns.clear()
    logLoop()

def logLoop():
    input2 = input('Would you like to log another item? [y/n]')
    if input2 == 'y':
        moneyManager()
    elif input2 == 'n':
        findBalance()
        input3 = input('Would you like to see how long it would take to save up for an expensive item? [y/n]')
        if input3 == 'y':
            product()
        elif input3 == 'n':
            inputGraph()

    else:
        print('Please try again. That selection was not an option.')
        logLoop()

balanceFile = open(f'{user1}Balance.txt', 'a')
timeFile = open(f'{user1}Time.txt', 'a')

def updateBalance():
    balanceFile = open(f'{user1}Balance.txt', 'a')
    balanceFile.write(str(balance) + '\n')

def updateTime():
    timeFile = open(f'{user1}Time.txt', 'a')
    timeFile.write(str(today1) + '\n')

def balanceGraph():
    with open(f'{user1}Balance.txt') as f:
        lines1 = [line.rstrip() for line in f]
    lines1 = [int(i) for i in lines1]

    with open(f'{user1}Time.txt') as t:
        lines2 = [line.rstrip() for line in t]

    xlist = lines2
    ylist = lines1

    plt.plot([i for i in xlist], [j for j in ylist])
    plt.ylabel('Balance')
    plt.xlabel('Dates')
    plt.show()

def findBalance():
    global balance
    balanceFile = open(f'{user1}Balance.txt', 'r')
    first_line = balanceFile.readline()
    for balance in balanceFile:
        pass
    print(balance)

def product():
    months = 0
    input3 = int(input('Enter your monthly salary: '))
    input4 = int(input('How much is the product you want to save up for? '))
    input5 = int(input('How much do you spend on necessities and utilities each month? '))
    mo1 = input3 - input5
    mo2 = input4 / mo1
    months = math.ceil(mo2)
    print('')
    print('It will take you approximately ' + str(months) + ' or more months to buy your desired product.')
    if months > 20:
        print('We recommend that you take a loan for this item if it is absolutely necessary.')
    else:
        pass
    print('')
    inputGraph()

def inputGraph():
    input4 = input('Would you like to see a graph of your balance? [y/n]')
    if input4 == 'y':
        balanceGraph()
    else:
        ending()

def ending():
    print(' ')
    print('To view your transaction log sheet, go to the text file that says ______.txt, where the blanks are your '
          'name.')
    print('Your latest transaction will be at the top.')
    print('To view your balance log sheet, go to the text file that says ______Balance.txt, where the blanks are your '
          'name.')
    print('Your latest balance update will be at the bottom.')
    print(' ')
    input5 = input('Type ok to continue: ')
    if input5 == 'ok' or input5 == 'OK':
        exit()


moneyManager()
