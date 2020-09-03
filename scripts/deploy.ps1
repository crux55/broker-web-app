$branch= &git rev-parse --abbrev-ref HEAD

if ($branch -ne 'v0.1-dev'){
    Write-Output 'You can not deploy from a feature'
    exit
}

gcloud app deploy --promote --stop-previous-version