"""
ingredientanalysis.py
"""

import sys

instruction = "Check list of ingredients against "\
    "internal ingredient database for possible allergic reaction. " \
    "\nPlease enter list of ingredients in lowercase and seperated by comma and a blankspace. "

safeIngredients = {
    "talc",               #dior
    "nylon-12",
    "mica",
    "barium sulfate",
    "phenyl trimethicone",
    "caprylyl glycol",
    "titanium dioxide"
    }


potentialAllergens= {
    "kaolin",             #kvd
    "magnesium myristate",
    "boron nitride",
    "isoamyl laurate",
    "zinc stearate",
    "polyester-4",
    "2-hexanediol",
    "dimethiconol",
    "oryza sativa hull powder",
    "iron oxide"}

def Convert(string): 
    verifyingList= set(string.split(", ")) 
    return verifyingList

verifyingList = input(instruction) 
verifyingList = Convert(verifyingList)

resultSafe, resultRisk, resultUnknown = verifyingList & safeIngredients, verifyingList & potentialAllergens, verifyingList - safeIngredients - potentialAllergens
dictofsets= {"safe": resultSafe, "potentially allergic": resultRisk, "unknown": resultUnknown}

print()
for key, eachset in dictofsets.items():
    if len(eachset) != 0:
        print(f"There are {len(eachset)} {key} ingredients: ")
        for i, ingredient in enumerate(eachset, start = 1):
            print(f"{i:2}. {ingredient} ")
    print()



sys.exit(0)

    
