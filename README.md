# QQpet-codex

QQpet-codex is a QQPet-inspired Codex desktop pet. The v2 edition adds 16 look directions and a laptop typing loop for active tasks, with rebuilt artwork and aligned body scale across states. It retains the microphone performance, hover greeting, blanket sleep, and instrument-checking motifs from the original QGG conversion.

QQpet-codex 是一款基于 QQ 宠物形象的 Codex 桌面宠物。v2 版新增 16 方向注视和任务执行时的笔记本敲键盘动作，重绘并统一各状态的身体比例，保留麦克风表演、悬浮招呼、盖被睡觉和检查仪器等原有动作特征。

Requires a client that supports `spriteVersionNumber: 2`. The client chooses task states and gaze directions; this package supplies their artwork. Desktop rendering sharpness still depends on client scaling.

需要支持 `spriteVersionNumber: 2` 的客户端。任务状态和注视方向由客户端选择，本包提供对应动画。桌面显示清晰度仍受客户端缩放影响。

## Preview / 动画预览

The previews below are animated PNGs generated from the bundled spritesheet. If they appear static in a Markdown client, open the image or view the repository on GitHub.

下面的预览图是从内置 spritesheet 生成的动态 PNG。如果某些 Markdown 客户端里看起来不动，可以打开图片或在 GitHub 页面查看。

| State / 状态 | Spritesheet row / 图集行 | Trigger / 触发语义 | Animated Preview / 动态预览 | Source / 来源 |
| --- | --- | --- | --- | --- |
| `idle` / 待机 | 0 | Default resting pose / 默认待机 | <img src="assets/previews/idle.png" width="112" alt="Idle animation preview"> | `1020010241.swf` |
| `running-right` / 向右走 | 1 | Move right / 向右移动 | <img src="assets/previews/running-right.png" width="112" alt="Running right animation preview"> | `1028020241.swf` |
| `running-left` / 向左走 | 2 | Move left / 向左移动 | <img src="assets/previews/running-left.png" width="112" alt="Running left animation preview"> | `1028020241.swf` mirrored |
| `waving` / 招手 | 3 | Greeting fallback; microphone pose / 打招呼备用状态，麦克风动作 | <img src="assets/previews/waving.png" width="112" alt="Waving microphone animation preview"> | `1023010221.swf` |
| `jumping` / hover | 4 | Hover greeting, feet planted / 悬浮时双翅招呼，双脚着地 | <img src="assets/previews/hover.png" width="112" alt="Hover animation preview"> | `1020090221.swf` |
| `failed` / 失败 | 5 | Failed or interrupted state / 失败或中断状态 | <img src="assets/previews/failed.png" width="112" alt="Failed animation preview"> | `1020000541.swf` |
| `waiting` / 等待 | 6 | Client waiting state, blanket sleep / 客户端等待状态，盖被睡觉 | <img src="assets/previews/waiting-sleep.png" width="112" alt="Waiting sleep animation preview"> | `1020041221.swf` |
| `running` / 运行中 | 7 | Active task: laptop typing / 执行任务时敲键盘 | <img src="assets/previews/running-active.png" width="112" alt="Running active animation preview"> | New generated laptop animation / 新绘制笔记本动作 |
| `review` / reviewing | 8 | Review mode; checking instrument / review 状态，检查/操作仪器 | <img src="assets/previews/review-instrument.png" width="112" alt="Review instrument animation preview"> | `1029200331.swf` |
| Look directions / 注视方向 | 9–10 | Clockwise from up / 从上方开始顺时针 | <img src="assets/previews/look-directions.png" width="112" alt="Sixteen clockwise look poses"> | New generated poses / 新绘制姿势 |

The Source column identifies the original visual reference. v2 artwork was generated from those references and deterministically registered; it is not a direct SWF frame export. Review uses six keyframes, combining two original neutral transition beats.

来源列记录原始视觉参考。v2 图像基于这些参考生成后统一配准，并非直接导出的 SWF 帧。仪器检查保留 6 个关键动作，合并了原来的两个中性过渡拍。

## Install / 安装

Clone this repository into your Codex skills folder:

将仓库克隆到 Codex 的 skills 目录：

```bash
git clone https://github.com/chenboos5/QQpet-codex.git ~/.codex/skills/QQpet-codex
```

Run the installer:

运行安装脚本：

```bash
bash ~/.codex/skills/QQpet-codex/scripts/install_QQpet_codex.sh
```

The pet will be installed to:

宠物会安装到：

```bash
~/.codex/pets/QQpet-codex
```

Then restart Codex or refresh the pet list, and select `QQpet-codex`.

然后重启 Codex 或刷新宠物列表，选择 `QQpet-codex`。

## Included / 包含内容

- `SKILL.md`: Codex skill instructions / Codex skill 说明
- `scripts/install_QQpet_codex.sh`: installer / 安装脚本
- `assets/QQpet-codex/pet.json`: pet metadata / 宠物配置
- `assets/QQpet-codex/spritesheet.webp`: pet animation sheet / 宠物动画图集
- `assets/QQpet-codex/source-mapping.json`: source animation mapping / 源动画映射
- `assets/previews/*.png`: animated README previews / README 动态预览

## Notes / 说明

- The installer copies bundled assets into your local Codex pets directory.
- No SWF conversion is required during installation.
- If `CODEX_HOME` is set, the installer uses `$CODEX_HOME/pets/QQpet-codex`; otherwise it uses `~/.codex/pets/QQpet-codex`.

- 安装脚本会把内置资源复制到本机 Codex pets 目录。
- 安装时不需要重新转换 SWF。
- 如果设置了 `CODEX_HOME`，会安装到 `$CODEX_HOME/pets/QQpet-codex`；否则安装到 `~/.codex/pets/QQpet-codex`。

## Update and restore / 更新与恢复

Before installing over an existing pet, copy its entire `QQpet-codex` folder to a backup location. To restore, replace the installed folder with that backup, then restart Codex or refresh the pet list. The installer replaces only its three bundled files; an old `spritesheet.png` may remain but is no longer referenced.

覆盖安装前，将现有的 `QQpet-codex` 整个目录复制到备份位置。恢复时用备份替换安装目录，再重启 Codex 或刷新宠物列表。安装脚本仅覆盖三个内置文件；旧版 `spritesheet.png` 可能保留，但不再被引用。

## Asset layout and checks / 图集布局与检查

The atlas is 1536×2288, with 8×11 cells of 192×208. Rows 0–8 contain 6, 8, 8, 4, 5, 8, 6, 6, 6 animation frames. Row 0 column 6 is a dedicated neutral copy of the first idle frame. Other unused cells are transparent. Rows 9–10 contain 16 gaze poses at 22.5° intervals: 0° up, 90° screen-right, 180° down, 270° screen-left.

图集为 1536×2288，包含 8×11 个 192×208 单元。第 0–8 行分别使用 6、8、8、4、5、8、6、6、6 帧；第 0 行第 6 列另存默认中性帧，其余未使用单元透明。第 9–10 行为间隔 22.5° 的 16 个方向：0° 向上、90° 屏幕右方、180° 向下、270° 屏幕左方。行列编号从 0 开始。

With Python 3 and Pillow installed, validate the metadata, atlas cells, and exact preview frames:

安装 Python 3 和 Pillow 后，检查元数据、图集单元和预览帧：

```bash
python3 scripts/check_pet_assets.py
```

To regenerate animated PNG previews from the atlas / 从图集重新生成动态 PNG 预览：

```bash
python3 scripts/check_pet_assets.py --write-previews
```
