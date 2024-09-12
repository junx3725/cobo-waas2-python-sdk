# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from cobo_waas2.models.transfer_destination_type import TransferDestinationType
from typing import Optional, Set
from typing_extensions import Self


class ExchangeTransferDestination(BaseModel):
    """
    The information about the transaction destination type `ExchangeWallet`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  An Exchange Wallet (Sub Account) can only receive asset transfers from another Exchange Wallet.  Switch between the tabs to display the properties for different transaction destinations. 
    """  # noqa: E501
    destination_type: TransferDestinationType
    wallet_id: StrictStr = Field(description="The wallet ID.")
    trading_account_type: StrictStr = Field(description="The trading account type.")
    amount: StrictStr = Field(description="The transfer amount. For example, if you trade 1.5 BTC, then the value is `1.5`. ")
    __properties: ClassVar[List[str]] = ["destination_type", "wallet_id", "trading_account_type", "amount"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ExchangeTransferDestination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeTransferDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "wallet_id": obj.get("wallet_id"),
            "trading_account_type": obj.get("trading_account_type"),
            "amount": obj.get("amount")
        })
        return _obj


