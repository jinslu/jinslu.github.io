#!/bin/bash
# 构建博达平台版本（lu.whu.edu.cn）并打包
# 用法：bash scripts/build-boda.sh

set -e
SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_ZIP="$SITE_DIR/boda-upload.zip"

echo "→ 构建博达版本（url: https://lu.whu.edu.cn）..."
cd "$SITE_DIR"
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll build \
  --config _config.yml,_config.boda.yml

echo "→ 打包 _site/ ..."
rm -f "$OUTPUT_ZIP"
cd "$SITE_DIR/_site"
zip -r "$OUTPUT_ZIP" . \
  --exclude "*.zip" --exclude "*.md" --exclude "*.py" \
  --exclude "feed.xml" --exclude "*.yml" --exclude "*.bib"

echo ""
echo "✓ 完成！上传包：boda-upload.zip（$(du -sh "$OUTPUT_ZIP" | cut -f1)）"
echo "  将 boda-upload.zip 解压后上传到博达平台，确保 index.html 在根目录。"
