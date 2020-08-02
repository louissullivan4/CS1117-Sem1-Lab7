# ScriptName: functions.py
# Author: Louis Sullivan 119363083

import random

def is_stairs(s):
    '''
    function - to see if a list numbers are in ascending or descending order
    :param: <s> is the stairs
    :param
    :return: true if it is a stairs or false if it isn't
    '''
    #if the length of s is greater than 1
    if len(s) > 1:
        #first number variable is set to list of s0
        first_number = ord(str(s[0]).lower())
        #second number is set to the list of s1
        second_number = ord(str(s[1]).lower())
        #if first number take is equal to second number
        if first_number -1 == second_number:
            #stairs is equal to second number minus first number
            stairs = second_number - first_number
        #if first number plus 1 is equal to second number
        elif first_number + 1 == second_number:
            #stairs is equal to second number minus first number
            stairs = second_number - first_number
        # else it isn't stairs so return false
        else:
            return False
        # when i is in the length of the list s
        for i in range(len(s)-1):
            if ord(str(s[i]).lower()) + stairs != ord(str(s[i + 1]).lower()):
                return False
        #else return true
        return True
    #else return false
    return False

def factorial(n):
    '''
    function - find the factorial of <n>
    :param: <n> is a number we are going to find the factorial of
    :param:
    :return:
    '''
    if n >= 0:
        fact_value = 1
        for val in range(1, n+1):
            fact_value *= val
            print(fact_value)
    else:
       print(-1)

def gremlins():
    '''
    function - To find out the outcome of our Gremlin
    :param:
    :param:
    :return:
    '''
    #name variable set to Gizmo
    name = 'Gizmo'
    #creatinf variable i starting with one
    i = 1
    #choose a random number between 1 and 3
    num = random.randint(1, 3)
    #while i is less than 5
    while i < 5:
        #if random number is equal to 1, call okay to feed function
        if num == 1:
            #if function returns false
            if okay_to_feed() == False:
                #gremlins name is now stripe
                name = 'Stripe'
                #print that Gizmo is now Stripe
                print("Gizmo is now a gremlin called Stripe")
            #else print name
            else:
                print(name)
        # if random number is equal to 2, call is too bright function
        elif num == 2:
            #if function returns true
            if is_too_bright() == True:
                #print gremlin name and is no more and break
                print(name, " is no more")
                break
            #else print name
            else:
                print(name)
        ##if random number is equal to 3, call is_wet function
        else:
            #if function returns true
            if is_wet() == True:
                #print name and is a triplet
                print( name, " is a triplet")
            #else print name
            else:
                print(name)
        #increment loop
        i += 1

#Helper Functions
def is_wet():
    '''
    function - choose true or false to see if Gremlin is wet
    :param:
    :param:
    :return: return true of false
    '''
    #makes a random choice between true or false
    n = random.choice([True, False])
    #if true is chosen
    if n == True:
        #return true
        return True
    else:
        #else return false
        return False

def is_too_bright():
    '''
    function - choose a random brightnesss to see if its too bright for Gremlin
    :param:
    :param:
    :return:True or False
    '''
    #randomly choose a number between 1 and 100
    lux_level = random.randint(1, 100)
    #if its greater than 80
    if lux_level > 80:
        #return true
        return True
    #else return false
    else:
        return False

def okay_to_feed():
    '''
    function - choose a random time to see if its okay to feed Gremlin
    :param:
    :param:
    :return: True or False
    '''
    #randomly choose a number between 0 and 24
    time = random.randint(0, 24)
    #if the time is is greater than or equal to 0 and less than 4
    if 0 <= time < 4:
        #return false
        return False
    #else return true
    else:
        return True




