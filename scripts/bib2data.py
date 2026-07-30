#!/usr/bin/env python3
"""
bib2data.py — 将 user_data/bib/jinsheng.bib 转换为 _data/publications.json

使用方法 / Usage:
    python3 scripts/bib2data.py

每次更新 jinsheng.bib 后运行一次，然后 git push。
幻灯片配置请直接编辑 _data/slides.yml。
"""
import re, json, os, sys

# ── 路径配置 ─────────────────────────────────────────────────────
REPO        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_PATH    = os.path.join(REPO, 'user_data', 'bib', 'jinsheng.bib')
DATA_DIR    = os.path.join(REPO, '_data')
PUB_OUT     = os.path.join(DATA_DIR, 'publications.json')
PDF_URL     = '/user_data/pdf'   # web path for PDF links


# ── bib 解析器 ────────────────────────────────────────────────────
def parse_bib(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    entries = []
    i = 0
    while i < len(text):
        at = text.find('@', i)
        if at == -1: break
        m = re.match(r'@(\w+)\s*\{', text[at:], re.IGNORECASE)
        if not m: i = at + 1; continue
        etype = m.group(1).lower()
        if etype == 'comment': i = at + m.end(); continue
        start = at + m.end()
        depth, j = 1, start
        while j < len(text) and depth:
            if text[j] == '{': depth += 1
            elif text[j] == '}': depth -= 1
            j += 1
        body = text[start:j-1]
        km = re.match(r'\s*([^\s,]+)\s*,', body)
        if km:
            key = km.group(1)
            fields = parse_fields(body[km.end():])
            fields['_key'] = key
            fields['_type'] = etype
            entries.append(fields)
        i = j
    return entries

def parse_fields(text):
    fields = {}
    i = 0
    while i < len(text):
        fm = re.match(r'\s*(\w+)\s*=\s*', text[i:])
        if not fm: i += 1; continue
        name = fm.group(1).lower()
        i += fm.end()
        if i >= len(text): break
        c = text[i]
        if c == '{':
            depth, j = 1, i+1
            while j < len(text) and depth:
                if text[j] == '{': depth += 1
                elif text[j] == '}': depth -= 1
                j += 1
            value = text[i+1:j-1]
        elif c == '"':
            j = i+1
            while j < len(text) and text[j] != '"': j += 1
            value = text[i+1:j]; j += 1
        else:
            vm = re.match(r'[\w\d]+', text[i:])
            if vm: value = vm.group(0); j = i + vm.end()
            else: i += 1; continue
        value = re.sub(r'\{([^{}]*)\}', r'\1', value)
        value = re.sub(r'\s+', ' ', value).strip()
        fields[name] = value
        i = j
        while i < len(text) and text[i] in ' \t\n\r,': i += 1
    return fields

def build_output(entries):
    articles, confs = [], []
    for e in entries:
        t = e.get('_type', '')
        file_val = e.get('file', '')
        obj = {
            'key':    e.get('_key', ''),
            'year':   int(e.get('year', 0) or 0),
            'title':  e.get('title', ''),
            'author': re.sub(r'\s+', ' ', e.get('author', '')).strip(),
            'doi':    e.get('doi', ''),
            'url':    e.get('url', ''),
            'file':   f"{PDF_URL}/{file_val}" if file_val else '',
            'news':   e.get('news', ''),
            'editors_suggestion': 'editorsuggestion' in e,
            'cover':  e.get('cover', ''),
        }
        if t == 'article':
            obj.update({
                'journal': e.get('journal', ''),
                'volume':  e.get('volume', ''),
                'number':  e.get('number', ''),
                'pages':   e.get('pages', ''),
            })
            articles.append(obj)
        elif t == 'inproceedings':
            obj.update({
                'booktitle': e.get('booktitle', ''),
                'pages':     e.get('pages', ''),
                'publisher': e.get('publisher', ''),
            })
            confs.append(obj)

    articles.sort(key=lambda x: x['year'], reverse=True)
    confs.sort(key=lambda x: x['year'], reverse=True)

    total = len(articles)
    for i, a in enumerate(articles):
        a['num'] = total - i

    ctotal = len(confs)
    for i, c in enumerate(confs):
        c['num'] = ctotal - i

    return {'articles': articles, 'conferences': confs,
            'total_articles': total, 'total_conferences': ctotal}


# ── 主程序 ────────────────────────────────────────────────────────
if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)
    errors = []

    # 1. 转换 bib → publications.json
    if not os.path.exists(BIB_PATH):
        errors.append(f'未找到 bib 文件：{BIB_PATH}')
    else:
        entries = parse_bib(BIB_PATH)
        output  = build_output(entries)
        with open(PUB_OUT, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f'✓ 论文数据已生成：_data/publications.json')
        print(f'  期刊论文 {output["total_articles"]} 篇 | '
              f'会议论文 {output["total_conferences"]} 篇')

    if errors:
        print('\n警告：')
        for e in errors: print(f'  ⚠ {e}')
        sys.exit(1)
    else:
        print('\n全部完成，现在可以运行 bundle exec jekyll serve 预览。')
