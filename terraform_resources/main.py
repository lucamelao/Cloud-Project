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
        option = input("\nChoose an option: ").upper()
    
        if option == "B":
            initial_input = True
            backup = B.set_infra()
            B.build_infra(backup)
            break

        elif option == "L":
            initial_input = True
            L.list()  

        elif option == "D":
            initial_input = True
            D.destroy()   

        elif option == "Q":
            initial_input = True
            Q.end()   

        else:
            print(f"{COLORS.WARNING}[WARNING] Invalid input. Please try again.\n{COLORS.ENDC}")
