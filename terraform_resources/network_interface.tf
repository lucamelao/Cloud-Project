resource "aws_network_interface" "network_interface" {
  for_each = { for network_interface in var.network_interface : network_interface.tags.Name => network_interface }

  subnet_id = aws_subnet.my_subnet[each.value.subnet_id].id

  private_ips = each.value.private_ip_address

  security_groups = [for security_group in each.value.security_groups : aws_security_group.my_security_group[security_group].id]

  tags = each.value.tags
}