'''
Esse file escreve o nosso my.tfvars.json recebendo inputs do usuário.
Com o arquivo estruturado, ele executa os comandos do Terraform para criar a infraestrutura.
'''

# Imports
import subprocess
import json

# Desgin
with open("start_image.txt", 'r') as f:
    print(f.read())

# Taking multiple inputs
x = [str(x) for x in input("Set as many params as you want for your infrastructure: ").split()]
# print("List: ", x)

# Set variables
keys = x[0::2]
values = x[1::2]
dictionary = dict(zip(keys, values))

print("\n Below you can see the selected parameters for your infrastructure:\n")
print(f"\n {dictionary}\n")

# Escreve no my.tfvars.json

# Serializing 
json_object = json.dumps(dictionary, indent=0)

# Writing 
with open("test_vars.json", "w") as output_file:
    output_file.write(json_object)

print(f"\nNow let's create your infrastructure...\n")
print(f"=======================================================================================================================================\n")

# Executa comandos no Terminal
# subprocess.call(['sh', './script.sh'])     