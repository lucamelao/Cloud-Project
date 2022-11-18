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

resource "aws_subnet" "mypublic_subnets" {
  count      = length(var.public_subnet_cidrs)
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = element(var.public_subnet_cidrs, count.index)

  tags = {
    Name = "Public Subnet ${count.index + 1}"
  }
}

resource "aws_subnet" "myprivate_subnets" {
  count      = length(var.private_subnet_cidrs)
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = element(var.private_subnet_cidrs, count.index)

  tags = {
    Name = "Private Subnet ${count.index + 1}"
  }
}