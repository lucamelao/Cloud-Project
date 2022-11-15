# Projeto Cloud 2022

Desenvolvimento de uma aplicação capaz de provisionar uma infraestrutura por meio de uma interface amigável para gerenciar e administrá-la (construir, alterar e deletar recursos).

## Tutorial de Instalação e Operação

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

Para demais configurações consultar [Terraform](https://developer.hashicorp.com/terraform/downloads).

- AWS CLI

Configurando AWS para usar o Terraform. Isso deve ser feito a partir da [AWS Command Line Interface](https://aws.amazon.com/pt/cli/).

Nesse passo devem ser inseridas as IAM credentials (Access Key e Secret Access Key) para autenticar o Terraform AWS provider, por meio de variáveis de ambiente.

```shell
export AWS_ACCESS_KEY_ID= {ACCESS_KEY}

export AWS_SECRET_ACCESS_KEY= {SECRET_ACCESS_KEY}
```

**WARNING:** Nunca deixe suas credenciais públicas, faça uso de variáveis de ambiente locais e do AWS CLI.
