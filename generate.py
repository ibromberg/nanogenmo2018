"""
NaNoGenMo: A Little Robot's Guide to Witchcraft
"""
import random

ingred_input = open("ingredients.txt","r")
all_ingredients = ingred_input.readlines()

i = 0 # ye olde index variable
j=0

title_printout = ' '

def generate():
    ingredient_printout = ''
    
    """ --------------- TITLE CHOICES --------- """
    titleA = ['Spell','Potion','Elixer','Poultice','Hex','Curse']
    titleB = ['Love','Sleep','Fertility','Health','Wisdom']
    titlechoice = random.randint(0,1)
    if titlechoice == 0:
        title_printout = random.choice(titleA) + ' of ' + random.choice(titleB) + '\n'
    else:
        title_printout = random.choice(titleA) + ' for ' + random.choice(titleB) + '\n'
        
        
    """ --------------- INGREDIENT CHOICES --------- """
    # possible_ingredients = ingred_input.read().splitlines()
        
    num_Ingred = random.randint(3,8) # randomly generates how many ingredients to choose
    ingredients = random.sample(range(0,len(all_ingredients)),num_Ingred) #array of random ingredients without repeating
    
    for i in range (0,num_Ingred):
        ingredient_printout += all_ingredients[ingredients[i]]
    return title_printout + '\n' + ingredient_printout
    

""" --------------- OUTPUT --------- """
print("A LITTLE ROBOT'S GUIDE TO WITCHCRAFT \n             ------------ \n")
for j in range (0,10): print(generate() + "\n             ------------ \n") # print ingredients list

ingred_input.close()