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


class KeyShareHolderGroupType(str, Enum):
    """
    The type of key share holder group. Possible values include:  - `MainGroup`: A [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups).  - `SigningGroup`: A [Signing Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups).  - `RecoveryGroup`: A [Recovery Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups).  **Note:** For `MainGroup` and `SigningGroup`, a Cobo key share holder will be added automatically. 
    """

    """
    allowed enum values
    """
    MAINGROUP = 'MainGroup'
    SIGNINGGROUP = 'SigningGroup'
    RECOVERYGROUP = 'RecoveryGroup'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of KeyShareHolderGroupType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


