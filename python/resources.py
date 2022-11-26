'''

Aqui são estruturados os resources que o Terraform criará. 

'''

import json

class Infrastructure:

    def user(self):
        usernames = input("\nType you username(s): ")
        with open('resources.json', 'w') as f:
            json.dump({"iam_users": usernames}, f)

        print("\nUsers info acquired.")

    def vpc(self):
        vpc_tag_name = input("\nType the VPC name: ")

        with open('resources.json', 'w') as f:
            json.dump({"vpc": {"vpc_tag_name": vpc_tag_name}}, f, indent=4)

        print("\nVPCs info acquired.")

    def subnet(self):

        subnet_tag_name = input("\nType the subnet name: ")

        with open('resources.json', 'w') as f:
            json.dump({"subnet_tags": {"name": subnet_tag_name}}, f, indent=4)

        print("\nSubnet info acquired.")
    
    def security_group(self):

        security_group_name = input("\nType the Security Group name: ")

        with open('resources.json', 'w') as f:
            json.dump({"security_group_name": security_group_name}, f, indent=4)

        print("\nSecurity Group info acquired.")
        

    def instance(self):
        user_choice = input("\n1. Select a instance option: \n\n  A. t1.micro \n\n  B. t2.micro \n\n").upper()
        instance_type = "t1.micro" if user_choice == "A" else "t2.micro"
        
        instance_tags_dict = {}        
        instance_tags_dict["Name"] = input("\nType the instance name: ")
        instance_tags_dict["Owner"] = input("\nType the isnstance's owner name: ")
    
        associated_security_group = str(input("\nType the associated security group name: "))

        # Update instances
        with open('resources.json', 'r') as infra_data:
            infra_dict = json.load(infra_data)
        
        infra_dict["instances"].append({"instance_type": instance_type, "security_group": associated_security_group, "instance_tags" : instance_tags_dict})
        
        with open('resources.json', 'w') as updated_infra_data:
            json.dump(infra_dict, updated_infra_data, indent=4)

        print("\nInstances info acquired.")