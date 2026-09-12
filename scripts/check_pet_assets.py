#!/usr/bin/env python3
"""Validate the v2 package and optionally regenerate exact APNG previews (Pillow)."""
import argparse
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets' / 'QQpet-codex'
ROWS = [
    ('idle', 'idle', [280, 110, 110, 140, 140, 320]),
    ('running-right', 'running-right', [120] * 7 + [220]),
    ('running-left', 'running-left', [120] * 7 + [220]),
    ('waving', 'waving', [140] * 3 + [280]),
    ('jumping', 'hover', [140] * 4 + [280]),
    ('failed', 'failed', [140] * 7 + [240]),
    ('waiting', 'waiting-sleep', [150] * 5 + [260]),
    ('running', 'running-active', [120] * 5 + [220]),
    ('review', 'review-instrument', [150] * 5 + [280]),
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(write_previews=False):
    pet = json.loads((ASSETS / 'pet.json').read_text())
    require(pet['id'] == 'QQpet-codex', 'Unexpected pet id')
    require(pet['spriteVersionNumber'] == 2, 'Expected sprite version 2')
    require(pet['spritesheetPath'] == 'spritesheet.webp', 'Unexpected atlas path')
    sheet = Image.open(ASSETS / pet['spritesheetPath'])
    require(sheet.format == 'WEBP' and sheet.mode == 'RGBA', 'Expected RGBA WebP')
    require(sheet.size == (1536, 2288), 'Expected 1536x2288 atlas')
    sheet.load()
    mapping = json.loads((ASSETS / 'source-mapping.json').read_text())
    require(len(mapping) == 11, 'Expected eleven row mappings')
    previews = []
    for row in range(11):
        state, name, durations = ROWS[row] if row < 9 else ('look-directions', '', [220] * 8)
        require(mapping[row]['state'] == state and mapping[row]['row'] == row,
                f'Incorrect mapping for row {row}')
        require(mapping[row]['frames'] == len(durations), f'Incorrect frame count at row {row}')
        require(mapping[row]['asset'] == pet['spritesheetPath'], f'Incorrect asset at row {row}')
        if row >= 9:
            require(mapping[row]['angles_degrees'] == [22.5 * i for i in range((row-9)*8, (row-8)*8)],
                    f'Incorrect gaze angle order at row {row}')
        frames = []
        for col in range(8):
            cell = sheet.crop((col*192, row*208, (col+1)*192, (row+1)*208))
            used = col < len(durations) or (row == 0 and col == 6)
            require(bool(cell.getchannel('A').getbbox()) == used, f'Unexpected occupancy at {row},{col}')
            if row == 0 and col == 6:
                require(cell.tobytes() == frames[0].tobytes(), 'Neutral must match first idle frame')
            if col < len(durations):
                frames.append(cell)
        if row < 9:
            previews.append((name, frames, durations))
        elif row == 9:
            look_frames = frames
        else:
            previews.append(('look-directions', look_frames + frames, [220] * 16))
    for name, frames, durations in previews:
        target = ROOT / 'assets' / 'previews' / f'{name}.png'
        if write_previews:
            frames[0].save(target, save_all=True, append_images=frames[1:], duration=durations,
                           loop=0, disposal=0, blend=0)
        with Image.open(target) as preview:
            require(preview.n_frames == len(frames), f'Preview frame count: {name}')
            require(preview.info.get('loop') == 0, f'Preview must loop: {name}')
            for index, expected in enumerate(frames):
                preview.seek(index)
                require(preview.convert('RGBA').tobytes() == expected.tobytes(),
                        f'Preview differs from atlas: {name} frame {index}')
                require(preview.info.get('duration') == durations[index],
                        f'Preview duration differs: {name} frame {index}')
    print('PASS: v2 metadata, 88 cells, neutral slot, row mappings, and 10 APNG previews')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-previews', action='store_true')
    check(parser.parse_args().write_previews)
