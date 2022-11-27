''''
Main file, execute to run the User Interface.
'''

from python.actions import *
from python.design import *
from python.design import *

user_interface = UI()
B = Build_Terraform()
L = List_Terraform()
D = Destroy_Terraform()
Q = Quit_Terraform()

user_interface.draw_header()

while True:
    initial_input = False
    while not initial_input:
        user_interface.show_options()
        option = input("Choose an option: ").upper()
    
        if option == "B" or option == "1":
            initial_input = True
            backup = B.set_infra()
            B.build_infra(backup)
            break

        elif option == "L" or option == "2":
            initial_input = True
            L.list()  
            break

        elif option == "D" or option == "3":
            initial_input = True
            D.destroy()   
            break

        elif option == "Q" or option == "4":
            initial_input = True
            Q.end()   

        else:
            print(f"{COLORS.WARNING}[WARNING] Invalid input. Please try again.\n{COLORS.ENDC}")
