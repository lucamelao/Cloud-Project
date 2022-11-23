'''

FUNCIONALIDADES
- Criar um arquivo .tfvars.json com os inputs do usuário - INFRA
    1. tipo da instancia, no minimo 2 disponiveis
    2. nome da instancia
    3. user
- Listar instancias
    OBS: security group default na porta 22, tem que listar seu conteudo
- Destruir instancias

'''
from python.helpers import UI, Build_Terraform, List_Terraform, Destroy_Terraform, Quit_Terraform

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