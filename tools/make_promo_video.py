#!/usr/bin/env python3
"""
LVE-Sunward 宣传视频
NOTHING UI+ 设计规范 · OpenCV 渲染

基于 Open-code-Studio/NOTHING-UI-1 设计规范:
- 暗色主题 + 青色强调
- 顶栏 + 内容区 + 底栏三段式布局
- 静态UI预渲染 + 动态内容叠加
- PingFang 中文字体
"""

import os, time, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

# ========== 设计规范 (NOTHING UI+) ==========
W, H, FPS = 1920, 1080, 24
TOP_H, BOT_H = 80, 56
CONTENT_Y, CONTENT_H = TOP_H, H - TOP_H - BOT_H
SIDE_W = 420
MAIN_X, MAIN_W = SIDE_W, W - SIDE_W

# 颜色 (BGR for OpenCV)
BG       = (18, 18, 20)
TOP_BG   = (22, 22, 24)
BOT_BG   = (22, 22, 24)
SIDE_BG  = (28, 28, 30)
PRI      = (235, 230, 225)          # 主文字
SEC      = (210, 208, 205)          # 次文字(高亮)
ACC      = (235, 235, 230)           # 强调色(纯白亮) 防压缩吞中文
SEP      = (50, 50, 52)

REF  = os.path.join(os.path.dirname(__file__), '..', '效果')
OUT  = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(OUT, exist_ok=True)

def font(sz=40, bold=False):
    for p in ['/System/Library/Fonts/STHeiti Medium.ttc',
              '/System/Library/Fonts/Hiragino Sans GB.ttc',
              '/Library/Fonts/Arial Unicode.ttf']:
        if os.path.exists(p):
            try:
                fnt = ImageFont.truetype(p, sz)
                m = fnt.getmask('中')
                if m and m.size[0] > 5:
                    return fnt
            except Exception as e:
                pass
    return ImageFont.load_default()

def pil2bgr(img): return np.array(img)[:, :, ::-1].copy()  # RGB→BGR via numpy

def bg_page(title, subtitle="", sz=70, sz_sub=28):
    """标题页/结尾页 - PIL 渲染"""
    img = Image.new('RGB', (W, H), BG[::-1])
    d = ImageDraw.Draw(img)
    f_title = font(sz)
    f_sub = font(sz_sub)
    lines = title.split('\n')
    # STHeiti needs small y offset, calc center approx
    total_h = len(lines) * (sz + 12) + (len(subtitle.split('\n')) * (sz_sub + 6) if subtitle else 0)
    y = 60  # STHeiti renders from ~font_size offset
    for line in lines:
        tw = d.textlength(line, font=f_title)
        x = max(0, (W - tw) // 2)
        d.text((x, y), line, font=f_title, fill=ACC[::-1])
        y += sz + 12
    if subtitle:
        y += 8
        for line in subtitle.split('\n'):
            tw = d.textlength(line, font=f_sub)
            x = max(0, (W - tw) // 2)
            d.text((x, y), line, font=f_sub, fill=SEC[::-1])
            y += sz_sub + 6
    return pil2bgr(img)

def feat_frame(img_path, text, idx, total, lang):
    """功能展示帧：图片 + 侧边栏 + 底栏(预渲染PNG防中文乱码)"""
    frame = np.full((H, W, 3), BG[::-1], dtype=np.uint8)

    # 主图片区
    raw = Image.open(img_path).convert('RGB').resize((MAIN_W, CONTENT_H), Image.LANCZOS)
    frame[CONTENT_Y:CONTENT_Y+CONTENT_H, MAIN_X:MAIN_X+MAIN_W] = pil2bgr(raw)

    # 顶栏
    cv2.rectangle(frame, (0, 0), (W, TOP_H), TOP_BG[::-1], -1)
    cv2.line(frame, (0, TOP_H - 1), (W, TOP_H - 1), SEP[::-1], 1)
    cv2.putText(frame, "LVE-Sunward  Sunward", (28, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.85, ACC[::-1], 2, cv2.LINE_AA)

    # 侧边栏 - 预渲染PNG
    hdr_png = f'/tmp/promo_txt/sidebar_hdr_{lang}.png'
    if os.path.exists(hdr_png):
        hdr = cv2.imread(hdr_png)
        frame[TOP_H:TOP_H+hdr.shape[0], :SIDE_W] = hdr
        # 分隔线
        cv2.line(frame, (8, TOP_H + 52), (SIDE_W - 8, TOP_H + 52), SEP[::-1], 1)

    # 特性文字 - 预渲染PNG
    for i, w in enumerate(text.split('·')):
        feat_png = f'/tmp/promo_txt/feat_{lang}_{i}.png'
        if os.path.exists(feat_png):
            fimg = cv2.imread(feat_png)
            y = TOP_H + 70 + i * 36
            if y + fimg.shape[0] < H - BOT_H:
                frame[y:y+fimg.shape[0], :fimg.shape[1]] = fimg

    # 底栏 - 预渲染PNG
    bot_png = f'/tmp/promo_txt/bot_{lang}.png'
    if os.path.exists(bot_png):
        bot = cv2.imread(bot_png)
        frame[H - BOT_H + 8:H - BOT_H + 8 + bot.shape[0], 20:20 + bot.shape[1]] = bot
    cv2.line(frame, (0, H - BOT_H), (W, H - BOT_H), SEP[::-1], 1)
    cv2.putText(frame, f"{idx + 1} / {total}",
                (W - 180, H - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, SEC[::-1], 1, cv2.LINE_AA)
    cv2.putText(frame, "github.com/Open-code-Studio",
                (W - 340, H - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ACC[::-1], 1, cv2.LINE_AA)

    return frame

# ========== 生成 ==========
for lang, meta in [
    ("CN", {
        "title": "LVE-灵动视效\n向阳而生 · Sunward",
        "sub": "基于 Complementary Reimagined r5\nSundial 法线 · Mac 色彩模拟 · labPBR · 实机截图",
        "feats": [
            "Sundial 法线管线 · 真实凹凸立体感",
            "Mac 模拟色彩光照 · PBR 物理渲染",
            "屏幕空间 TBN · 平滑双线性法线采样",
            "POM 视差深度 1.0 · 精度 256 · AF 8x",
            "真实 PBR 镜面反射 · 动态水面波纹",
            "体积光 · 大气散射 · 自然色调映射",
            "全中文界面 · 法线凸起独立设置页",
            "Iris 1.10.7+ macOS ARM 实测截图",
            "光影包 500KB · 零依赖 · 开箱即用",
            "向阳而生 · LVE-Sunward 真实效果",
        ],
        "end": "LVE-Sunward\ngithub.com/Open-code-Studio",
    }),
    ("EN", {
        "title": "LVE-Sunward\nLively Visual Effects",
        "sub": "Based on Complementary Reimagined r5\nSundial Normals · Mac Color Sim · Real Captures",
        "feats": [
            "Sundial Normal Pipeline · Real 3D Depth",
            "Mac Color Simulation · PBR Rendering",
            "Screen-Space TBN · Bilinear Normal Sampling",
            "POM Depth 1.0 · Quality 256 · AF 8x",
            "PBR Specular Reflection · Dynamic Water",
            "Volumetric Light · Atmospheric Scattering",
            "Full Chinese UI · Normal Settings Page",
            "Iris 1.10.7+ macOS ARM · Real Screenshots",
            "500KB Pack · Zero Deps · Ready to Use",
            "Sunward · LVE-Sunward Real Results",
        ],
        "end": "LVE-Sunward\ngithub.com/Open-code-Studio",
    }),
]:
    images = sorted([os.path.join(REF, f) for f in os.listdir(REF) if f.endswith('.png')])
    feats = meta["feats"]
    total = len(images) + 3  # title + images + end

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out_path = os.path.join(OUT, f"LVE-Sunward-{lang}.mp4")
    writer = cv2.VideoWriter(out_path, fourcc, FPS, (W, H))
    assert writer.isOpened(), "编码器不可用"

    print(f"🎬 {lang}: {total} 段 → {out_path}")
    t0 = time.time()

    # Title - 预渲染PNG(避开Pillow中文bug)
    title_png = f'/tmp/promo_{lang}_title.png'
    if os.path.exists(title_png):
        title_frame = cv2.imread(title_png)
    else:
        title_frame = bg_page(meta["title"], meta["sub"])
    for _ in range(int(2.5 * FPS)): writer.write(title_frame)

    # Features
    for i, img in enumerate(images):
        frame = feat_frame(img, feats[i % len(feats)], i, len(images), lang)
        for _ in range(int(4.0 * FPS)): writer.write(frame)

    # End
    end_frame = bg_page(meta["end"], sz=60)
    for _ in range(int(2.0 * FPS)): writer.write(end_frame)

    writer.release()
    sz_mb = os.path.getsize(out_path) / 1024 / 1024
    print(f"   ✅ {sz_mb:.1f} MB ({time.time() - t0:.1f}s)")

print("\n完成！output/ 目录")
