# Terraform Infrastructure Deployment Action

The purpose of this action is to deploy infrastructure defined as config.yaml, and map it into Terraform and deploy it.

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `config-file` | Path to the config.yaml file | Yes | - |
| `secrets` | JSON object containing secret key-value pairs | No | `"{}"` |
| `tf-api-token` | Terraform Cloud API token | No | - |

## Example config.yaml

```yaml
---
terraform:
  config_version: "1"

  ssm_parameters:
    - name: "/my-app/api-key"
      description: "API key for a third-party service"
      type: "SecureString"
      value: "{{- var.api_key -}}"
      tags:
        project: "my-app"
    - name: "/my-app/database-url"
      description: "Database connection URL"
      type: "SecureString"
      value: "{{- var.database_url -}}"
      tags:
        project: "my-app"
        environment: "production"
```

## Usage

The deploy workflow from the "Product repository":

```yaml
name: Deploy Infrastructure

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write   # Required for AWS OIDC
      contents: read    # Required to checkout repo

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Deploy infrastructure
        uses: kaihendry/actions/terraform@main
        with:
          # Path to the config file
          config-file: 'config.yaml'

          # Secrets as JSON - keys should match parameter names in config.yaml
          secrets: |
            {
              "api_key": "${{ secrets.API_KEY }}",
              "database_url": "${{ secrets.DATABASE_URL }}"
            }

          # Terraform Cloud API token (optional, required for Terraform Cloud)
          tf-api-token: ${{ secrets.TF_API_TOKEN }}
```

## How it works

1. **Authentication**: Uses AWS OIDC to authenticate with AWS
2. **Config Processing**: Reads the config.yaml file and parses secrets JSON
3. **Terraform Generation**: Creates main.tf with AWS SSM parameters based on config
4. **Variable Mapping**: Maps secrets to Terraform variables in terraform.tfvars
5. **Deployment**: Runs `terraform init` and `terraform plan`

## Requirements

- AWS OIDC role configured for GitHub Actions
- Repository secrets for any values referenced in config.yaml
- Optional: Terraform Cloud API token for remote state management
