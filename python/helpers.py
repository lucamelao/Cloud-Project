# Imports
from python.resources import Infrastructure
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

        infra = Infrastructure()

        infra.user()
        infra.vpc()
        infra.subnet()
        infra.security_group()
        infra.instance()

        with open('resources.json', 'r') as f:
            infra_data = json.load(f)

            with open("test.tfvars.json", "w") as output_file:
                json.dump(infra_data, output_file, indent=4)

    def build_infra(self):

        subprocess.call(['sh', './shell_scripts/init.sh'])
        print(f"\nNow let's create your Private Cloud...\n")

        
        print("VALIDATING YOUR INFRASTRUCTURE\n")
        subprocess.call(['sh', './shell_scripts/validate.sh'])

        print("===================================================================\n")

        print("PLANNING\n")
        subprocess.call(['sh', './shell_scripts/plan.sh'])

        print("===================================================================\n")

        while True:
            apply = input('Apply? [Y]es or [N]o: ').upper()
            if apply == 'Y':
                print("\nAPPLYING\n")
                try:
                    res = subprocess.call(['sh', './shell_scripts/apply.sh'])
                    print("===================================================================\n")
                    print("Your infrastructure is ready!\n")
                    break
                except res == 0:
                    print("===================================================================\n")
                    print("Something went wrong. Implementing again...\n")
                    subprocess.call(['sh', './shell_scripts/apply.sh'])

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
        res = subprocess.call(['sh', './shell_scripts/destroy.sh'])
        if res == 0:
            print("===================================================================\n")
            print("Your infrastructure was destroyed.\n")
        else:
            print("===================================================================\n")
            print("Something went wrong. Destroying again...\n")
            subprocess.call(['sh', './shell_scripts/destroy.sh'])

class Quit_Terraform:

    '''
    Classe responsável por encerrar o programa.
    '''
    def end(self):
        print("Closing User Interface\n")
        exit()