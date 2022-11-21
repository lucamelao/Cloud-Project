aws_region = "us-east-1"

instance_ami = "ami-08c40ec9ead489470"

instance_type = "t3.micro"

vpc_cidr_block = "10.0.0.0/16"

vpc_tags = {
  Name    = "VsC"
  Project = "Projeto Cloud 2022"
}

subnet_tags = {
  Name = "My Subnet Name"
}

subnet_cidr_block = "10.0.1.0/24"

instance_tags = {
  Name    = "Ubuntu"
  Project = "Projeto Cloud 2022"
}

ingress_from_port = 43

ingress_to_port = 43

ingress_protocol = "tcp"

egress_from_port = 0

egress_to_port = 0

egress_protocol = "-1"

egress_cidr_blocks = ["0.0.0.0/0"]