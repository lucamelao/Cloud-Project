# Imports
from python.resources import Infrastructure
from python.design import COLORS, UI

import subprocess       

class Build_Terraform:

    '''
    Essa classe escreve o my.tfvars.json recebendo inputs do usuário.
    Com o arquivo estruturado, ele executa os comandos do Terraform para criar a infraestrutura.
    
    '''

    def set_infra(self):

        print("===================================================================\n")
        print("Let's start building your infrastructure!\nIf you're in doubt about what to type, just press enter to set the values as default.\n")

        infra = Infrastructure()

        # Criando o backup do arquivo my.tfvars.json antes de configurar mudanças na infraestrutura
        backup = infra.get_infra()

        infra.region()
        infra.user()
        infra.vpc()
        infra.subnet()
        infra.security_group()
        infra.network_interface()
        infra.instance()

        print(f"{COLORS.OKGREEN}\nConfiguration done!{COLORS.ENDC}")
        print("===================================================================\n")
        return backup


    def build_infra(self, backup):

        print("Initializing Terraform")
        subprocess.call(['sh', '../shell_scripts/init.sh'])
        print("===================================================================\n")

        print("VALIDATING YOUR INFRASTRUCTURE\n")
        subprocess.call(['sh', '../shell_scripts/validate.sh'])

        print("===================================================================\n")

        print("PLANNING\n")
        subprocess.call(['sh', '../shell_scripts/plan.sh'])

        print("===================================================================\n")

        while True:
            apply = input('Apply? [Y]es or [N]o: ').upper()
            if apply == 'Y':
                print("\nAPPLYING\n")
                res = subprocess.call(['sh', '../shell_scripts/apply.sh'])
                if res != 0:
                    print("===================================================================\n")
                    print("Something went wrong. Implementing again...\n")
                    subprocess.call(['sh', '../shell_scripts/apply.sh'])
                else:
                    print("===================================================================\n")
                    print("Your infrastructure is ready!\n")
                    break
            elif apply == 'N':
                print("\nOperation canceled.\n")

                # Resetando o arquivo my.tfvars.json para o backup
                infra = Infrastructure()
                infra.update_infra(backup)

                print(f"{COLORS.FAIL}All the inputed values were dropped.\n{COLORS.ENDC}")
                break
            else:
                print(f"{COLORS.WARNING}Invalid option, try again.\n{COLORS.ENDC}")

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
        res = subprocess.call(['sh', '../shell_scripts/destroy.sh'])
        if res == 0:
            print("===================================================================\n")
            print("Your infrastructure was destroyed.\n")
        else:
            print("===================================================================\n")
            print("Something went wrong. Destroying again...\n")
            subprocess.call(['sh', '../shell_scripts/destroy.sh'])

class Quit_Terraform:

    '''
    Classe responsável por encerrar o programa.
    '''
    def end(self):
        print("Closing User Interface\n")
        exit()