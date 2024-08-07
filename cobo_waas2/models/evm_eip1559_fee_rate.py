# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.evm_eip1559_fee_base_price import EvmEip1559FeeBasePrice
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class EvmEip1559FeeRate(BaseModel):
    """
    The transaction fee rate based on the EIP-1559 fee model.
    """  # noqa: E501
    fee_type: FeeType
    token_id: StrictStr = Field(description="The token ID of the transaction fee.")
    slow: Optional[EvmEip1559FeeBasePrice] = None
    recommended: EvmEip1559FeeBasePrice
    fast: Optional[EvmEip1559FeeBasePrice] = None
    __properties: ClassVar[List[str]] = ["fee_type", "token_id", "slow", "recommended", "fast"]

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
        """Create an instance of EvmEip1559FeeRate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of slow
        if self.slow:
            _dict['slow'] = self.slow.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recommended
        if self.recommended:
            _dict['recommended'] = self.recommended.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fast
        if self.fast:
            _dict['fast'] = self.fast.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EvmEip1559FeeRate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "slow": EvmEip1559FeeBasePrice.from_dict(obj["slow"]) if obj.get("slow") is not None else None,
            "recommended": EvmEip1559FeeBasePrice.from_dict(obj["recommended"]) if obj.get("recommended") is not None else None,
            "fast": EvmEip1559FeeBasePrice.from_dict(obj["fast"]) if obj.get("fast") is not None else None
        })
        return _obj


