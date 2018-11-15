# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 22:29:27 2018

@author: ilana
"""
import random

i = 0 # ye olde index variable

ingredient_printout = ''
anger = ["rusty nails","war water","hot sauce","pepper","lemon", "cayenne pepper", "dragon's blood", "black salt", "onyx"]

num_Ingred = random.randint(2,8) # randomly generates how many ingredients to choose
ingredients = random.sample(range(0,len(anger)),num_Ingred) #array of random ingredients without repeating

for i in range (0,num_Ingred):
    #print(anger[ingredients[i]])
    ingredient_printout += anger[ingredients[i]] + '\n'
    
    
print(ingredient_printout)