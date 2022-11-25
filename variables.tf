variable "aws_region" {
  type        = string
  description = ""
  default     = "us-east-1"
}

variable "instance_ami" {
  type        = string
  description = ""
  default     = "ami-08c40ec9ead489470"

}

variable "instance_type" {
  type        = string
  description = ""
}

variable "instance_tags" {
  type        = map(string)
  description = ""
  default = {
    "Name" = "Tag da instancia do luca"
  }
}

variable "vpc_cidr_block" {
  type        = string
  description = ""
  default     = "10.0.0.0/16"
}

variable "vpc_tags" {
  type        = map(string)
  description = ""
  default = {
    "Name" = "VPC do Luca"
  }
}

variable "subnet_tags" {
  type        = map(string)
  description = ""
  default = {
    "Name" = "VPC de teste do Luca"
  }
}

variable "subnet_cidr_block" {
  type        = string
  description = "Public Subnet CIDR values"
  default     = "10.0.1.0/24"
}

variable "ingress_from_port" {
  type        = number
  description = "Ingress from port"
  default     = 43
}

variable "ingress_to_port" {
  type        = number
  description = "Ingress to port"
  default     = 43
}

variable "ingress_protocol" {
  type        = string
  description = "Protocol"
  default     = "tcp"
}

variable "egress_to_port" {
  type        = number
  description = "Egress to port"
  default     = 0
}

variable "egress_from_port" {
  type        = number
  description = "Egress from port"
  default     = 0
}

variable "egress_protocol" {
  type        = string
  description = "Protocol"
  default     = "-1"
}

variable "egress_cidr_blocks" {
  type        = list(string)
  description = "CIDR blocks"
  default     = ["0.0.0.0/0"]
}

variable "igw_tags" {
  type        = map(string)
  description = "Internet Gateway Tags"
  default = {
    "Name" : "Project VPC Internet Gateway",
    "Project" : "Projeto Cloud 2022"
  }
}

variable "route_table_cidr_block" {
  type        = string
  description = "Route Table CIDR block"
  default     = "0.0.0.0/0"
}

variable "second_route_table_tags" {
  type        = map(string)
  description = "2nd Route Table Tags"
  default = {
    "Name" : "2nd Route Table",
    "Project" : "Projeto Cloud 2022"
  }
}

variable "security_group_name" {
  type        = string
  description = "Security Group Name"
}

variable "security_group_tags" {
  type        = map(string)
  description = "Tags for the security group"
  default = {
    "Name" : "Test Security Group"
  }
}

variable "iam_users" {
  type        = list(string)
  description = "IAM users"
  default     = ["luca1", "luca2", "luca3", "luca4"]
}