import random

response = input("Do you want to roll a dice?")

while(True):
   
    response = input("to continue press:y" " to exit press:n")
    
    response == "y"

    no = random.randint(1,6)

    if(no.value()):
        print()
    
    if no==1 :
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

   

    if( response== "n"):
        break   

