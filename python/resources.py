'''

Aqui são estruturados os resources que o Terraform criará. 

'''

import json

class Infrastructure:

    def user(self):
        # transformar em lista
        usernames = [str(x) for x in input("\nType you username(s) separated by a blank space " ": ").split()]

        with open('my.tfvars.json', 'r') as arquivo:
            content = arquivo.read()
            infra_dict = json.loads(content)
            
        # check if dict is empty
        if infra_dict.get("iam_users") is None:
            infra_dict["iam_users"] = usernames
        else:
            infra_dict["iam_users"].append(usernames)

        with open('my.tfvars.json', 'w') as file:
            json.dumps(infra_dict, file, indent=4)

        print("\nUsers info acquired.")
        print("===========================")


    def vpc(self):

        with open('my.tfvars.json', 'r') as arquivo:
            content = arquivo.read()
            infra_dict = json.loads(content)

        # check if dict is empty
        if infra_dict.get("vpc") is None:
            vpc_tag_name = input("\nType the VPC name: ")
            infra_dict["vpc"] = {
                "cidr_block": "10.0.0.0/16",
                "tags": {
                    "Name": vpc_tag_name
                }}
        else:
            print("\nVPC is OK.")

        print("\nDefault VPC created.")    
        print("===========================")

    def subnet(self):

        subnet_tag_name = input("\nType the subnet name: ")

        with open('my.tfvars.json', 'w') as f:
            json.dump({"subnet_tags": {"name": subnet_tag_name}}, f, indent=4)

        print("\nSubnet info acquired.")
        print("===========================")
    
    def security_group(self):

        security_group_name = input("\nType the Security Group name: ")

        with open('my.tfvars.json', 'r') as f:
            infra_data = json.load(f)

            with open("my.tfvars.json", "w") as output_file:
                json.dump({"security_group_name": security_group_name}, output_file, indent=4)

        print("\nSecurity Group info acquired.")
        print("===========================")

    def instance(self):
        user_choice = input("\n1. Select a instance option: \n\n  A. t1.micro \n\n  B. t2.micro \n\n").upper()
        instance_type = "t1.micro" if user_choice == "A" else "t2.micro"
        
        instance_name = input("\nType the instance name: ")
    
        # Update instances
        with open('my.tfvars.json', 'r') as arquivo:
            content = arquivo.read()
            infra_dict = json.loads(content)
                
        # check if dict is empty
        if infra_dict.get("instances") is None:
            infra_dict["instances"] = [{
                "ami": "ami-08c40ec9ead489470",
                "type": instance_type,
                "network_interface": "NIC 1",
                "device_index": 0,
                "tags": {  
                  "Name": instance_name
                }}]
        else:
            infra_dict["instances"].append({
                "ami": "ami-08c40ec9ead489470",
                "type": instance_type,
                "network_interface": "NIC 1",
                "device_index": 0,
                "tags": {  
                  "Name": instance_name
                }})
        
        with open('my.tfvars.json', 'w') as file:
            json.dumps(infra_dict, file, indent=4)

        print("\nInstances info acquired.")
        print("===========================")

    def network_interface(self):
        # subnet_id = input("\nType the network interface subnet id: ")
        subnet_id = "SUBNET DA UI"
        # private_ip_address = str(input("\nType the network interface private ip address: "))
        private_ip_address = ["10.0.1.4"]
        associated_security_group = str(input("\nType the associated security group: "))
        nic_name = input("\nType the network interface name: ")

        # Update network interfaces
        with open('my.tfvars.json', 'r') as arquivo:
            content = arquivo.read()
            infra_dict = json.loads(content)

        # check if dict is empty
        if infra_dict.get("network_interfaces") is None:
            infra_dict["network_interfaces"] = [{
                "subnet_id": subnet_id,
                "private_ip_address": [private_ip_address],
                "security_groups": [associated_security_group],
                "tags": {
                    "Name": nic_name
                }}]
        else:
            infra_dict["network_interfaces"].append({
                "subnet_id": subnet_id,
                "private_ip_address": [private_ip_address],
                "security_groups": [associated_security_group],
                "tags": {
                    "Name": nic_name
                }})
        
        with open('my.tfvars.json', 'w') as file:
            json.dumps(infra_dict, file, indent=4)

        print("\nNetwork Interface info acquired.")
        print("===========================")
