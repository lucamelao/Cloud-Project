aws_region = "us-east-1"

instance_ami = "ami-08c40ec9ead489470"

instance_type = "t3.micro"

vpc_cidr_block = "10.0.0.0/16"

vpc_tags = {
  Name    = "VPC"
  Project = "Projeto Cloud 2022"
}

#subnet_cidr_block = "10.0.0.0/16"

subnet_tags = {
  Name = "My Subnet Name"
}

#--------------------------------------------

public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]

private_subnet_cidrs = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]

instance_tags = {
  Name    = "Ubuntu"
  Project = "Projeto Cloud 2022"
}