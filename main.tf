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