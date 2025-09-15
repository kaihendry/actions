# Terraform Infrastructure Deployment Action

The purpose of this action is to deploy infrastructure defined as config.yaml,
and map it into Terraform and deploy it.

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `config-file` | Path to the config.yaml file | Yes | - |
| `tf-api-token` | Terraform Cloud API token | No | - |

## Example config.yaml

From https://github.com/kaihendry/terraform-config

    APIKEY=foo pkl eval -f yaml config.pkl
    terraform_version: '1'
    terraform:
      ssm_parameters:
      - name: /my-app/api-key
        description: API key for a third-party service
        type: String
        value: foo
        tags:
          project: my-app
