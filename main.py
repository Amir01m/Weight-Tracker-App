#==========files defs ========== 
def file_daily(w):
    
    try:
        with open("weight_daily.txt",'r') as f:
            lines = f.readlines()
        with open("weight_daily.txt",'a') as f:
            f.write(f"day {int(len(lines))+1} ==> {w} KG\n")
    except FileNotFoundError or FileExistsError:
        with open("weight_daily.txt",'w') as f:
            f.write(f"day 1 ==> {w} KG\n")

def show_file_daily():
    
    try:
        with open("weight_daily.txt",'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
        a = input("for back to menu enter 'm' :")
        if a == 'm':
            return menu()
        else:
            return menu()
    except FileNotFoundError or FileExistsError:
        print("you dont have daily weight please add somthing...")
        while True:
            answer = input("for add enter 'a'  and for retuning to menu enter 'm'.")
            if answer.lower() == "a":
                return daily_weight()
            elif answer.lower() == "m":
                return menu()
            else:
                print("Error...please enter 'a' or 'm'.")
            


#====================== menu defs ======================

#==================================daily weight def==================================

def daily_weight():
    while True:
        w = input("Enter your weight:")
        try:
            w = int(w)
            if w < 18 or w > 640:
                print("please enter your real weight...")
                return daily_weight()
        except :
            print("please enter your real weight....")
            return daily_weight()
        
        file_daily(w)
        return menu()
#==================================weight goal def==================================

def weight_goal():
    while True:
        answer = input("do you want to change your goal? (y/n):")
        if answer.lower() == "y":
            w = input("Enter is your weight goal:")
            with open("goal_weight.txt",'w') as f :
                f.write(w)
            print("your goal changed...returning to menu.")
            return menu()
        elif answer.lower() == "n":
            print("returning to menu...")
            return menu()
        else:
            print("please enter (y/n)...")


#==================================progress def==================================

def progress():
    try:
        with open("weight_daily.txt",'r') as f:
            lines = f.readlines()
            last_line = lines[len(lines)-1]
            print(f"your weight is : {last_line}")
        with open("goal_weight.txt",'r') as g:
            goal = g.readline()
            print("your goal is ",goal)
        w = int(goal) - int(last_line[9:12])
        if w < 0 :
            print(f"you have {abs(w)} KG to gain.")
        else:
            print(f"you have {abs(w)} KG to lose.")
        a = input("for return to menu enter any key:")
        if a == "e":
            pass
        else:
            return menu()
    except:
        print("please add weight....")
        return menu()

#==================================menu def==================================
def menu():
    print("""
    1.daily weight
    2.change your weight goal
    3.show all daily weight
    4.your progress
    5.for exit      
""")
    
    while True:
        action = input("Enter your action:")
        if action == "1":
            return daily_weight()
        elif action == "2":
            return weight_goal()
        elif action == "3":
            return show_file_daily()
        elif action == "4":
            return progress()
        elif action == "5" or action.lower() == "e":
            print("exit...")
            break 
        else:
            print("please enter one of the action.")


menu()