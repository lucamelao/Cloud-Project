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

# Create aws iam user
resource "aws_iam_user" "my_iam_user" {
  for_each = toset(var.iam_users)
  name     = each.value
}

resource "aws_instance" "web_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type

  #disable_api_termination = true

  tags = var.instance_tags
}

# Create a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  tags       = var.vpc_tags
  # change default behaviour of the resource
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_subnet" "mypublic_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = var.subnet_cidr_block
  tags       = var.subnet_tags
}

# Create an Internet Gateway
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags   = var.igw_tags
}

# Create a second route table
resource "aws_route_table" "second_route_table" {
  vpc_id = aws_vpc.my_vpc.id
  route {
    cidr_block = var.route_table_cidr_block
    gateway_id = aws_internet_gateway.my_igw.id
  }

  tags = var.second_route_table_tags
}

# Create a route table association
resource "aws_route_table_association" "pulic_subnet_table_association" {
  subnet_id      = aws_subnet.mypublic_subnet.id
  route_table_id = aws_route_table.second_route_table.id
}

resource "aws_security_group" "my_security_group" {
  name = var.security_group_name

  ingress {
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

  tags = var.security_group_tags
}