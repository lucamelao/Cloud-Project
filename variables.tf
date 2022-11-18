variable "aws_region" {
  type        = string
  description = ""
}

variable "instance_ami" {
  type        = string
  description = ""
}

variable "instance_type" {
  type        = string
  description = ""
}

variable "instance_tags" {
  type        = map(string)
  description = ""
  default = {
    Name    = "Ubuntu"
    Project = "Projeto Cloud 2022"
  }
}

variable "vpc_cidr_block" {
  type        = string
  description = ""
}

variable "vpc_tags" {
  type        = map(string)
  description = ""
}

variable "subnet_tags" {
  type        = map(string)
  description = ""
}

variable "subnet_cidr_block" {
  type        = string
  description = ""
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public Subnet CIDR values"
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "Private Subnet CIDR values"
}