import random as rd
import inquirer


k_max_roulette_number = 49


def spinning_roulette(current_money: int, bet_money: int, number: int) -> int:
    roulette_number = rd.randint(0, k_max_roulette_number)

    if number == roulette_number:
        bet = """
OMG OMG OMG!
        
YOU GOT IT!
I CAN'T BELIEVE YOU GOT IT!
"""
        resulting_money = current_money + bet_money * 500
    else:
        bet = f"""

O no!
        
Your bet ({number}) was not chosen :-:
"""
        resulting_money = current_money - bet_money
    print(
        f"""

The roulette is spinning and spinning...

and spinning...

and the number is... {roulette_number}!
{bet}
""")
    print(f"You still have {resulting_money} in your pocket")
    return resulting_money


print(
"""
Welcome to Havayuna's Roulette!

The rules are pretty simple: choose a number between 0 and 49.
If the result is the same as your number 
you'll receive x50 the money you bet!
If the result is different you'll lose the money you bet in the round.

You can play as many times - but if you waste all the money is
G A M E    O V E R
.
.
.
So let's begin!
"""
)

money = 500

# Game loop
while money > 0:
    chosen_number = int(input("Choose your number:"))
    if chosen_number > k_max_roulette_number or chosen_number < 0:
        print(
            """
Oops!
        
The roulette has a range between 0 and 49, so this value is not valid.
Try a valid number this time ^-^
"""
            )
        continue
    
    while True:
        round_money = int(input("How much are you going to bet in this round?"))

        if round_money >= money:
            print(
                f"""
Ooo no!
                
You don't have that much to play on this round.
You have {money} to bet, so try this value or a lower one.
"""
            )
            continue
        else:
            break

    money = spinning_roulette(money, round_money, chosen_number)
    
    still_want_to_play = [
        inquirer.List(
            "stay_or_go",
            message="Do you still want to play?",
            choices=["Yes", "No"],
        ),
    ]
    what_to_do = inquirer.prompt(still_want_to_play)
    if what_to_do["stay_or_go"] == "No":
        exit_message = "See you next time!"
        break

# Shutdown
if money <= 0:
    exit_message = """
Oh boy!

You don't have money to play again.
"""

print(exit_message)
print("G A M E     O V E R")