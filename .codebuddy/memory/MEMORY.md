# 项目记忆 - LVE-灵动视效 向阳而生·Sunward

## 项目概述
专属 Minecraft 光影系统，基于 Complementary Reimagined r5 架构，专注于 PBR 着色器光照。

## 项目结构
- `shader_pack/` - 光影着色器
  - `lib/common.glsl` - 核心配置定义（RP_MODE=2 labPBR, POM_DEPTH=0.90, NORMAL_MAP_STRENGTH=50）
  - `program/` - 着色器程序（gbuffers_basic, gbuffers_terrain 等）
  - `lang/` - 中文化设置
- `参考/` - 零雾老师 ZeroPBR 效果参考截图

## 关键设计决策
- **专注光影**：资源包已移除，项目专攻 GLSL 着色器 PBR 光照
- **基础架构**: Complementary Reimagined r5，`#version 130` + macro-based `#include`
- **PBR 模式**: RP_MODE=2 (labPBR/CUSTOM_PBR)，POM 仅在地形通道启用
- **打包规范**: zip 内所有文件必须在 `shaders/` 目录下
- **macOS ARM 兼容**: Iris 1.10.7 + Sodium，仅 `#version 130` 格式可用

## 重要教训
- `gbuffers_basic.glsl` 不要添加 POM 代码（变量不全会导致编译失败）
- 打包用 Python zipfile，确保 `shaders/` 前缀
- 恢复方法：原始 `LVE-灵动视效.zip` 在各个 shaderpacks 目录有备份

## 安装路径
- 主实例: `versions/1.21.11-Fabric-CODER/shaderpacks/`
- 备用: `shaderpacks/`
