# LVE-Sunward · 向阳而生

> 为 PBR 而生的真实质感 Minecraft 光影

---

## 项目简介

**LVE-Sunward** 是一套基于 Complementary Reimagined r5 代码,和 Bedrock 灵动视效 风格的 Minecraft Java 版光影。  
借鉴 Sundial 的光线追踪理念与法线管线技术，专为 Minecraft JAVA 版优化。

设计理念：

> *"在不魔改原版画风的前提下，用真实的 PBR 物理渲染给每个方块注入灵魂"*

---

## ✨ 核心特性

### 法线 & 材质
- **Sundial 法线管线**：屏幕空间 TBN · 梯度衰减混合 · 掠射角修正 · 平滑双线性采样
- **POM 视差贴图**：深度 1.0 · 精度 256 · 各向异性过滤 8x
- **labPBR 完整支持**：法线贴图 · 反射贴图 · MER 材质 · 自发光

### 光照 & 色彩
- **Apple Silicon 专属色彩模拟**：发光矿石全开 · 自发光方块 · 光色时段曲线（三档可调）
- **实时阴影**：品质 4 · 距离 256m · 柔和过渡
- **体积光**：Lv3 光束 · 大气散射
- **TAA 时序抗锯齿**：配合 FXAA 混合抗锯齿

### 水面 & 大气
- **真实水面**：波纹 1.5 · PBR 镜面反射 · 动态折射
- **云层品质 3**：最高云渲染 · 体积感
- **自然色调映射**：对比度 1.1 · 饱和度 1.05
- **雨天水坑**：地面反射

### 用户体验
- **全中文界面** · 法线凸起独立设置页 · 模拟色彩光照快捷开关
- **500KB 体积** · 零依赖 · 开箱即用

---

## 📁 项目结构

```
Lively-Visual-Effects/
├── shader_pack/                  # 光影源码
│   ├── lib/
│   │   ├── common.glsl           # 核心配置（所有可调参数）
│   │   └── materials/
│   │       └── materialHandling/
│   │           └── customMaterials.glsl  # Sundial 法线管线
│   ├── program/
│   │   ├── gbuffers_terrain.glsl # 地形渲染（POM 通道）
│   │   └── gbuffers_basic.glsl   # 基础方块渲染
│   ├── lang/
│   │   └── en_US.lang            # 全中文设置界面
│   └── shaders.properties        # 设置页面布局
├── output/                       # 宣传视频输出
├── 效果/                         # 实机截图
├── 参考/                         # 零雾 ZeroPBR 参考
├── LVE-Sunward-Shader.zip        # 打包好的光影（开箱即用）
└── README.md
```

---

## 🚀 快速开始

### 安装

1. 下载 `LVE-Sunward-Shader.zip`
2. 放入 `.minecraft/shaderpacks/`（或你的 Fabric 实例目录）
3. 在 Iris 设置中选择 "LVE-Sunward-Shader"
4. 搭配 labPBR 材质包（如零雾 ZeroPBR）获得最佳效果

### 推荐设置

| 设置项 | 推荐值 | 说明 |
|--------|--------|------|
| 模拟色彩光照 | 真实色彩 | Mac 专属彩色光源替代方案 |
| 法线贴图强度 | 80 | Sundial 风格凹凸 |
| 视差深度 | 1.00 | POM 最大强度 |
| 视差精度 | 256 | 高精度视差 |
| 材质支持 | labPBR | 需要 PBR 材质包 |

---

## 🎯 开发信息

### 技术栈
- **基础架构**：Complementary Reimagined r5
- **GLSL 版本**：`#version 130`（macOS ARM 兼容）
- **包装格式**：`shaders/` 前缀 zip，Python zipfile 打包

### 关键参数（common.glsl）

| 参数 | 值 | 说明 |
|------|-----|------|
| RP_MODE | 2 | labPBR/seuspbr 模式 |
| SHADOW_QUALITY | 4 | 高质量阴影 |
| TAA_MODE | 1 | 时序抗锯齿 |
| POM_DEPTH | 1.00 | 视差深度 |
| NORMAL_MAP_STRENGTH | 80 | 法线强度 |
| ANISOTROPIC_FILTER | 8 | 各向异性过滤 |
| CLOUD_QUALITY | 3 | 最高云品质 |
| DETAIL_QUALITY | 3 | 最高细节 |
| COLOR_LIGHT_MODE | 1 | Mac 色彩模拟 |

### macOS 注意事项
- `COLORED_LIGHTING`（彩色光源）在 Mac 上不可用，已用 `COLOR_LIGHT_MODE` 替代
- 不要在 `gbuffers_basic.glsl` 中启用 POM（变量不全会导致 Iris 编译失败）
- 打包时必须保持 `shaders/` 目录结构前缀

---

## 📝 参考

- **Complementary Reimagined r5** by EminGT — 基础架构
- **Sundial** by GeForceLegend — 光线追踪理念 & 法线管线参考
- **零雾构想 (ZeroPBR)** by 零雾05_Fogg05 — PBR 材质设计标准
- **LabPBR 1.3** — Java 版 PBR 材质规范

---

## 📄 许可

GNU General Public License v3.0 · [github.com/Open-code-Studio](https://github.com/Open-code-Studio/Lively-Visual-Effects)

---

**LVE-Sunward · 向阳而生** — Lively Studio (「零」影制作组) 出品 — 让每一束光都有真实的温度 ✨
