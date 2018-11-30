"""
NaNoGenMo: A Little Robot's Guide to Witchcraft
"""
import random

ingred_input = open("ingredients.txt","r")
novel = open("novel.doc","w")

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
    del ingredients_list[:]
    
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
    
    num_components = random.randint(4,7) # randomly generates how many ingredients to choose   
    ingred_index = random.sample( range(0,len(all_ingredients)), num_components ) # picks out num_comp amount of integers within 0 to the length of the ingredients list
    
    for i in range (0,num_components):               
        ingredients_list.append( all_ingredients[ingred_index[i]].rstrip() ) # makes an acessible list of all the ingred for this loop 
        ingredient_print += ( (ingredients_list[i]) + "\n" ) # string to print out

    """ GENERATE INSTRUCTIONS """
    
    potential0 = ['grind up','burn','drown','burn a candle over','crush','dab oil on','meditate over']
    potential1 = ['grind together','mix together','stir in water','combine together','crush together with a mortar and pestle']
    potential2 = ['under the light of a full moon', 'during a new moon','in a cauldron',
                  'during a waxing moon','during a waning moon','on a cloudless night',
                  'under the light of a solar eclipse','during a lunar eclipse',
                  'during a blood moon','during a harvest moon','at exactly noon',
                  'at daybreak','at dawn','at dusk','at exactly midnight']
    potential3 = ['with a steady hand','while praying to a deity of your choice','while keeping a clear mind',
                  'while envisioning the desired result','while meditating over','while chanting a mantra',
                  'while whispering in tongues']
    potential4 = ['Apply result to forehead.','Sleep with result under your pillow.',
                  'Bury result under a dead tree.','Use result to clean your threshold.',
                  'Drink result with water before bed.','Burn result and apply ashes to the subject.',
                  'Carry result on your person in small pouch for full effect.']

    if num_components == 4:
        instructions = ("First, take the " + ingredients_list[0] + " and the " + ingredients_list[1]
        + " and " + random.choice(potential1) + ". Next, add the " + ingredients_list[2] 
        + ' ' + random.choice(potential2) + " and " + random.choice(potential1) 
        + ". Finally, " + random.choice(potential0) + " the " + ingredients_list[3] 
        + " and " + random.choice(potential1) + " " + random.choice(potential3) + ". " + random.choice(potential4))
    elif num_components == 5:
        instructions = ("Take the " + ingredients_list[0] + ", " + ingredients_list[1] 
        + ", and " + ingredients_list[2] + " and " + random.choice(potential1)
        + ". Then, " + random.choice(potential3) + ", add the " + ingredients_list[3]  + " "
        + random.choice(potential2) + ". Finally, take the " + ingredients_list[4] 
        + " and " + random.choice(potential1) + " " + random.choice(potential2) + ". " + random.choice(potential4))
    elif num_components == 6:
        instructions = ("First, " + random.choice(potential2) + " and " + random.choice(potential3)
        + ", take the " + ingredients_list[0] + " and the " + ingredients_list[1]
        + " and " + random.choice(potential1) + ". Then add the " + ingredients_list[2] + " and "
        + ingredients_list[3] + " " + random.choice(potential3) + ". Separately "
        + random.choice(potential1) + " the " + ingredients_list[4] + " and "
        + ingredients_list[5] + " " + random.choice(potential3) + " before adding to the first mixture. " + random.choice(potential4))
    else:
        instructions = ("First, " + random.choice(potential0) + " the " + ingredients_list[0]
        + " and " + random.choice(potential1) + " with the " + ingredients_list[1]
        + ". Take this and add the " + ingredients_list[2] + " " + random.choice(potential3)
        + " " + random.choice(potential2) + ". Separately, " + random.choice(potential1) 
        + " the " + ingredients_list[3] + ", " + ingredients_list[4] + ", and "
        + ingredients_list[5] + " " + random.choice(potential3) + ". Now " + random.choice(potential1)
        + ". Finally, " + random.choice(potential3) + ", add the " + ingredients_list[6]
        + " " + random.choice(potential2) + ". " + random.choice(potential4))
    
    return titleA + '\n\n' + ingredient_print + '\n\n' + instructions
    

""" --------------- OUTPUT --------- """
print("A LITTLE ROBOT'S GUIDE TO WITCHCRAFT \n------------\n",file=novel)
for j in range (0,1000): 
    print(generate() + "\n------------\n",file=novel)

ingred_input.close()
novel.close()


