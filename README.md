# Lively-Magic · 灵动魔法

> 为 Minecraft 原版画风注入魔法灵魂的幻想光影

---

## 项目简介

**Lively-Magic** 是一套基于 LVE-Sunward 代码架构的 Minecraft Java 版光影。
在保留原版 Minecraft 视觉风格的基础上，融入魔法幻想元素——梦幻色彩、奇幻大气、发光特效。

设计理念：

> *"在不破坏原版画风的前提下，用魔法的色彩给每个世界注入幻想灵魂"*

---

## 核心特性

### 魔法 & 色彩
- **梦幻色调映射**：高饱和度 · 鲜艳色彩 · 魔法般的视觉氛围
- **增强色彩模拟**：发光矿石 · 自发光方块 · 时段光色曲线
- **泛光辉光**：魔法般的发光效果，让光源更具幻想感

### 大气 & 天空
- **极光 & 星云**：夜空中的魔法极光与星系星云
- **彩虹**：雨后或始终出现的魔法彩虹
- **幻想风格云层**：体积感云层，可选无界或幻想风格
- **幻想风格日月**：更梦幻的太阳和月亮外观

### 水面 & 材质
- **幻想风格水面**：清澈梦幻的水面效果
- **传送门特效**：地狱/末地传送门的魔法动画与自发光
- **发光矿石**：全矿石发光，营造魔法世界氛围

### 用户体验
- **全中文界面**
- **原版友好**：不魔改原版方块画风，仅增强视觉氛围
- **Mac 兼容**：Apple Silicon 专属色彩模拟方案

---

## 项目结构

```
Lively-Magic/
├── shader_pack/                  # 光影源码
│   ├── lib/
│   │   ├── common.glsl           # 核心配置（魔法风格默认参数）
│   │   └── materials/
│   │       └── materialHandling/
│   │           └── customMaterials.glsl
│   ├── program/
│   └── world0/                   # 主世界着色器
│   ├── world-1/                  # 地狱着色器
│   └── world1/                   # 末地着色器
├── 效果/                         # 实机截图
├── 参考/                         # 参考资料
└── README.md
```

---

## 快速开始

### 安装

1. 将 `shader_pack/` 打包为 `shaders/` 前缀的 zip 文件
2. 放入 `.minecraft/shaderpacks/`（或你的 Fabric 实例目录）
3. 在 Iris 设置中选择 "Lively-Magic"
4. 搭配任意资源包获得最佳效果

### 推荐设置

| 设置项 | 推荐值 | 说明 |
|--------|--------|------|
| 视觉风格 | 魔法 | 魔法幻想风格默认参数 |
| 模拟色彩光照 | 增强色彩 | 魔法色彩氛围 |
| 泛光 | 开启 | 魔法辉光效果 |
| 发光矿石 | 开启 | 全矿石发光 |
| 夜空星云 | 开启 | 魔法星空 |
| 极光 | 开启 | 魔法极光 |

---

## 开发信息

### 技术栈
- **基础架构**：LVE-Sunward / Complementary Reimagined r5
- **GLSL 版本**：`#version 130`（macOS ARM 兼容）

### 关键参数（common.glsl）

| 参数 | 值 | 说明 |
|------|-----|------|
| SHADER_STYLE | 6 | 魔法风格 |
| COLOR_LIGHT_MODE | 2 | 增强色彩模拟 |
| BLOOM_STRENGTH | 0.15 | 魔法辉光 |
| T_SATURATION | 1.20 | 高饱和度 |
| AURORA | 开启 | 魔法极光 |
| NIGHT_NEBULAE | 开启 | 夜空星云 |

### macOS 注意事项
- `COLORED_LIGHTING`（彩色光源）在 Mac 上不可用，已用 `COLOR_LIGHT_MODE` 替代
- 打包时必须保持 `shaders/` 目录结构前缀

---

## 参考

- **LVE-Sunward** by Lively Studio — 基础架构与代码参考
- **Complementary Reimagined r5** by EminGT — 方法与结构
- **零雾构想 (ZeroPBR)** by 零雾05_Fogg05 — PBR 材质标准

---

## 许可

GNU General Public License v3.0

---

**Lively-Magic · 灵动魔法** — Lively Studio (「零」影制作组) 出品 — 让每一束光都充满魔法
