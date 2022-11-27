''''
Arquivo com as possíveis ações que podem ser executadas pelo usuário.
'''

# Imports
from python.resources import Infrastructure
from python.design import COLORS
import subprocess       

class Build_Terraform:

    '''
    Essa classe escreve o my.tfvars.json recebendo inputs do usuário.
    Com o arquivo estruturado, ele executa os comandos do Terraform para criar a infraestrutura.
    '''

    def keyboard_interrupt(self, backup):
        infra = Infrastructure()
        infra.update_infra(backup)
        print(f"{COLORS.FAIL} \nCtrl + C was pressed, all inputs were discarted.\n")


    def set_infra(self):

        infra = Infrastructure()

        # Criando o backup do arquivo my.tfvars.json antes de configurar mudanças na infraestrutura
        backup = infra.get_infra()
        
        try:
            print("===================================================================\n")

            print(f"{COLORS.orange}Let's start building your infrastructure!\nIf you're in doubt about what to type, just press enter to set the values as default.{COLORS.ENDC}")

            infra.region()
            infra.user()
            infra.vpc()
            infra.subnet()
            infra.security_group()
            infra.network_interface()
            infra.instance()

            print(f"{COLORS.OKGREEN}\nConfiguration done!{COLORS.ENDC}")
            print("===================================================================\n")
        
        except KeyboardInterrupt:
            self.keyboard_interrupt(backup)
            exit()

        return backup


    def build_infra(self, backup):

        try:
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
                        subprocess.call(['sh', '../shell_scripts/plan.sh'])
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
                    print(f"{COLORS.WARNING}\nInvalid option, try again.\n{COLORS.ENDC}")
        
        except KeyboardInterrupt:
            self.keyboard_interrupt(backup)
            exit()

class List_Terraform:

    '''
    Essa classe lista os recursos ativos na AWS.
    '''
    
    def list(self):
        print("===================================================================\n")

        infra = Infrastructure()
        information = infra.get_infra()
        
        print(f"{COLORS.BOLD}{COLORS.OKCYAN}Options: \n\n  1. List all active instances \n\n  2. List an specific instance.{COLORS.ENDC}")
        
        user_choice = str(input("\n Choose your option: "))

        # Nessa aplicação, as informações abaixo não são afetadas de acordo com each instance.
        # Pois todas as instâncias são associadas a um VPC padrão e criadas em uma mesma região.
        
        users = information["iam_users"]
        vpc_name = information['vpc']['tags']['Name']
        security_group_name = information['security_groups'][0]['tags']['Name']
        security_groups_ingress_rules = information['security_groups'][0]['ingress']
        security_groups_egress_rules = information['security_groups'][0]['egress']

        if user_choice == '1':
            print("===================================================================\n")
            
            if "instances" not in information:
                print(f"{COLORS.WARNING}You don't have any active instances.\n{COLORS.ENDC}")
            
            else:
            
                active_instances = len(information["instances"])
                print(f"You currently have {active_instances} active instances. You can see their information below:")
    
                print(f"{COLORS.BOLD}{COLORS.OKCYAN}\nListing all active instances.\n{COLORS.ENDC}")
                print("===================================================================\n")
                for instance in information["instances"]:
                    print(f"\n{COLORS.OKCYAN}{COLORS.BOLD}Instance: {instance['tags']['Name']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}VPC: {vpc_name}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Type: {instance['type']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated Security Group: {security_group_name}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated SG Ingress Rules: {security_groups_ingress_rules}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated SG Egress Rules: {security_groups_egress_rules}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Network Interface: {instance['network_interface']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Region: us-east-1\n{COLORS.ENDC}") 
                    print(f"  {COLORS.OKCYAN}Users: {users}\n{COLORS.ENDC}")
                    print("===================================================================\n")
        
        elif user_choice == '2':

            print("===================================================================\n")
            nome = input("Type the name of the specific instance you want to display info: ")
            
            exists = False
            for instance in information["instances"]:
                if instance['tags']['Name'] == nome:
                    exists = True
                    print(f"\n{COLORS.OKCYAN}{COLORS.BOLD}Instance: {instance['tags']['Name']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}VPC: {vpc_name}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Type: {instance['type']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated Security Group: {security_group_name}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated SG Ingress Rules: {security_groups_ingress_rules}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Associated SG Egress Rules: {security_groups_egress_rules}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Network Interface: {instance['network_interface']}\n{COLORS.ENDC}")
                    print(f"  {COLORS.OKCYAN}Region: us-east-1\n{COLORS.ENDC}") 
                    print(f"  {COLORS.OKCYAN}Users: {users}\n{COLORS.ENDC}")
                    print("===================================================================\n")
                    break
            if not exists:
                print(f"{COLORS.WARNING}You don't have any active instances with this name. Try again.\n{COLORS.ENDC}")

class Destroy_Terraform:

    '''
    Essa classe destrói os recursos criados pelo Terraform.
    '''
    
    def destroy(self):
        print("===================================================================\n")
        print("Destroying your infrastructure...\n")
        res = subprocess.call(['sh', '../shell_scripts/destroy.sh'])
        if res != 0:
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