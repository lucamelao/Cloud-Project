resource "aws_vpc" "vpc" {
  cidr_block = var.vpc.cidr_block
  tags       = var.vpc.tags
}