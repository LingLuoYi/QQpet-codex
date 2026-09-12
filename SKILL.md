---
name: QQpet-codex
description: Install the bundled QQpet-codex desktop pet, a QQPet-inspired v2 pet with 16 look directions, laptop typing during active tasks, microphone performance, hover greeting, and instrument review. Use when the user wants to install, restore, or share this custom Codex pet. 中文：安装、恢复或分享 QQpet-codex 这款 Codex 桌面宠物。
---

# QQpet-codex

## English

This skill installs a bundled Codex desktop pet into:

```bash
${CODEX_HOME:-$HOME/.codex}/pets/QQpet-codex
```

## Install

If this skill is already installed under Codex skills, run:

```bash
bash "${CODEX_HOME:-$HOME/.codex}/skills/QQpet-codex/scripts/install_QQpet_codex.sh"
```

If you are inside the unpacked skill folder, run:

```bash
bash scripts/install_QQpet_codex.sh
```

After installation, restart Codex or refresh the pet list, then select `QQpet-codex`.

## What It Installs

- Pet id: `QQpet-codex`
- Display name: `QQpet-codex`
- Format: v2 (`spriteVersionNumber: 2`), 1536×2288 lossless WebP
- Look directions: 16 clockwise poses, starting at up
- Active task (`running`, row 7): six-frame laptop typing loop
- Hover animation: planted greeting inspired by `1020090221.swf`, mapped to the `jumping` row
- Waving animation: microphone pose inspired by `1023010221.swf`
- Review animation: instrument-checking pose inspired by `1029200331.swf`
- Assets: `pet.json`, `spritesheet.webp`, and `source-mapping.json`

The installer verifies the bundled files before copying them. Back up an existing pet directory before updating; see README for restore instructions. A v2-compatible Codex client controls state transitions.

## 中文

这个 skill 会把内置的 QQpet-codex 桌面宠物安装到：

```bash
${CODEX_HOME:-$HOME/.codex}/pets/QQpet-codex
```

### 安装

如果这个 skill 已经放在 Codex 的 skills 目录里，运行：

```bash
bash "${CODEX_HOME:-$HOME/.codex}/skills/QQpet-codex/scripts/install_QQpet_codex.sh"
```

如果你正在解压后的 skill 文件夹里，运行：

```bash
bash scripts/install_QQpet_codex.sh
```

安装完成后，重启 Codex 或刷新宠物列表，然后选择 `QQpet-codex`。

### 安装内容

- 宠物 id：`QQpet-codex`
- 展示名称：`QQpet-codex`
- 格式：v2（`spriteVersionNumber: 2`），1536×2288 无损 WebP
- 注视方向：从正上方开始，顺时针 16 个方向
- 任务执行（`running`，第 7 行）：6 帧笔记本敲键盘动作
- hover 动画：参考 `1020090221.swf` 的站立招呼，映射到 `jumping` 行
- waving 动画：参考 `1023010221.swf` 的麦克风姿势
- review 动画：参考 `1029200331.swf` 的检查/操作仪器姿势
- 资源文件：`pet.json`、`spritesheet.webp`、`source-mapping.json`

安装脚本会先检查内置资源是否齐全，再复制到 Codex 的 pets 目录。更新前请备份现有宠物目录，恢复方法见 README。状态切换由支持 v2 的 Codex 客户端控制。
