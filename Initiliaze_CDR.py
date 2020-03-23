from random import *

class CDR:
    def __init__(self, Name, Description):
        # Personal information
        self.Name = Name
        self.Faction = 1    # Numerical identifier as to which faction the CDR belongs to
        self.Health_Current = 100   # CDR's personal health
        self.Health_Max = 100       # Max health for the CDR
        self.Trait1 = " "
        self.Description = Description

        # Unit information
        self.Echelon = " "   # DIV, BN, CO, PLT, TM
        self.Rank = " "  # CDR, COL, CPT, LT, SGT
        self.Unit = " "  # Name of unit
        self.Parent = " "  # Higher unit in charge
        self.Soldiers = " "  # Number of Soldiers in the formation

        # Status variables
        self.Selected = False  # " " indicates false, "X" indicates true
        self.Location = "" # Will be the planet the CDR is stationed on currently

def Initialize_CDR(GAMESTATE, number):
    print("jj")
















# Armies intent:
# Be able to view all armies within the faction
# Fist to appear are the units under you (SCR) direct line of command
# As the first stage of the game, there will only be one rank known as Commander (CDR)
# These CDRs will all report to the SCR automatically
# In the future, CDRs will have subordinate levels of leaders that can eventually be reassigned to follow The SCR's specific guidance
# The only difference between the CDRs is the echelon unit they command (Team, Company, Division)
# Each unit can be modified from the top down as to what its specialty will be (To start, Infantry, Armor, Aviation, Engineer, Special Forces, more will come)
# Each unit type has certain advantages given the situation at hand

# Maps intent
# You can select one planet and either build on it, view the garrison, or move units
# The game will read how many of your troops are actually on that planet. If you have none, it will only read you the planet's basic information
# If you choose to move, the next question will be to what planet
# When you choose to move units, it will display all of the CDRs on that planet in garrison like so
# ex. [1][ ] CDR 1
#     [2][X] CDR 2
#     [3][ ] CDR 3
#     >:
# The "X" means that you have selected them for example. So, when you type "1" and "Ent", this page will refresh and view as:
#     [1][X] CDR 1
#     [2][X] CDR 2
#     [3][ ] CDR 3
#     >:
# You continue to select/deselect CDRS you want to move until you are satisfied. Then, you would type the option corresponding to "Execute" and your troops will begin movement
# In the first stage, movement speed will not yet be implemented. However, the intent is to make it so the distance between planets alters the speed of transportation
# Therefore, this will lead you directly into the battle phase (given there are opponents on the planet being moved to)

# Battle Phase:
# The battle phase is meant to allow the player some tactical decision making options present.
# For example, there are different ways you can attack a heavily fortified defense
# This part in general needs to work to improve the concepts before progressing too far