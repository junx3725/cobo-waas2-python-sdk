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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class MPCProject(BaseModel):
    """
    The data for project information.
    """  # noqa: E501
    project_id: Optional[StrictStr] = Field(default=None, description="The project ID.")
    org_id: Optional[StrictStr] = Field(default=None, description="The [organization](https://manuals.cobo.com/en/portal/organization/introduction) ID.")
    name: Optional[StrictStr] = Field(default=None, description="The project name.")
    participants: Optional[StrictInt] = Field(default=None, description="The number of key share holders in the project.")
    threshold: Optional[StrictInt] = Field(default=None, description="The number of key share holders required to sign an operation in the project.")
    create_timestamp: Optional[StrictInt] = Field(default=None, description="The project's creation time in Unix timestamp format, measured in milliseconds.")
    __properties: ClassVar[List[str]] = ["project_id", "org_id", "name", "participants", "threshold", "create_timestamp"]

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
        """Create an instance of MPCProject from a JSON string"""
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
        """Create an instance of MPCProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "org_id": obj.get("org_id"),
            "name": obj.get("name"),
            "participants": obj.get("participants"),
            "threshold": obj.get("threshold"),
            "create_timestamp": obj.get("create_timestamp")
        })
        return _obj


