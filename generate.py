"""
NaNoGenMo: A Little Robot's Guide to Witchcraft
"""
import random

ingred_input = open("ingredients.txt","r")
all_ingredients = ingred_input.readlines()

titleB = ['Infatuation','Sleep','Fertility','Health','Wisdom','Peace','Healing','Transformation','Luck','Hair Growth','Safety']

i = 0 # ye olde index variable
j = 0
ingredients_list = []

def generate_positive():
    positive_ttl = ['Poultice','Balm','Charm','Glamour','Enchantment']
    p2 = ['Love','Rest','Health','Wisdom','Peace','Healing','Luck','Hair Growth','Safety']
    
    titlechoice = random.randint(0,1)
    if titlechoice == 0:
        return random.choice(positive_ttl) + ' of ' + random.choice(p2)
    else:
        return random.choice(positive_ttl) + ' for ' + random.choice(p2)
    
def generate_neutral():
    neutral_ttl = ['Spell','Elixer','Potion']
    p2 = ['Love','Rest','Health','Wisdom','Peace','Healing','Luck','Hair Growth','Safety','Infatuation','Death','Sickness','Acne']
    
    titlechoice = random.randint(0,1)
    if titlechoice == 0:
        return random.choice(neutral_ttl) + ' of ' + random.choice(p2)
    else:
        return random.choice(neutral_ttl) + ' for ' + random.choice(p2)
    
def generate_negative():
    negative_ttl = ['Hex','Curse','Blight','Plague']
    p2 = ['Infatuation','Death','Sickness','Acne']
    
    titlechoice = random.randint(0,1)
    if titlechoice == 0:
        return random.choice(negative_ttl) + ' of ' + random.choice(p2)
    else:
        return random.choice(negative_ttl) + ' for ' + random.choice(p2)

def generate():
    ingredient_print = ''
    
    """ --------------- intent generation --------- """
    
    # determine if positive, neutral, or negative spell
    intent = random.randint(0,2)
    if intent == 0: 
        titleA = generate_positive()
    elif intent == 1:
        titleA = generate_neutral()
    else:
        titleA = generate_negative()
            
    """ --------------- INGREDIENT CHOICES --------- """
    
    
  #  num_components = random.randint(4,7) # randomly generates how many ingredients to choose    
    num_components = 4
    which_ingred_index = random.sample( range(0,len(all_ingredients)), num_components ) # picks out num_comp amount of integers within 0 to the length of the ingredients list
    
    for i in range (0,num_components):               
        ingredients_list.append( all_ingredients[which_ingred_index[i]].rstrip() ) #appends 
        ingredient_print += ( (ingredients_list[i]) + "\n" ) # string to print out
        
    """ GENERATE INSTRUCTIONS """
    
    potential0 = ['grind up','burn','drown','burn a candle over']
    potential1 = ['grind together','mix together','stir','combine together']
    potential2 = ['under the light of a full moon', 'during a new moon','in a cauldron']
    potential3 = ['with a steady hand','while praying to a deity of your choice','while keeping a clear mind','while envisioning the desired result']
   

    if num_components == 4:
        instructions = ("First, take the " + ingredients_list[0] + " and the " + ingredients_list[1]
        + " and " + random.choice(potential1) + ". Next, add the " + ingredients_list[2] + ' ' + random.choice(potential2)
        + " and " + random.choice(potential1) + ". Finally, " + random.choice(potential0) + " the " + ingredients_list[3] + " and " + random.choice(potential1)
        + " " + random.choice(potential3) + ".")
    elif num_components == 5:
        instructions = "lol"
    elif num_components == 6:
        instructions = "what"
    else:
        instructions = "weener"
    
    return titleA + '\n\n' + ingredient_print + '\n\n' + instructions
    

""" --------------- OUTPUT --------- """
print("A LITTLE ROBOT'S GUIDE TO WITCHCRAFT \n             ------------ \n")
for j in range (0,2): 
    print(generate() + "\n\t\t------------\n") # print ingredients list

ingred_input.close()