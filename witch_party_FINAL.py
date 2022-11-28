print("Greetings and welcome. There's a story about a witch that's on her way to her first \nCoven meeting ")
print("and I'd like to share it with you. I do, however, need you to answer some questions \nfirst before we start. ")
print("Make sure that you press the 'Enter' key after you answer each question. ")
input("\nPress the enter key to continue............")

goAgain = "y"
while goAgain.lower() == "y":


    witchName = input("\nWhat is the witch's name? ")
    is_Int = True
    try:
        int(witchName)
    except ValueError:
        is_Int = False
    if is_Int:
        witchName = input("\nYou entered a number. Please enter a name:  ")
    else:
        continue

    while (len(witchName.lower()) == 0):
            witchName = input("Please enter a name: ")

    witchAge = input("How old is the witch? ")
    is_Str = True
    try:
        str(witchAge)
    except ValueError:
        is_Str = False
    if is_Str:
        witchAge = input("\nYou entered a letter. Please enter a numeric value:  ")
    else:
        continue
    if witchAge == "0":
        witchAge = input("Age cannot be 0, please enter an age: ")
    else:
        continue

    while (len(witchAge.lower()) == 0):
        witchAge = input("Please enter an age: ")
       
    witchHair = input("What color is her hair? ")
    is_Int = True
    try:
        int(witchHair)
    except ValueError:
        is_Int = False
    if is_Int:
        witchHair = input("\nYou entered a number. Please enter a color:  ")
    else:
        continue
    while (len(witchHair.lower()) == 0):
        witchHair = input("Please enter what the witch's hair color is: ")


    forestName = input("What is the name of the forest? ")
    is_Int = True
    try:
        int(forestName)
    except ValueError:
        is_Int = False
    if is_Int:
        forestName = input("\nYou entered a number. Please enter a name:  ")
    else:
        continue
    while (len(forestName.lower()) == 0):
        forestName = input("Please enter the name of the forest: ")


    witchFamiliar = input("What type of familiar will she have with her? ")
    is_Int = True
    try:
        int(witchFamiliar)
    except ValueError:
        is_Int = False
    if is_Int:
        witchFamiliar = input("\nYou entered a number. Please enter what type of familiar the witch will have:  ")
    else:
        continue
    while (len(witchFamiliar.lower()) == 0):
        witchFamiliar = input("Please enter what kind of familiar the witch will have: ")

    witchFamiliar_name = input("What is the familiar's name? ")
    is_Int = True
    try:
        int(witchFamiliar_name)
    except ValueError:
        is_Int = False
    if is_Int:
        witchFamiliar_name = input("\nYou entered a number. Please enter a name:  ")
    else:
        continue
    while (len(witchFamiliar_name.lower()) == 0):
        witchFamiliar_name = input("Please enter the familiar's name: ")

    magic = input("What type of magic will the witch specialize in? ")
    is_Int = True
    try:
        int(magic)
    except ValueError:
        is_Int = False
    if is_Int:
        magic = input("\nYou entered a number. Please enter what type of magic the witch will specialize in:  ")
    else:
        continue
    while (len(magic.lower()) == 0):
        magic = input("Please enter what type of magic the witch will specialize in: ")

    print("\nLet us begin..... ")

    print("\nThere was a witch, by the name of", witchName + ". She is " + witchAge + " with " + 
    witchHair + " hair and has a " + witchFamiliar + " with her named " + witchFamiliar_name + ". "
    )
    print(witchName + " just joined a coven but she must make it through " + forestName + " \nforest in order to get to her Initiation Ceremony. ")
    print("She plans on specializing in " + magic + " magic. " + forestName + " forest has many perils that could mislead or trap her, \nso she must be careful. ")

    pathA = input("\nShould " + witchName + " and " + witchFamiliar_name + " take Path A?  yes or no:  ")

    if pathA == "yes":
        print("\n" + witchName + " looks at the paths they can choose from and decides to try the first path on the left. ")
        print(witchName + " and " + witchFamiliar_name + " start down this path attempting to be completely aware of their surroundings. ")
        print(witchFamiliar_name + " trots ahead of " + witchName + " and falls into a pitfall trap! ")
        print(witchName + " helps " + witchFamiliar_name + " out of the trap with a vine she finds nearby. ")
        print("Suddenly, goblins spring from behind the trees and start to chase " + witchName + " and " + witchFamiliar_name + ". ")
        print("They get away from the goblins just in time! ")

        tryAgain = input("\nWould you like " + witchName + " and " + witchFamiliar_name + " to choose another path? yes or no:  ")
        
        if tryAgain == "yes":
            pathB = input("\nShould " + witchName + " and " + witchFamiliar_name + " take Path B?  yes or no:  ")
            if pathB == "yes":
                print("\n" + witchName + " approachs " + forestName + " forest with her faithful " + witchFamiliar + " at her side. ")
                print(witchName + " chooses the second one from the left. ")
                print("That path leads " + witchName + " and " + witchFamiliar_name + " to a griffin's nest! ")
                print("There's a mother griffin and three babies in the nest sleeping. They back up slowly, so the griffins don't wake up. ")
                print("Looks like " + witchName + " and " + witchFamiliar_name + " will have to choose a different path. ")
            
                tryAgain = input("\nWould you like " + witchName + " and " + witchFamiliar_name + " to choose another path? yes or no:  ")
            
                if tryAgain == "yes":
                    pathC = input("\nShould " + witchName + " and " + witchFamiliar_name + " take Path C?  yes or no:  ")
                    if pathC == "yes":
                        print("\n" + witchFamiliar_name + " licked at " + witchName + "'s hands as they sat at the beginning of the paths. ")
                        #print("Seeing her mother made her sad, " + witchName + " had only seen pictures of her mother and wished that she hadn't died. ")
                        print("The " + witchFamiliar + " rubbed on " + witchName + "'s legs and went toward the third path from the left. ")
                        #print(witchName + " shrugged thinking that if this path wasn't the right one, then, they only had one other choice. ")
                        #print(witchFamiliar_name + " ran ahead of " + witchName + ", romping playfully trying to cheer her up. ")
                        print("Suddenly, a ghost-like figure appeared through the trees! The ghost came quickly towards " + witchName + " " + witchFamiliar_name + ", shrieking awful noises! ")
                        print(witchName + " and " + witchFamiliar_name + " ran back to the beginning of " + forestName + " forest. " )

                        tryAgain = input("\nWould you like " + witchName + " and " + witchFamiliar_name + " to choose another path? yes or no:  ")
        
                        if tryAgain == "yes":
                            pathD = input("\nShould " + witchName + " and " + witchFamiliar_name + " take Path D?  yes or no:  ")
                            if pathD == "yes":
                                print("\n" + witchName + " and " + witchFamiliar_name + " stand in front of " + forestName + " forest and the " + witchFamiliar + " points towards the fourth path from the left, this time. ")
                                print("As they go down the path, their surroundings start to get foggy, misty, and windy. ")
                                print(witchName + " brushes her " + witchHair + " hair out of her face, when suddenly, a person appears through the mist. ")
                                print("It looks like " + witchName + "'s mother! ")
                                print("How could that be when " + witchName + "'s mother died giving birth to her? ")
                                print("It must be a mirage trying to trick them. " + witchName + " and " + witchFamiliar_name + " go back to the beginning. ")
                            
                                tryAgain = input("\nWould you like " + witchName + " and " + witchFamiliar_name + " to choose another path? yes or no:  ")
                                
                                if tryAgain == "yes":
                                    pathE = input("\nShould " + witchName + " and " + witchFamiliar_name + " take Path E?  yes or no:  ")
                                    if pathE == "yes":
                                        #print("\nSince " + witchName + " and " + witchFamiliar_name + " had exhausted all of their options, the first path on the right had to be the right one. ")
                                        print("\n" + witchName + " started down the path with " + witchFamiliar_name + " running after her. ")
                                        print("The " + witchFamiliar + " started chasing the leaves that swirled around their feet in the night wind. ")
                                        print("The path wound, went up over a slight hill and as " + witchName + " and " + witchFamiliar_name + " reached the top, there was an orange radiance. ")
                                        print("Being cautious, " + witchName + " slowly poked her " + witchHair + "-haired head above the crest of the hill to see where the light was coming from. ")
                                        print("It was a bonfire with all her new coven sisters surrounding the bright light of the fire. ")
                                        print(witchName + " and " + witchFamiliar_name + " had made it to the Initiation Ceremony! ")
                                    else:
                                        altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                                        if altEnding1 == "yes":
                                            print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                                            print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                                            print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                                        else:
                                            altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                                            if altEnding2 == "yes":
                                                print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell. ")
                                                print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                                            else:
                                                print(" ")
                                else:
                                    altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                                    if altEnding1 == "yes":
                                        print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                                        print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                                        print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                                    else:
                                        altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                                        if altEnding2 == "yes":
                                            print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                                            print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                                        else:
                                            print(" ")

                            else:
                                altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                                if altEnding1 == "yes":
                                    print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                                    print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                                    print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                                else:
                                    altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                                    if altEnding2 == "yes":
                                        print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                                        print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                                    else:
                                        print(" ")

                        else:
                            altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                            if altEnding1 == "yes":
                                print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                                print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                                print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                            else:
                                altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                                if altEnding2 == "yes":
                                    print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                                    print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                                else:
                                    print(" ")

                    else:
                        altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                        if altEnding1 == "yes":
                            print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                            print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                            print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                        else:
                            altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                            if altEnding2 == "yes":
                                print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                                print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                            else:
                                print(" ")

                else:
                    altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                    if altEnding1 == "yes":
                        print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                        print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                        print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                    else:
                        altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                        if altEnding2 == "yes":
                            print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                            print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                        else:
                            print(" ")

            else:
                altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
                if altEnding1 == "yes":
                    print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                    print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                    print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
                else:
                    altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                    if altEnding2 == "yes":
                        print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                        print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                    else:
                        print(" ")

        else:
            altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
            if altEnding1 == "yes":
                print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
                print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
                print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
            else:
                altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
                if altEnding2 == "yes":
                    print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                    print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
                else:
                    print(" ")

    else:
        altEnding1 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to fly over the forest instead? yes or no: ")
        if altEnding1 == "yes":
            print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a spell and fly over " + forestName + " forest. ")
            print("As " + witchName + " and " + witchFamiliar_name + " soar over the forest, they see an orange glow over the treetops. ")
            print("Standing around a big bonfire are all of " + witchName + "'s new coven sisters. " + witchName + " and " + witchFamiliar_name + " have arrived at the Initiation Ceremony! ")
        else:
            altEnding2 = input("Would you like " + witchName + " and " + witchFamiliar_name + " to use a transportation spell, instead? yes or no: ")
            if altEnding2 == "yes":
                print("\nInstead of choosing a path, " + witchName + " and " + witchFamiliar_name + " use a transportation spell instead. ")
                print(witchName + " says,'Me fugere ubi opus sit' and " + witchFamiliar_name + " and her are instantly taken to the Initiation Ceremony! ")
            else:
                print(" ")

goAgain = input("\nWould you like to play again? yes or no:  ")
while goAgain.lower() != "yes" and goAgain.lower() != "no":
    goAgain = input("Please enter yes or no:  ")      
    
