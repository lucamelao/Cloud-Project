# Imports
from resources import Infrastructure
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

    infra = Infrastructure()
    
    def set_infra(self, infra):
        infra.user()
        infra.vpc()
        infra.subnet()
        infra.security_group()
        infra.instance()

        with open("test.tfvars.json", "w") as output_file:
            output_file.write('resources.json')

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
                subprocess.call(['sh', './shell_scripts/apply.sh'])
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
        # subprocess.run(["terraform", "terraform", "-auto-approve", "-var-file=test.tfvars.json"])

class Quit_Terraform:

    '''
    Classe responsável por encerrar o programa.
    '''
    def end(self):
        print("Closing User Interface\n")
        exit()