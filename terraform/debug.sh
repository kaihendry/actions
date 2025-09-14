REPO=kaihendry/terraform-config
gh workflow run deploy.yaml -R $REPO
sleep 5
gh run view $(gh run list -w deploy.yaml -R $REPO --json databaseId -q '.[0].databaseId') -R $REPO --log-failed
