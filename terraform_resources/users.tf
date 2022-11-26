# Create aws iam user
resource "aws_iam_user" "my_iam_user" {

  for_each = toset(var.iam_users)

  name = each.value

  force_destroy = true

}