# 集成与超构光子芯片实验室网站

**Integrated and Meta Photonics Lab, Wuhan University**

---

## 项目结构

```
lab-site/
├── _config.yml          # GitHub 版主配置（metaphotonics.cn）
├── _config.boda.yml     # 博达版配置（lu.whu.edu.cn，仅覆盖 url）
├── _data/               # 数据文件（publications.json 等）
├── _layouts/            # 页面模板
├── _includes/           # 公共组件
├── assets/              # CSS / JS
├── user_data/           # 图片、PDF 等内容资源
├── scripts/             # 工具脚本
│   └── build-boda.sh    # 博达打包脚本
├── .github/workflows/   # GitHub Actions 自动部署
├── CNAME                # metaphotonics.cn
└── *.html               # 各栏目页面
```

---

## 两个部署版本

### 版本 A：GitHub Pages → metaphotonics.cn

推送到 main 分支后 GitHub Actions 自动构建发布（约 2 分钟生效）：

    git add .
    git commit -m "说明"
    git push origin main

**首次 GitHub 设置（只需做一次）：**
1. 在 GitHub 创建仓库（建议名：lab-website）
2. Settings → Pages → Source 选择 **GitHub Actions**
3. Settings → Pages → Custom domain 填写 `metaphotonics.cn`
4. DNS 添加：CNAME @ <username>.github.io
5. 添加远程并推送：
   git remote add origin git@github.com:<用户名>/<仓库名>.git
   git push -u origin main

---

### 版本 B：博达平台 → lu.whu.edu.cn

    bash scripts/build-boda.sh
    # 生成 boda-upload.zip，解压后上传到博达平台

---

## 日常更新流程

1. 修改源文件
2. 本地预览：bundle exec jekyll serve
3. 推送 GitHub（自动更新 metaphotonics.cn）：git add . && git commit -m "说明" && git push
4. 更新博达：bash scripts/build-boda.sh → 上传 boda-upload.zip
