resource "aws_security_group" "my_security_group" {

  for_each = { for security_group in var.security_groups : security_group.tags.Name => security_group }
  name     = each.value.name
  vpc_id   = aws_vpc.vpc.id

  ingress {
    from_port   = each.value.ingress.from_port
    to_port     = each.value.ingress.to_port
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.vpc.cidr_block]
  }

  egress {
    from_port   = each.value.egress.from_port
    to_port     = each.value.egress.to_port
    protocol    = "-1"
    cidr_blocks = each.value.egress.cidr_blocks
  }

  tags = each.value.tags
}