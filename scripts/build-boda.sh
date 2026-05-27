#!/bin/bash
# 构建博达平台版本（lu.whu.edu.cn）
# 用法：bash scripts/build-boda.sh
# 构建完成后直接从 _site/ 目录上传文件到博达，无需打包。

set -e
SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "→ 构建博达版本（url: https://lu.whu.edu.cn）..."
cd "$SITE_DIR"
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll build \
  --config _config.yml,_config.boda.yml

# ── 生成博达模板 JSP 文件 ──────────────────────────────────────────
echo "→ 生成博达模板 JSP 文件..."
PAGES=(research publications members news contact join)
cp "$SITE_DIR/_site/index.html" "$SITE_DIR/_site/index.jsp"
echo "  + index.jsp"
for page in "${PAGES[@]}"; do
  cp "$SITE_DIR/_site/$page/index.html" "$SITE_DIR/_site/$page.jsp"
  echo "  + $page.jsp"
done

echo ""
echo "✓ 完成！_site/ 目录已就绪，可直接上传到博达。"
echo ""
echo "  ┌─ 博达上传指南 ──────────────────────────────────────────────┐"
echo "  │ 【模板（每次更新页面内容时）】                               │"
echo "  │   新建/更新模板 → 选用本地HTML源文件：                       │"
echo "  │     首页       : _site/index.html      → 模板名 index       │"
echo "  │     研究方向   : _site/research/index.html  → research      │"
echo "  │     发表论文   : _site/publications/index.html → publications│"
echo "  │     课题组成员 : _site/members/index.html   → members       │"
echo "  │     新闻动态   : _site/news/index.html      → news          │"
echo "  │     联系我们   : _site/contact/index.html   → contact       │"
echo "  │     招生信息   : _site/join/index.html      → join          │"
echo "  │                                                              │"
echo "  │ 【静态资源（首次或资源有变动时）】                            │"
echo "  │   文件|模板 → 批量上传：                                     │"
echo "  │     CSS/JS : _site/assets/       → 上传到 assets/           │"
echo "  │     图片   : _site/user_data/images/ → 上传到 user_data/images/│"
echo "  │     PDF    : _site/user_data/pdf/    → 上传到 user_data/pdf/ │"
echo "  └──────────────────────────────────────────────────────────────┘"
