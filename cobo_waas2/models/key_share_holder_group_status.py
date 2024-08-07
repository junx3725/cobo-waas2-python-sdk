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


class KeyShareHolderGroupStatus(str, Enum):
    """
    The status of the key share holder group. Possible values include: - `New`: The key share holder group has been newly created. The status will become `Valid` after you call [Create TSS request](/api-references/v2/wallets--mpc-wallet/create-a-tss-request-to-generate-key-secrets-for-a-tss-group) and specifying this key share holder group as the target key share holder group.  - `Valid`: The key share holder group is valid.  - `Unavailable`: The key share holder group is currently unavailable. This status appears when a key share holder uses [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/back-up-key-share-groups#mobile-co-signer) to change node. For example, when a key share holder changes to a new phone or loses their phone, and is in the process of setting up [Cobo Guard](https://manuals.cobo.com/en/guard/introduction) on their new phone. 
    """

    """
    allowed enum values
    """
    NEW = 'New'
    VALID = 'Valid'
    UNAVAILABLE = 'Unavailable'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of KeyShareHolderGroupStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


