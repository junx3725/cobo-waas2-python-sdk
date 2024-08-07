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


class ReplaceType(str, Enum):
    """
    The `replaced_by_type` property indicates the replacement type of the transaction that this transaction was replaced by, and the `replaced_type` property indicates the replacement type of the transaction that this transaction replaced. Possible values include:    - `Drop`: To drop a transaction.   - `Resend`: To resend a transaction.   - `SpeedUp`: To speed up a transaction. 
    """

    """
    allowed enum values
    """
    DROP = 'Drop'
    RESEND = 'Resend'
    SPEEDUP = 'SpeedUp'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReplaceType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


