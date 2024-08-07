# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.address_transfer_destination import AddressTransferDestination
from cobo_waas2.models.exchange_transfer_destination import ExchangeTransferDestination
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSFERDESTINATION_ONE_OF_SCHEMAS = ["AddressTransferDestination", "ExchangeTransferDestination"]

class TransferDestination(BaseModel):
    """
    TransferDestination
    """
    # data type: AddressTransferDestination
    oneof_schema_1_validator: Optional[AddressTransferDestination] = None
    # data type: ExchangeTransferDestination
    oneof_schema_2_validator: Optional[ExchangeTransferDestination] = None
    actual_instance: Optional[Union[AddressTransferDestination, ExchangeTransferDestination]] = None
    one_of_schemas: Set[str] = { "AddressTransferDestination", "ExchangeTransferDestination" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TransferDestination.model_construct()
        error_messages = []
        match = 0
        # validate data type: AddressTransferDestination
        if not isinstance(v, AddressTransferDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AddressTransferDestination`")
        else:
            match += 1
        # validate data type: ExchangeTransferDestination
        if not isinstance(v, ExchangeTransferDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExchangeTransferDestination`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransferDestination with oneOf schemas: AddressTransferDestination, ExchangeTransferDestination. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransferDestination with oneOf schemas: AddressTransferDestination, ExchangeTransferDestination. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("destination_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `destination_type` in the input.")

        # check if data type is `AddressTransferDestination`
        if _data_type == "Address":
            instance.actual_instance = AddressTransferDestination.from_json(json_str)
            return instance

        # check if data type is `ExchangeTransferDestination`
        if _data_type == "ExchangeWallet":
            instance.actual_instance = ExchangeTransferDestination.from_json(json_str)
            return instance

        # check if data type is `AddressTransferDestination`
        if _data_type == "AddressTransferDestination":
            instance.actual_instance = AddressTransferDestination.from_json(json_str)
            return instance

        # check if data type is `ExchangeTransferDestination`
        if _data_type == "ExchangeTransferDestination":
            instance.actual_instance = ExchangeTransferDestination.from_json(json_str)
            return instance

        # deserialize data into AddressTransferDestination
        try:
            instance.actual_instance = AddressTransferDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExchangeTransferDestination
        try:
            instance.actual_instance = ExchangeTransferDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransferDestination with oneOf schemas: AddressTransferDestination, ExchangeTransferDestination. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into TransferDestination with oneOf schemas: AddressTransferDestination, ExchangeTransferDestination. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AddressTransferDestination, ExchangeTransferDestination]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


