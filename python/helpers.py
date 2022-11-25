# Imports
import subprocess
import json

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

class UI:
    def draw_header(self):
        with open("start_image.txt", 'r') as f:
            print(f.read())
    def show_options(self):
        print("Options: \n\n  1. [B]uild \n\n  2. [L]ist \n\n  3. [D]estroy \n\n  4. [Q]uit \n") 

class Build_Terraform:

    '''
    Essa classe escreve o my.tfvars.json recebendo inputs do usuário.
    Com o arquivo estruturado, ele executa os comandos do Terraform para criar a infraestrutura.
    
    '''

    # CONSERTAR
    #instance_name
    #vpc_name_tag
    
    def set_infra(self):
        dictionary = {}

        # User
        dictionary["iam_users"] = [str(x) for x in input("Set your IAM usernames: ").split()]
        
        # VPC
        vpc_tags_dict = {}
        vpc_tags_dict["Name"] = str(input("\n3. Type your VPC name: "))
        dictionary["vpc_tags"] = vpc_tags_dict

        # Instance 
        dictionary["instance_type"] = input("\n1. Select a instance option: \n\n  A. t1.micro \n\n  B. t2.micro \n\n")
        dictionary["instance_type"] = "t1.micro" if dictionary["instance_type"].upper() == "A" else "t2.micro"

        instance_tags_dict = {}
        instance_tags_dict["Name"] = input("\n2. Type your instance name: ")
        instance_tags_dict["Owner"] = input("\n3. Type your name: ")
        dictionary["instance_tags"] = instance_tags_dict
        
        # Security Group
        dictionary["security_group_name"] = input("\n4. Type your Security Group name: ")

        print("\n Below you can see the selected parameters for your infrastructure:\n")
        print(f"\n {dictionary}\n")
        
        # Serializing 
        json_object = json.dumps(dictionary, indent=0)

        with open("test.tfvars.json", "w") as output_file:
            output_file.write(json_object)

    def build_infra(self):
        print(f"\nNow let's create your Private Cloud...\n")
        print("=======================================================================================================================================\n")  
        print("VALIDATING YOUR INFRASTRUCTURE\n")
        subprocess.run(["terraform", "validate"])
        print("===================================================================\n")
        print("PLANNING\n")
        subprocess.run(["terraform", "plan", "-out", "tfplan.out", "-var-file=test.tfvars.json"])
        print("===================================================================\n")
        while True:
            apply = input('Apply? [Y]es or [N]o: ').upper()
            if apply == 'Y':
                print("\nAPPLYING\n")
                subprocess.run(["terraform", "apply", "tfplan.out"])    
                break
            elif apply == 'N':
                print("Operation canceled.\n")
                break
            else:
                print("Invalid option, try again.\n")

class List_Terraform:

    '''
    Essa classe lista os recursos criados pelo Terraform.
    '''
    
    def list(self):
        print("===================================================================\n")
        print("LISTING YOUR INFRASTRUCTURE...\n")
        subprocess.run(["terraform", "show"])

class Destroy_Terraform:

    '''
    Essa classe destrói os recursos criados pelo Terraform.
    '''
    
    def destroy(self):
        print("===================================================================\n")
        print("Destroying your infrastructure...\n")
        subprocess.run(["terraform", "terraform", "-auto-approve", "-var-file=test.tfvars.json"])

class Quit_Terraform:

    '''
    Classe responsável por encerrar o programa.
    '''
    def end(self):
        print("Closing User Interface\n")
        exit()