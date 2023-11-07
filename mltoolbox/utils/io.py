# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/7 17:44
@Author  : itlubber
@Site    : itlubber.art
"""

import joblib


def load_pickle(file):
    return joblib.load(file)


def save_pickle(obj, file):
    joblib.dump(obj, file)
