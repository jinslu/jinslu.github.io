# 集成与超构光子芯片实验室网站 / Integrated and Meta Photonics Lab Website

## 文件结构 / File Structure

```
jinslu.github.io/
├── _config.yml              # Jekyll 配置
├── _layouts/
│   └── default.html         # 主布局（导航、页眉、页脚）
├── assets/
│   ├── css/
│   │   └── style.css        # 全站样式
│   ├── js/
│   │   └── main.js          # 语言切换 + 导航激活
│   └── img/                 # ⬅ 放置图片（PI照片等）
│       ├── pi.jpg           # PI头像（130×160px）
│       └── logo.png         # 实验室 logo（可选，64×64px）
├── index.html               # 首页
├── research.html            # 研究方向
├── members.html             # 课题组成员
├── publications.html        # 发表论文
├── news.html                # 新闻动态
├── contact.html             # 联系我们
└── join.html                # 招生信息
```

## 部署步骤 / Deployment

1. **清空现有仓库内容**（保留 `.git` 目录），将上述所有文件复制进去。

2. **替换占位内容：**
   - `assets/img/pi.jpg` — 替换为您的真实照片
   - `members.html` — 替换为真实成员信息
   - `publications.html` — 替换为真实论文列表
   - `news.html` — 替换为真实新闻
   - `index.html` 中的 `pi-bio` — 替换为您的真实简介

3. **推送到 GitHub：**
   ```bash
   git add .
   git commit -m "rebuild: professional academic lab site"
   git push origin main
   ```

4. **等待 1-2 分钟**，访问 `https://jinslu.github.io` 即可看到新网站。

## 功能说明 / Features

- ✅ 中英双语切换（点击右上角 EN/中文 按钮）
- ✅ 7个页面：首页、研究方向、成员、论文、新闻、联系、招生
- ✅ 论文/新闻分类筛选
- ✅ 响应式设计（支持手机/平板/电脑）
- ✅ 专业学术蓝配色，参照北大课题组风格
- ✅ 无需插件，纯 Jekyll 原生支持

## 自定义建议 / Customization

- 修改颜色：编辑 `assets/css/style.css` 中 `:root` 的 CSS 变量
- 添加实验室 Logo：将图片放至 `assets/img/logo.png`，并在 `_layouts/default.html` 取消注释 `<img>` 标签
- 添加成员照片：放至 `assets/img/members/` 并在 `members.html` 中引用
