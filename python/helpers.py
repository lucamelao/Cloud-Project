# Imports
import subprocess
import json


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

    def set_infra(self):
        x = [str(x) for x in input("Set as many params as you want for your infrastructure: ").split()]
        
        # Set variables
        keys = x[0::2]
        values = x[1::2]
        dictionary = dict(zip(keys, values))
        
        dictionary["username"] = input("Set your username: ")
        dictionary["instance_type"] = "t1.micro" if dictionary["instance_type"].upper() == "A" else "t2.micro"
        #dictionary["instance_type"] = input("\n1. Select a instance option: \n\n  A. t1.micro \n\n  B. t2.micro \n\n")
        dictionary["instance_name"] = input("\n2. Type your instance name: ")

        print("\n Below you can see the selected parameters for your infrastructure:\n")
        print(f"\n {dictionary}\n")
        
        # Serializing 
        json_object = json.dumps(dictionary, indent=0)

        with open("out.json", "w") as output_file:
            output_file.write(json_object)

    def build_infra(self):
        print(f"\nNow let's create your Private Cloud...\n")
        print("=======================================================================================================================================\n")  
        print("VALIDATING YOUR INFRASTRUCTURE\n")
        subprocess.run(["terraform", "validate"])
        print("=========================================================\n")
        print("PLANNING\n")
        subprocess.run(["terraform", "plan", "-out", "tfplan.out", "-var-file=my.tfvars.json"])
        print("=========================================================\n")
        print("APPLYING\n")
        subprocess.run(["terraform", "apply", "tfplan.out"])

class List_Terraform:

    '''
    Essa classe lista os recursos criados pelo Terraform.
    '''
    
    def list(self):
        print("LISTING YOUR INFRASTRUCTURE...\n")
        subprocess.run(["terraform", "show"])

class Destroy_Terraform:

    '''
    Essa classe destrói os recursos criados pelo Terraform.
    '''
    
    def destroy(self):
        print("Destroying your infrastructure...\n")
        subprocess.run(["terraform", "destroy", "-auto-approve", "-var-file=my.tfvars.json"])

class Quit_Terraform:

    '''
    Classe responsável por encerrar o programa.
    '''
    def end(self):
        print("Goodbye!")
        exit()