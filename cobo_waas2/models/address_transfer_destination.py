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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.address_transfer_destination_account_output import AddressTransferDestinationAccountOutput
from cobo_waas2.models.address_transfer_destination_utxo_outputs_inner import AddressTransferDestinationUtxoOutputsInner
from cobo_waas2.models.transfer_destination_type import TransferDestinationType
from typing import Optional, Set
from typing_extensions import Self


class AddressTransferDestination(BaseModel):
    """
    The information about the transaction destination type `Address`.   Specify either the `account_output` property or the `utxo_outputs` property. Only MPC Wallets as the transaction source can transfer tokens to multiple addresses by using the `utxo_outputs` property. 
    """  # noqa: E501
    destination_type: TransferDestinationType
    account_output: Optional[AddressTransferDestinationAccountOutput] = None
    utxo_outputs: Optional[List[AddressTransferDestinationUtxoOutputsInner]] = None
    change_address: Optional[StrictStr] = Field(default=None, description="The address used to receive the remaining funds or change from the transaction.")
    force_internal: Optional[StrictBool] = Field(default=None, description="Whether the transaction request must be executed as a Loop transfer. For more information about Loop, see [Loop's website](https://loop.top/).   - `true`: The transaction request must be executed as a Loop transfer.   - `false`: The transaction request may not be executed as a Loop transfer. ")
    force_external: Optional[StrictBool] = Field(default=None, description="Whether the transaction request must not be executed as a Loop transfer. For more information about Loop, see [Loop's website](https://loop.top/).   - `true`: The transaction request must not be executed as a Loop transfer.   - `false`: The transaction request can be executed as a Loop transfer. ")
    __properties: ClassVar[List[str]] = ["destination_type", "account_output", "utxo_outputs", "change_address", "force_internal", "force_external"]

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
        """Create an instance of AddressTransferDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_output
        if self.account_output:
            _dict['account_output'] = self.account_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in utxo_outputs (list)
        _items = []
        if self.utxo_outputs:
            for _item in self.utxo_outputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['utxo_outputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddressTransferDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "account_output": AddressTransferDestinationAccountOutput.from_dict(obj["account_output"]) if obj.get("account_output") is not None else None,
            "utxo_outputs": [AddressTransferDestinationUtxoOutputsInner.from_dict(_item) for _item in obj["utxo_outputs"]] if obj.get("utxo_outputs") is not None else None,
            "change_address": obj.get("change_address"),
            "force_internal": obj.get("force_internal"),
            "force_external": obj.get("force_external")
        })
        return _obj


