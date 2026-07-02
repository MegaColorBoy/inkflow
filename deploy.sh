#!/usr/bin/env bash

set -euo pipefail

echo "Begin deployment..."

echo "Preparing all pages..."
inkflow build --mode=all

echo "Generating RSS feed..."
inkflow export --mode=rss

echo "Syncing generated output to ghpages..."
mkdir -p ghpages
rsync -a --delete --exclude=".git" output/ ghpages/

echo "Committing and pushing changes if needed..."
git -C ghpages add -A

if git -C ghpages diff --cached --quiet; then
  echo "No changes to deploy."
else
  git -C ghpages commit -m "deploy: update generated site"
  git -C ghpages push origin master
fi

echo "Deployment complete."
