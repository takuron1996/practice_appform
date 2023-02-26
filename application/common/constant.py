#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""定数関連のモジュール
"""
from enum import Enum


class LoggerName(Enum):
    """ロガー名"""

    APPLICATION = "application"
    """アプリケーションロガー用"""
    EMERGENCY = "emergency"
    """エマージェンシーロガー用"""
