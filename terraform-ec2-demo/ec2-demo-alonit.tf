terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.17.10"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  # this ami according to product spec
  ami           = "ami-0b0af3577fe5e3532"
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformEc2DemoAlonitV2"
  }
}
