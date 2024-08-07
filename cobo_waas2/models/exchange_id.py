# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ExchangeId(str, Enum):
    """
    The ID of the exchange:   - `binance`: Binance.   - `okx`: OKX.   - `deribit`: Deribit.   - `bybit`: Bybit.   - `gate`: Gate.io 
    """

    """
    allowed enum values
    """
    BINANCE = 'binance'
    OKX = 'okx'
    DERIBIT = 'deribit'
    BYBIT = 'bybit'
    GATE = 'gate'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ExchangeId from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


