"""Spacing tokens for the design system."""

from __future__ import annotations

from pydantic import BaseModel


class Spacing(BaseModel, frozen=True):
    """Design system spacing tokens."""

    # Base spacing unit (px)
    _0: str = "0"
    _0_5: str = "0.125rem"  # 2px
    _1: str = "0.25rem"  # 4px
    _1_5: str = "0.375rem"  # 6px
    _2: str = "0.5rem"  # 8px
    _2_5: str = "0.625rem"  # 10px
    _3: str = "0.75rem"  # 12px
    _3_5: str = "0.875rem"  # 14px
    _4: str = "1rem"  # 16px
    _5: str = "1.25rem"  # 20px
    _6: str = "1.5rem"  # 24px
    _7: str = "1.75rem"  # 28px
    _8: str = "2rem"  # 32px
    _9: str = "2.25rem"  # 36px
    _10: str = "2.5rem"  # 40px
    _11: str = "2.75rem"  # 44px
    _12: str = "3rem"  # 48px
    _14: str = "3.5rem"  # 56px
    _16: str = "4rem"  # 64px
    _20: str = "5rem"  # 80px
    _24: str = "6rem"  # 96px
    _28: str = "7rem"  # 112px
    _32: str = "8rem"  # 128px
    _36: str = "9rem"  # 144px
    _40: str = "10rem"  # 160px
    _44: str = "11rem"  # 176px
    _48: str = "12rem"  # 192px
    _52: str = "13rem"  # 208px
    _56: str = "14rem"  # 224px
    _60: str = "15rem"  # 240px
    _64: str = "16rem"  # 256px
    _72: str = "18rem"  # 288px
    _80: str = "20rem"  # 320px
    _96: str = "24rem"  # 384px
