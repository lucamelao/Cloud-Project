output "my_instance_name" {
  value = aws_instance.web_server.tags.Name
}

output "web_ami" {
  value = aws_instance.web_server.ami
}

output "igw_descpriton" {
  value = aws_internet_gateway.my_igw.tags.Name
}

output "name_of_iam_user" {
    value = aws_iam_user.my_iam_user[*]
  }