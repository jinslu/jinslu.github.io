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

# ── 生成博达模板 JSP 文件 ──────────────────────────────────────────
# 博达栏目模板路径为 /xxx.jsp，将各页面 HTML 复制为对应 JSP 文件
echo "→ 生成博达模板 JSP 文件..."
PAGES=(research publications members news contact join)
cp "$SITE_DIR/_site/index.html" "$SITE_DIR/_site/index.jsp"
echo "  + index.jsp"
for page in "${PAGES[@]}"; do
  cp "$SITE_DIR/_site/$page/index.html" "$SITE_DIR/_site/$page.jsp"
  echo "  + $page.jsp"
done

# ── 打包 ──────────────────────────────────────────────────────────
echo "→ 打包 _site/ ..."
rm -f "$OUTPUT_ZIP"
cd "$SITE_DIR/_site"
zip -r "$OUTPUT_ZIP" . \
  --exclude "*.zip" --exclude "*.md" --exclude "*.py" \
  --exclude "feed.xml" --exclude "*.yml" --exclude "*.bib"

echo ""
echo "✓ 完成！上传包：boda-upload.zip（$(du -sh "$OUTPUT_ZIP" | cut -f1)）"
echo ""
echo "  博达操作步骤："
echo "  ① 将 boda-upload.zip 解压，把所有文件（含 *.jsp）上传覆盖到博达「文件|模板」根目录"
echo "  ② 各栏目对应模板文件：index.jsp / research.jsp / publications.jsp"
echo "                       members.jsp / news.jsp / contact.jsp / join.jsp"
echo "  ③ PDF等静态文件：在博达「文件|模板」中确认 user_data/pdf/ 目录已上传"
