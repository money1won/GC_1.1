from random import *
import time
from Initiliaze_CDR import *

def clear():
    print("\n"*60)

def print_Menu(options, outcomes, GAME_STATE, checkbox = False):

    count = 1
    selected = ""
    for i in range(len(options)):
        if checkbox == True:
            selected = "[ ] "
            if i == 0 or i == 1:
                selected = ""
            elif (GAME_STATE["CDR_1"][i-2].Selected == True) and (GAME_STATE["Selected_Planet"] == GAME_STATE["CDR_1"][i-2].Location):
                selected = "[X] "
        print("[" + str(count) + "] " + selected + str(options[str(count)]))
        count = count + 1

    selected = input(">: ")
    if selected == "" or (selected.isnumeric() == False):
        selected = 0  # sets the input to a valid int if the format is otherwise invalid (blank or str)
    if (int(selected) <= len(options)) & (int(selected) > 0):
        GAME_STATE["State"] = outcomes[selected]
        GAME_STATE["Selected"] = selected
        return GAME_STATE
    else:
        GAME_STATE["Selected"] = 1  # Selected value set to something valid so it loops correctly
        return GAME_STATE           # Game state set to its original value so loop is induced


def print_Map(GAME_STATE):
    for Planet in GAME_STATE["Map"]:
        print("\n"*Planet.y + " "*Planet.x + Planet.Name)






class SCR:
    def __init__(self, Name, Description):
        self.Name = Name
        self.Faction = 1
        self.Health_Current = 100
        self.Health_Max = 100
        self.Trait1 = " "
        self.Description = Description


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

class Planet:
    def __init__(self, Name):
        self.Name = Name
        self.Faction = 1
        self.x = randint(0,200)
        self.y = randint(0,3)


class u:
    Name = ""

class Player:
    Name = ""
    Faction = ""


Player_1 = Player
Player_2 = Player

SCR_1 = SCR
SCR_2 = SCR


temp_CDR_1 = ""

Factions = ["AA", "BB"]
Weapons = u
Equipment = u
Map = u
initialized = False

Starting_Currency_1 = 0
Starting_Currency_2= 0

# Randomly generate the first three SCRs the player can pick from
SCR1 = SCR(Name="SCR 1",
           Description="FDAFDFAG")


SCR2 = SCR(Name="SCR 2",
           Description="ghshDFAG")

options = {}

GAME_STATE = {"State": "Menu",
              "Factions": Factions,
              "Player_1": Player_1,
              "Player_2": Player_2,
              "SCR_1": SCR_1,
              "SCR_2": SCR_2,
              "CDR_1": [""],
              "CDR_2": [""],
              "Currency_1": 500,
              "Currency_2": 500,
              "Currency_Rate_1": 25,
              "Currency_Rate_2": 25,
              "Weapons": Weapons,
              "Equipment": Equipment,
              "Map": Map,
              "isRunning": True,
              "Selected": 0,
              "Selected_Planet": "",
              "Target_Planet": ""}



while GAME_STATE["isRunning"]:
    clear()
    while GAME_STATE["State"] == "Menu":
        initialized = False  # Used in "New Game" to ensure game doesn't initialize variables twice
        # print Main Menu
        options = {"1": "New Game", "2": "Load Game", "3": "Extras", "4": "Options", "5": "Quit"}
        outcomes = {"1": "New Game", "2": "Load Game", "3": "Extras", "4": "Options", "5": "Quit"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)  # New Game or load game is chosen
        clear()
    # NEW GAME SCREENS BEGIN
    while GAME_STATE["State"] == "New Game":
        # INITIALIZE BEGINS
        if not initialized:  # todo Only for variables that need to be initialized just before the game starts
            planet1 = Planet("Home")  # todo force planets to be randomly generated instead of hardcoded
            planet2 = Planet("Neutral")
            planet3 = Planet("Hostile")
            GAME_STATE["Map"] = [planet1, planet2, planet3]  # Packs all planets generated into the GAME_STATE

            cdr1 = CDR("CDR 1", "")
            cdr2 = CDR("CDR 2", "")
            cdr3 = CDR("CDR 3", "")
            # todo working on this!!!!_________

            GAME_STATE["CDR_1"] = Initialize_CDR(GAME_STATE, 3)




            # todo working on this!!!!!^^^^^^^^^


            cdr1.Location = GAME_STATE["Map"][1]
            cdr2.Location = GAME_STATE["Map"][1]
            cdr3.Location = GAME_STATE["Map"][1]
            GAME_STATE["CDR_1"] = [cdr1, cdr2, cdr3]

        # INITIALIZE ENDS

        options = {"1": GAME_STATE["Factions"][0], "2": GAME_STATE["Factions"][1]}
        outcomes = {"1": "New Game 1", "2": "New Game 1"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)  # Selected and State updated

        GAME_STATE["Player_1"].Faction = options[str(GAME_STATE["Selected"])]  # Faction updated to selection from the options
        clear()

    while GAME_STATE["State"] == "New Game 1":
        options = {"1": SCR1.Name, "2": SCR2.Name}
        outcomes = {"1": "New Game 2", "2": "New Game 2"}  # outcomes for the game state to be used
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)

        outcomes2 = {"1": SCR1, "2": SCR2}  # Outcomes used for loading the object specifically
        GAME_STATE["SCR_1"] = outcomes2[str(GAME_STATE["Selected"])]  # Temporary SCR updated to selection
        clear()

    while GAME_STATE["State"] == "New Game 2":
        print(GAME_STATE["SCR_1"].Name + "\n\n" + GAME_STATE["SCR_1"].Description + "\n")
        options = {"1": "Confirm", "2": "Back"}
        outcomes = {"1": "New Game 3", "2": "New Game 1"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)

        print(GAME_STATE["SCR_1"].Name)
        clear()

    while GAME_STATE["State"] == "New Game 3":  # Intro page. Any comments displayed to user before conquering galaxy

        print("test test: " + GAME_STATE["SCR_1"].Name)
        time.sleep(0)
        options = {"1": "Enter"}
        outcomes = {"1": "Overview"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    # NEW GAME SCREENS END
    # GAME PLAY SCREENS BEGIN
    while GAME_STATE["State"] == "Overview":
        options = {"1": "Map", "2": "Armies", "3": "R&D", "4": "Finance"}
        outcomes = {"1": "Map", "2": "Armies", "3": "R&D", "4": "Finance"}
        print("\n"*2 + "Credits: " + str(GAME_STATE["Currency_1"]) + "      Credits per turn: " + str(GAME_STATE["Currency_Rate_1"]))
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()






    # Begin Map based interfaces

    while GAME_STATE["State"] == "Map":
        print_Map(GAME_STATE)

        options = {"1": "Back"}
        outcomes = {"1": "Overview"}
        for i in range(len(GAME_STATE["Map"])):
            options[str(i+2)] = GAME_STATE["Map"][i].Name  # Creates the dictionary for all planets added into the game
            outcomes[str(i+2)] = "Selected Planet"

        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        GAME_STATE["Selected_Planet"] = GAME_STATE["Map"][int(GAME_STATE["Selected"]) - 2]  # Selected_Planet var used in next screen exclusively so it is not apart of GAME_STATE
        clear()

    # Prints menu for a selected planet
    while GAME_STATE["State"] == "Selected Planet":
        options = {"1": "Back", "2": "Build", "3": "View Garrison", "4": "Move"}
        outcomes = {"1": "Map", "2": "Build", "3": "View Garrison", "4": "Move"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    # Prints menu for building on a selected planet
    while GAME_STATE["State"] == "Build":   # todo add all building choices here. Each will require their own while loop
        options = {"1": "No buildings programmed currently"}
        outcomes = {"1": "Selected Planet"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    # Prints the garrison of the selected planet
    while GAME_STATE["State"] == "View Garrison":
        options = {"1": "Back"}
        outcomes = {"1": "Selected Planet"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        # todo print all CDRs and their respective units here
        clear()

    # Allows the player to pick commanders to move to a different planet
    while GAME_STATE["State"] == "Move":
        # This will require all CDRs listed so the player may select as many as they choose to move.
        # Will require a separate set of options, outcomes, and an alternate print menu for this mechanic

        options = {"1": "Back", "2": "Execute"}
        outcomes = {"1": "Selected Planet", "2": "Target Planet"}

        count = 3
        for i in range(len(GAME_STATE["CDR_1"])):
            if GAME_STATE["CDR_1"][i].Location == GAME_STATE["Selected_Planet"]:    # todo this condition will later be changed to something that allows ONLY directly subordinate CDRs to be immediatly shown
                options[str(count)] = GAME_STATE["CDR_1"][i].Name  # Creates the dictionary for all player 1's CDRs
                outcomes[str(count)] = "Checked"
                count = count + 1

        print(options)
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE, True)
        if GAME_STATE["Selected"] == "1":
            for i in range(len(GAME_STATE["CDR_1"])):
                GAME_STATE["CDR_1"][i].Selected = False
        clear()

    # Take the commander selected for combat and toggle the "checked" or "unchecked" box based on what they currently are
    while GAME_STATE["State"] == "Checked":
        selected = int(GAME_STATE["Selected"])
        if GAME_STATE["CDR_1"][selected-3].Selected == True:
            GAME_STATE["CDR_1"][selected-3].Selected = False
        elif GAME_STATE["CDR_1"][selected-3].Selected == False:
            GAME_STATE["CDR_1"][selected-3].Selected = True
        else:
            print("ERROR")
        GAME_STATE["State"] = "Move"

    # This takes place after the Commanders are selected. This will allow you to pick a planet to move to.
    while GAME_STATE["State"] == "Target Planet":


        options = {"1": "Back"}
        outcomes = {"1": "Move"}
        for i in range(len(GAME_STATE["Map"])):
            options[str(i+2)] = GAME_STATE["Map"][i].Name  # Creates the dictionary for all planets added into the game
            outcomes[str(i+2)] = "Battle Deployment"

        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        GAME_STATE["Target_Planet"] = GAME_STATE["Map"][int(GAME_STATE["Selected"]) - 2].Name
        clear()
    # End Map based interfaces





    # "Battle Deployment" This takes place after a selected and target planet are selected allowing the movement of Soldiers to take place
    # This must detect if the movement is considered peaceful or hostile based on the faction of the hosted planets
    # This will use the Planet classes "Faction" variable to determine if the factions are the same or different
    # Ie, if selected_planet.Faction == target_planet.Faction, movement is peaceful as the planets are owned by the same
    # factions, meaning, that the player is simply reinforcing the planet. However, if the faction numbers are NOT equal
    # the game will then simulate battle to determine the outcome.

    # This is a grossly simplified explanation as there will be add ins allowing the player to change their overall
    # attack strategy for a planet, but this is the basics.

    # Begin Battle based interfaces! FINALLY!!!!!!!!!!!!!!!!!!!!!
    while GAME_STATE["State"] == "Battle Deployment":
        print("Prepare for battle")
        input(":")


    # End Battle based interfaces









    # Begin Army information

    while GAME_STATE["State"] == "Armies":
        options = {"1": "Back"}
        outcomes = {"1": "Overview"}
        count = 1
        for CDR in GAME_STATE["CDR_1"]:
            if CDR != "":  # If the commander exists
                count = count + 1
                options[str(count)] = str(CDR.Name)
                outcomes[str(count)] = "Speak"
        # Todo add all other kinds of commanders here. Fix so all CDRs are in the same GAME_STATE var
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        temp_CDR_1 = GAME_STATE["CDR_1"][int(GAME_STATE["Selected"]) - 2]
        # CDR_1[Selected] using the selected from the "Armies"
        # used to display the CDR that was selected earlier. Added in the "-2" because it is a list index, not a dict
        clear()

    # CDRs information presented here
    while GAME_STATE["State"] == "Speak":
        print(temp_CDR_1.Name)

        print("\n")

        options = {"1": "Back", "2": "Dialogue 1", "3": "Dialogue 2", "4": "Dialogue 3"}
        outcomes = {"1": "Armies", "2": "Speak", "3": "Speak", "4": "Speak"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    # End Army interfaces







    # todo add a way for the upgrades to do something. They are currently placeholders. Should cost credits
    # Begin research menus
    while GAME_STATE["State"] == "R&D":
        options = {"1": "Back", "2": "Engineering", "3": "Tactics", "4": "Economy"}
        outcomes = {"1": "Overview", "2": "Engineering", "3": "Tactics", "4": "Economy"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    while GAME_STATE["State"] == "Engineering":
        options = {"1": "Back", "2": "Stronger Ships", "3": "New Rifles", "4": "Faster Ships"}
        outcomes = {"1": "R&D", "2": "R&D", "3": "R&D", "4": "R&D"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    while GAME_STATE["State"] == "Tactics":
        options = {"1": "Back", "2": "Faster Raids", "3": "Naval Tactics", "4": "Officer School"}
        outcomes = {"1": "R&D", "2": "R&D", "3": "R&D", "4": "R&D"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    while GAME_STATE["State"] == "Economy":
        options = {"1": "Back", "2": "Tax Boost", "3": "Salvage", "4": "Grants"}
        outcomes = {"1": "R&D", "2": "R&D", "3": "R&D", "4": "R&D"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()
    # End research menus









    # Begin Finance options
    while GAME_STATE["State"] == "Finance":
        print("Credits per turn " + str(GAME_STATE["Currency_Rate_1"]))
        options = {"1": "Back", "2": "Increase Taxes +5%", "3": "Decrease taxes -5%"}
        outcomes = {"1": "Overview", "2": "Finance+", "3": "Finance-"}
        GAME_STATE = print_Menu(options, outcomes, GAME_STATE)
        clear()

    # Perform the calculation of the tax increase
    while GAME_STATE["State"] == "Finance+":
        GAME_STATE["Currency_Rate_1"] = int(GAME_STATE["Currency_Rate_1"]*1.05)
        GAME_STATE["State"] = "Finance"
        clear()

    # Perform the calculation of the tax decrease
    while GAME_STATE["State"] == "Finance-":
        GAME_STATE["Currency_Rate_1"] = int(GAME_STATE["Currency_Rate_1"]*0.95)
        GAME_STATE["State"] = "Finance"
        clear()

    # End Finance options












    #LOAD GAME SCREENS BEGIN
    while GAME_STATE["State"] == "Load Game":
        print("load game")
        GAME_STATE["State"] = "Quit"

    if GAME_STATE["State"] == "Quit":
        GAME_STATE["isRunning"] = False
