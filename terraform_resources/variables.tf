variable "region" {
  type        = string
  description = ""
  default     = "us-east-1"
}

variable "iam_users" {
  type        = list(string)
  description = "IAM users"
  default     = ["User_Luca_Terraform", "luca2", "luca3", "luca4"]
}

variable "instances" {
  type = list(object({
    ami               = string
    type              = string
    network_interface = string
    device_index      = number
    tags              = map(string)
  }))
  default = [
    {
      ami               = "ami-08c40ec9ead489470"
      type              = "t2.micro"
      network_interface = "NIC 1"
      device_index      = 0
      tags = {
        Name = "Tag da instancia do luca"
  } }]
}

variable "network_interface" {
  type = list(object({
    subnet_id          = string
    private_ip_address = list(string)
    security_groups    = list(string)
    tags               = map(string)
  }))
  default = [
    {
      subnet_id          = "LUCA"
      private_ip_address = ["10.0.1.4"]
      security_groups    = ["sg-Luca"]
      tags = {
        Name = "Tag da interface de rede"
      }
  }]
}

variable "vpc" {
  type = object({
    cidr_block = string
    tags       = map(string)
  })
  default = {
    cidr_block = "10.0.0.0/16"
    tags = {
      "Name" = "VPC do Luca"
  } }
}

variable "subnets" {
  type = list(object({
    cidr_block  = string
    tags        = map(string)
  }))
  default = [{
    cidr_block  = "10.0.1.0/24"
    tags = {
      "Name" = "Subnet do Luca"
  } }]
}

variable "security_groups" {
  type = list(object({
    name        = string
    description = string

    ingress = object({
      from_port   = number
      to_port     = number
      protocol    = string
      cidr_blocks = list(string)
    })

    egress = object({
      from_port   = number
      to_port     = number
      protocol    = string
      cidr_blocks = list(string)
    })

    tags = map(string)

  }))

  default = [{
    name        = "Security Group do Luca"
    description = "Testing SEC"
    ingress = {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress = {
        from_port = 0
        to_port   = 0
        protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"] 
    }

    tags = {
      "Name" = "Security Group Tag test"
    }
  }]
}