import rawpy
import imageio
from filter import *

"""path = 'image.nef'
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
print(rgb)
imageio.imsave('output.png', rgb)"""

@make_filter
def load_raw(path: str) -> (list,):
    return ([1, 2, 3],)

print(filters)
