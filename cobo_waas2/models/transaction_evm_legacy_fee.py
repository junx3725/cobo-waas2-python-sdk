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
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class TransactionEvmLegacyFee(BaseModel):
    """
    The transaction fee actually charged by the chain that uses the legacy fee model.   The transaction fee is calculated by multiplying the gas price by the used gas. This can be expressed as: Transaction fee = gas price * used gas units.  Switch between the tabs to display the properties for different transaction fee models. 
    """  # noqa: E501
    gas_price: Optional[StrictStr] = Field(default=None, description="The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used.")
    gas_limit: Optional[StrictStr] = Field(default='21000', description="The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies.")
    fee_type: FeeType
    token_id: Optional[StrictStr] = Field(default=None, description="The token ID of the transaction fee.")
    fee_used: Optional[StrictStr] = Field(default=None, description="The transaction fee.")
    gas_used: Optional[StrictStr] = Field(default=None, description="The gas units used in the transaction.")
    __properties: ClassVar[List[str]] = ["gas_price", "gas_limit", "fee_type", "token_id", "fee_used", "gas_used"]

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
        """Create an instance of TransactionEvmLegacyFee from a JSON string"""
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
        """Create an instance of TransactionEvmLegacyFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gas_price": obj.get("gas_price"),
            "gas_limit": obj.get("gas_limit") if obj.get("gas_limit") is not None else '21000',
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "fee_used": obj.get("fee_used"),
            "gas_used": obj.get("gas_used")
        })
        return _obj


