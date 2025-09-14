The purpose of this action is to deploy infrastructure defined as config.yaml, and map it into Terraform and deploy it.

Example config.yaml:

```config.yaml
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

```

The deploy workflow from the "Product repository":
```deploy.yaml

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Deploy infrastructure
        uses: kaihendry/actions/terraform@main # The custom action
        with:
          # Input for the custom action: path to the config file
          config-file: 'config.yaml'

          # Input for the custom action: the secrets
          secrets: '{"api_key": "${{ secrets.API_KEY }}"}'
```


