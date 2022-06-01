from random import choice

store = {"R":"rock", "P":"paper", "S":"scissors"}
options=["R", "P", "S"]


computer = choice(options)
player=input("Choose between R, P, S, \n ").upper()
condition = True

while condition:
 
        if player not in options:
            player=input("Choose between R, P, S, \n ").upper()

        elif (computer=="R" and player=="S")or(computer=="S" and player=="R"):
            print(f"Player({store[player]}): CPU ({store[computer]})")
            print("Rock wins")
            condition = False

        elif (computer=="R" and player=="P")or(computer=="P" and player=="R"):
            print(f"Player({store[player]}): CPU ({store[computer]})")
            print("Paper wins")
            condition = False
        
        elif (computer=="P" and player=="S")or(computer=="S" and player=="P"):
            print(f"Player({store[player]}): CPU ({store[computer]})")
            print("Scissors wins")
            condition = False

      

        else:
            print("There is a tie")
            player=input("Choose between R, P, S, \n ").upper()

for k,v in store.items():
    pass
