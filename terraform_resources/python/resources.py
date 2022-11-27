'''

Aqui são estruturados os resources que o Terraform criará. 

'''

import json
from python.design import COLORS

class Infrastructure:

    def get_infra(self):
        with open('my.tfvars.json', 'r') as arquivo:
            infra_dict = json.load(arquivo)
            return infra_dict
        
    def update_infra(self, new_infra):
        json_content = json.dumps(new_infra, indent=4)
        with open('my.tfvars.json', 'w') as file:
            file.write(json_content)

    def region(self):
        region = "us-east-1"
        infra_dict = self.get_infra()
        infra_dict["region"] = region
        self.update_infra(infra_dict)
            
    def user(self):
        usernames = [str(x) for x in input("\nType your desired username(s) separated by a blank space " ": ").split()]
        
        infra_dict = self.get_infra()
            
        if "iam_users" in infra_dict.keys():
            infra_dict["iam_users"] += usernames
        else:
            infra_dict["iam_users"] = usernames
        
        self.update_infra(infra_dict)

        print(f"{COLORS.OKGREEN}\nUsers info acquired.{COLORS.ENDC}")
        print("===========================")


    def vpc(self):

        infra_dict = self.get_infra()

        if "vpc" in infra_dict.keys():
            print(f"{COLORS.OKGREEN}\nVPC already created.{COLORS.ENDC}")
            print("===========================")
            return
        
        else:
            print("\nNow let's create your Virtual Private Cloud(VPC).")
            
            vpc_name = input("\nType the VPC name: ")
            if vpc_name == "":
                vpc_name = "VPC do LUCA"
            
            vpc_cidr = input("\nType the VPC CIDR (example: 10.0.0.0/16): ")
            if vpc_cidr == "":
                vpc_cidr = "10.0.0.0/16"

            infra_dict["vpc"] = {
                "cidr_block": vpc_cidr,
                "tags": {
                    "Name": vpc_name
                }
            }
            
            self.update_infra(infra_dict)

            print(f"{COLORS.OKGREEN}\nVPC info acquired.{COLORS.ENDC}")
            print("===========================")

    def subnet(self):

        print("\nNow let's create your subnets.")
        infra_dict = self.get_infra()

        subnet_name = input("\nType the subnet name: ")
        if subnet_name == "":
            subnet_name = "SUBNET LUCA"

        subnet_cidr = input("\nType the subnet CIDR (example: 10.0.1.0/24): ")
        if subnet_cidr == "":
            subnet_cidr = "10.0.1.0/24"

        if "subnets" in infra_dict.keys():
            infra_dict["subnets"].append({
                "cidr_block": subnet_cidr,
                "tags": {
                    "Name": subnet_name
                }
            })
        else:
            infra_dict["subnets"] = [{
                "cidr_block": subnet_cidr,
                "tags": {
                    "Name": subnet_name
                }
            }]
        
        self.update_infra(infra_dict)

        print(f"{COLORS.OKGREEN}\nSubnet info acquired.{COLORS.ENDC}")
        print("===========================")
    
    def security_group(self):

        '''
        O security group será default, sendo criado para estar associado a instância.
        '''
        
        print("\nNow let's set your security group.")

        infra_dict = self.get_infra()

        # security_group_name = input("\nType the Security Group name: ")
        # if security_group_name == "":
        security_group_name = "SG LUCA"

        # SG_description = input("\nType the Security Group description: ")
        # if SG_description == "":
        SG_description = "This is a default description."
        
        # ingress_from_port = input("\n[INGRESS]Type the from port: ")
        # if ingress_from_port == "":
        ingress_from_port = "22"
        
        # ingress_to_port = input("\n[INGRESS]Type the to port: ")
        # if ingress_to_port == "":
        ingress_to_port = "22"

        # ingress_protocol = input("\n[INGRESS]Type the protocol: ")
        # if ingress_protocol == "":
        ingress_protocol = "tcp"

        # ingress_cidr = input("\n[INGRESS]Type the CIDR: ")
        # if ingress_cidr == "":
        ingress_cidr = "0.0.0.0/0"

        # eggress_from_port = input("\n[EGGRESS]Type the from port: ")
        # if eggress_from_port == "":
        eggress_from_port = "0"

        # eggress_to_port = input("\n[EGGRESS]Type the to port: ")
        # if eggress_to_port == "":
        eggress_to_port = "0"
        
        eggress_protocol = "-1"

        # eggress_cidr = input("\n[EGGRESS]Type the CIDR: ")
        # if eggress_cidr == "":
        eggress_cidr = "0.0.0.0/0"
            
        # name_tag = input("\nType the name tag: ")
        # if name_tag == "":
        name_tag = "SECURITY GROUP DO LUCA"

        
        if "security_groups" in infra_dict.keys():
            return
        else:
            infra_dict["security_groups"] = [{
                "name": security_group_name,
                "description": SG_description,
                "ingress": {
                    "from_port": ingress_from_port,
                    "to_port": ingress_to_port,
                    "protocol": ingress_protocol,
                    "cidr_blocks": [ingress_cidr]
                },
                "egress": {
                    "from_port": eggress_from_port,
                    "to_port": eggress_to_port,
                    "protocol": eggress_protocol,
                    "cidr_blocks": [eggress_cidr]
                },
                "tags": {
                    "Name": name_tag
                }
            }]

        self.update_infra(infra_dict)
        
        print(f"{COLORS.OKGREEN}\nSecurity Group established.{COLORS.ENDC}")
        print("===========================")

    def network_interface(self): 

        print("\nNow let's create your network interface.")
        print("\nIt will be attached to your instance.")

        infra_dict = self.get_infra()

        subnet_id = infra_dict["subnets"][0]["tags"]["Name"]

        
        private_ip_address = input("\nType the private IP address (example: 10.0.1.4): ")
        if private_ip_address == "":
            private_ip_address = "10.0.1.4"
        
        security_groups = infra_dict["security_groups"][0]["tags"]["Name"]
        
        nic = input("\nType the network interface name (example: NIC 1): ")
        if nic == "":
            nic = "NIC 1"

        if "network_interface" in infra_dict.keys():
            infra_dict["network_interface"].append({
                "subnet_id": subnet_id,
                "private_ip_address": private_ip_address,
                "security_groups": [security_groups],
                "tags": {
                    "Name": nic
                }
            })
        else:
            infra_dict["network_interface"] = [{
                "subnet_id": subnet_id,
                "private_ip_address": [private_ip_address],
                "security_groups": [security_groups],
                "tags": {
                    "Name": nic
                }
            }]

        self.update_infra(infra_dict)

        print(f"{COLORS.OKGREEN}\nNetwork Interface established.{COLORS.ENDC}")
        print("===========================")

    def instance(self):

        print("\nNow let's create your instance.")

        infra_dict = self.get_infra()

        while True:
            user_choice = input("\nSelect a instance size: \n\n  A. t1.micro \n\n  B. t2.micro \n\n").upper()
            if user_choice == "A":
                instance_type = "t1.micro"
                break
            elif user_choice == "B":
                instance_type = "t2.micro"
                break
            else:
                print("\nInvalid option. Please, try again.")
        
        instance_name = input("\nType the instance name: ")
        if instance_name == "":
            instance_name = "INSTANCE LUCA"

        ami = "ami-08c40ec9ead489470"
        network_interface = infra_dict["network_interface"][0]["tags"]["Name"]
        device_index = 0

        if "instances" in infra_dict.keys():
            infra_dict["instances"].append({
                "ami": ami,
                "type": instance_type,
                "network_interface": network_interface,
                "device_index": device_index,
                "tags": {
                    "Name": instance_name
                }
            })
        else:
            infra_dict["instances"] = [{
                "ami": ami,
                "type": instance_type,
                "network_interface": network_interface,
                "device_index": device_index,
                "tags": {
                    "Name": instance_name
                }
            }]

        print(f"{COLORS.OKGREEN}\nInstances info acquired.{COLORS.ENDC}")
        print("===========================")