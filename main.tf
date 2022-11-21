terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.39.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "web_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type

  tags = var.instance_tags
}

resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  tags = var.vpc_tags
}

resource "aws_subnet" "mypublic_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = var.subnet_cidr_block

  tags = {
    Name = "Luca's Public Subnet"
  }
}

resource "aws_security_group" "my_security_group" {
  name        = "Luca Security Group"
  description = "Testing security group"
  vpc_id      = aws_vpc.my_vpc.id

  ingress {
    description = "TLS from VPC"
    from_port   = var.ingress_from_port
    to_port     = var.ingress_to_port
    protocol    = var.ingress_protocol
    cidr_blocks = [aws_vpc.my_vpc.cidr_block]
  }

  egress {
    from_port   = var.egress_from_port
    to_port     = var.egress_to_port
    protocol    = var.egress_protocol
    cidr_blocks = var.egress_cidr_blocks
  }

  tags = {
    Name = "Test Security Group"
  }
}