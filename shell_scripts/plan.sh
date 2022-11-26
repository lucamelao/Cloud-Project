cd ../terraform_resources
terraform plan -out "tfplan.out" -var-file="my.tfvars.json"