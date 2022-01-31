terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  # this ami according to product spec
  ami           = "ami-0a8b4cd432b1c3063"
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformEc2DemoAlonitV2"
  }
}
