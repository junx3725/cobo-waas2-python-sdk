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


class FeeType(str, Enum):
    """
    The fee model. Possible values include: - `Fixed`: The fixed fee model.  - `EVM_EIP_1559`: The EIP-1559 fee model. - `EVM_Legacy`: The legacy fee model. - `UTXO`: The fee model used in UTXO-based blockchains, such as Bitcoin. 
    """

    """
    allowed enum values
    """
    FIXED = 'Fixed'
    EVM_EIP_1559 = 'EVM_EIP_1559'
    EVM_LEGACY = 'EVM_Legacy'
    UTXO = 'UTXO'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FeeType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


