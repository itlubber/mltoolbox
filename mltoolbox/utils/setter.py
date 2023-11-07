# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/2 13:46
@Author  : itlubber
@Site    : itlubber.art
"""

import warnings

warnings.filterwarnings("ignore")

import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

from .utils.logger import init_logger


def seed_torch(seed):
    import torch

    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.manual_seed(seed)
        # Benchmark 模式会提升计算速度，但是由于计算中有随机性，每次网络前馈结果略有差异。
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.deterministic = True


def seed_tensorflow(seed):
    import tensorflow as tf

    tf.compat.v1.reset_default_graph()
    tf.random.set_seed(seed)


def seed_everything(seed: int, freeze_torch=False, freeze_tf=False):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

    if freeze_torch:
        seed_torch(seed)

    if freeze_tf:
        seed_tensorflow(seed)


def init_setting(font_path=None, seed=None, freeze_torch=False, freeze_tf=False, logger=False, **kwargs):
    warnings.filterwarnings("ignore")

    pd.options.display.float_format = '{:.4f}'.format
    pd.set_option("display.max_colwidth", 300)

    if "seaborn-ticks" in plt.style.available:
        plt.style.use('seaborn-ticks')
    else:
        plt.style.use('seaborn-v0_8-ticks')

    font_path = font_path or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matplot_chinese.ttf')

    if font_path.lower() in [font.fname.lower() for font in font_manager.fontManager.ttflist]:
        plt.rcParams['font.family'] = font_path
    else:
        if not os.path.isfile(font_path):
            import wget
            font_path = wget.download(
                "https://itlubber.art/upload/matplot_chinese.ttf"
                , os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matplot_chinese.ttf')
            )

        font_manager.fontManager.addfont(font_path)
        plt.rcParams['font.family'] = font_manager.FontProperties(fname=font_path).get_name()

    plt.rcParams['axes.unicode_minus'] = False

    if seed:
        seed_everything(seed, freeze_torch=freeze_torch, freeze_tf=freeze_tf)

    if logger:
        return init_logger(**kwargs)
