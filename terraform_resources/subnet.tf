resource "aws_subnet" "my_subnet" {
  for_each = { for subnet in var.subnets : subnet.tags.Name => subnet }

  cidr_block = each.value.cidr_block
  tags       = each.value.tags

  vpc_id = aws_vpc.vpc.id
}