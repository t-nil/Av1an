from .aom import Aom
from .rav1e import Rav1e
from .svtav1 import SvtAv1
from .vpx import Vpx
from .x264 import X264
from .x265 import X265

ENCODERS = {
    "aom": Aom(),
    "rav1e": Rav1e(),
    "svt_av1": SvtAv1(),
    "vpx": Vpx(),
    "x264": X264(),
    "x265": X265(),
}
