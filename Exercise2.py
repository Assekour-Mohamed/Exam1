 def CalculateMonthlyCosts(duration):
    Plans=[0,0,0,0]
    
    Plans[0] = duration * 2
    Plans[1] = (duration - 30) * 1.5
    Plans[2] = (duration - 60) * 1
    Plans[3] = (duration - 120 ) * 0.5

    return Plans

def askUser(message):
    ansewr = input(message)
    return ansewr

 ## MAIN PROGRAM ##

def main():
    duration = 0
    Plans=[]
    while(True):
        menu ='''
        ----------Menu------------
        1- Saisir la durée de communication
        2- Afficher la liste du côut mensuelle par offre
        3- Afficher l’offre la plus intéressante (moindre coût)
        4- Quitter le programme 
        --------------------------
        '''
        print(menu)

        option = askUser("what is your option ? 1 to 4 :")

        MonthlyAmount=[10,20,50,100,200]
        if option == "1":
            duration = float(input("enter your monthly duration in minutes"))
            Plans = CalculateMonthlyCosts(duration)
            
        elif option =="2":
            if duration > 0 :
                print("\n your monthly plans ")
                for i in range(4):
                    print("plan " ,i+1, "costs you ",Plans[i], "(MAD)")
            else :
                print("enter your duration first!!")    

        elif option == "3":
            if duration > 0 :
                print("the most effictive plan is " ,min(Plans)) 
            else :
                print("enter your duration first!!")
               
        elif option == "4":
            if askUser("are you sur n/N y/Y ?") == "y":
                break
        else :
            print("wrong input")
            
        input("pess any key to go to MENU")

main()
