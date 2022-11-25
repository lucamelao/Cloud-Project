''''
Main file, execute to run the User Interface.
'''

from python.helpers import *

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
    
        if option == "B":
            initial_input = True
            B.set_infra()
            B.build_infra()
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
            print("[ERROR] Invalid input. Please try again.\n")