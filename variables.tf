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
  description = "Public Subnet CIDR values"
}

variable "ingress_from_port" {
  type        = number
  description = "Ingress from port"
}

variable "ingress_to_port" {
  type        = number
  description = "Ingress to port"
}

variable "ingress_protocol" {
  type        = string
  description = "Protocol"
}

variable "egress_to_port" {
  type        = number
  description = "Egress to port"
}

variable "egress_from_port" {
  type        = number
  description = "Egress from port"
}

variable "egress_protocol" {
  type        = string
  description = "Protocol"
}

variable "egress_cidr_blocks" {
  type        = list(string)
  description = "CIDR blocks"
}

variable "igw_tags" {
  type        = map(string)
  description = "Internet Gateway Tags"
}

variable "route_table_cidr_block" {
  type        = string
  description = "Route Table CIDR block"
}

variable "second_route_table_tags" {
  type        = map(string)
  description = "2nd Route Table Tags"
}

variable "security_group_tags" {
  type        = map(string)
  description = "Tags for the security group"
}

variable "user_name" {
  type        = string
  description = "User name"
}