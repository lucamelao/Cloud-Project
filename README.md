# Projeto Cloud 2022

Desenvolvimento de uma aplicação capaz de provisionar uma infraestrutura por meio de uma interface amigável para gerenciar e administrá-la (construir, alterar e deletar recursos).

## Tutorial de Instalação

- Bibliotecas e dependências

```shell
pip3 install -r requirements.txt
```

- Instalação do Terraform

Utilizando o Home Brew no MacOS:

```shell
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

Para demais configurações, consulte [Terraform](https://developer.hashicorp.com/terraform/downloads).

- AWS CLI

Configurando AWS para usar o Terraform. Isso deve ser feito a partir da [AWS Command Line Interface](https://aws.amazon.com/pt/cli/).

Nesse passo devem ser inseridas as IAM credentials (Access Key e Secret Access Key) para autenticar o Terraform AWS provider e permitir o acesso programático pelo usuário.

Uma vez instalado o CLI, é necessário configurar o acesso à AWS.

```shell
aws configure 
```

O terminal mostrará o seguinte output, solicitando o preenchimento com as credenciais.

```shell
AWS Access Key ID [None]: {ACCESS_KEY}
AWS Secret Access Key [None]: {SECRET_ACCESS_KEY}
Default region name [None]: {REGION}
Default output format [None]: {OUTPUT FORMAT}
```

Preencha os valores **{ACCESS_KEY}** e **{SECRET_ACCESS_KEY}** com as suas credenciais.

Para a finalidade da aplicação, pode preencher os demais campos com os valores abaixo:

**{REGION}** = us-east-1

**{OUTPUT FORMAT}** = json

Testando:

```shell
cat ~/.aws/credentials
```

É esperado que o terminal mostre as credenciais registradas em sua máquina.

Em caso de dúvidas, esse vídeo sobre [Como configurar AWS para usar o Terraform](https://youtu.be/2Q39eWPLVpg) pode ajudar.

**WARNING:** Nunca deixe suas credenciais públicas, faça uso de variáveis de ambiente locais ou do AWS CLI.

## Tutorial de uso

Após clonar o repositório em sua máquina, é importante que chegue ao diretório "terraform_resources".

```shell
cd terraform_resources
```

Para rodar a Interface de Usuário, digite no terminal:

```shell
python3 main.py
```
