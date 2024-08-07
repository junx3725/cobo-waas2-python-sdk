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


class TransactionInitiatorType(str, Enum):
    """
    The transaction initiator type. Possible values include:   - `API`: An API initiator, who initiates the transaction by using the WaaS API.   - `Web`: An web initiator, who initiates the transaction from Cobo Portal.   - `App`: An App initiator, who initiates the transaction from Cobo Portal Apps.   - `External`: An external initiator, who initiates the transaction outside Cobo. 
    """

    """
    allowed enum values
    """
    API = 'API'
    WEB = 'Web'
    APP = 'App'
    EXTERNAL = 'External'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionInitiatorType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


