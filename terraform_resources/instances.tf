resource "aws_instance" "my_instance" {
  for_each = { for instance in var.instances : instance.tags.Name => instance }

  ami = each.value.ami

  instance_type = each.value.type

  network_interface {
    network_interface_id = aws_network_interface.network_interface[each.value.network_interface].id
    device_index         = each.value.device_index
  }

  tags = each.value.tags
}