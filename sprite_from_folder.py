import urllib.request, time, sprite_creator, io, os

SUFFIX = ''
SPRITE_NAME = 'types'
IMAGE_DIR = 'Sprites/' + SPRITE_NAME + ' Images'
DATA_FILE_LOCATION = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX + '.txt'
IMAGE_WIDTH = 25
IMAGE_HEIGHT = 25
IMAGE_GAP = 1
IMAGES_ACROSS = 4

SPRITE_FILE_NAME = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX

sprite = sprite_creator.Sprite(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGES_ACROSS, IMAGE_GAP, SPRITE_FILE_NAME)
sprite.create_new()

lines = [
    """return {{
        ids = {{""".format(str(IMAGE_HEIGHT), str(sprite.sheet_width), str(IMAGE_GAP), str(IMAGE_WIDTH)).replace(
        'SPRITENAME', SPRITE_NAME)
]

for pos, fname in enumerate(os.listdir(IMAGE_DIR)):
    name = fname.replace('.png', '')
    sprite.add_next_image_from_file(IMAGE_DIR + '/' + fname)
    lines.append('\t\t["{}"] = {{ pos = {}, section = 1 }},'.format(name.replace('_', ' '), pos + 2))

lines.append('\t\t["{}"] = {{ pos = {}, section = 1 }},'.format('unknown', '1'))

lines.append('	},')
lines.append('}')

with open(DATA_FILE_LOCATION, 'w', encoding="utf-8") as f:
    f.write('\n'.join(lines))

sprite.save()
