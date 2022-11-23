# Listando outputs


output "web_name" {
  value = aws_instance.web_server.tags.Name
}

output "web_ami" {
  value = aws_instance.web_server.ami
}

output "igw_descpriton" {
  value = aws_internet_gateway.my_igw.tags.Name
}