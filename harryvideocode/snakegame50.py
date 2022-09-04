import random
list1=["s","w","g"]
player=0
computer=0
total_chance=0
number_chance=10
print("snake water gun game \n \n")
print("s for snake \n w for eater \n g for gun")

while total_chance<number_chance:
    _input=input("enter snake, water or gun:::")
    _random=random.choice(list1)

    if _input==_random:
        print("tie both 0 point each \n")

    elif _input=="s" and _random=="g":
        computer=computer+1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("compuer get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    elif _input=="s" and _random=="w":
        player=player+1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("player get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    elif _input=="g" and _random=="s":
        player = player + 1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("player get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    elif _input == "g" and _random == "w":
        computer=computer+1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("computer get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    elif _input == "w" and _random == "s":
        computer=computer+1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("computer get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    elif _input == "w" and _random == "g":
        player = player + 1
        print(f"player guess{_input} and computer guess {_random} \n")
        print("player get 1 point")
        print(f"total point of computer={computer} and total point of player={player}")
    else:
        print("please input valid number")
    total_chance=total_chance+1
    print(f"{number_chance-total_chance} left chance {number_chance} \n")
print("GAME OVER")
if computer==player:
    print("tie")
elif computer>player:
    print("computer win and player losses")
else:
    print("player win and computer losses")
print(f"computer point {computer} and player point {player}")



