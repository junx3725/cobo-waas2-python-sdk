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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.transaction_approver import TransactionApprover
from cobo_waas2.models.transaction_block_info import TransactionBlockInfo
from cobo_waas2.models.transaction_destination import TransactionDestination
from cobo_waas2.models.transaction_initiator_type import TransactionInitiatorType
from cobo_waas2.models.transaction_raw_tx_info import TransactionRawTxInfo
from cobo_waas2.models.transaction_replacement import TransactionReplacement
from cobo_waas2.models.transaction_request_fee import TransactionRequestFee
from cobo_waas2.models.transaction_result import TransactionResult
from cobo_waas2.models.transaction_signer import TransactionSigner
from cobo_waas2.models.transaction_source import TransactionSource
from cobo_waas2.models.transaction_status import TransactionStatus
from cobo_waas2.models.transaction_sub_status import TransactionSubStatus
from cobo_waas2.models.transaction_timeline import TransactionTimeline
from cobo_waas2.models.transaction_toke_approval import TransactionTokeApproval
from cobo_waas2.models.transaction_type import TransactionType
from typing import Optional, Set
from typing_extensions import Self


class TransactionDetails(BaseModel):
    """
    TransactionDetails
    """  # noqa: E501
    transaction_id: StrictStr = Field(description="The transaction ID.")
    cobo_id: Optional[StrictStr] = Field(default=None, description="The Cobo ID, which can be used to track a transaction.")
    request_id: Optional[StrictStr] = Field(default=None, description="The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization.")
    wallet_id: StrictStr = Field(description="For deposit transactions, this property represents the wallet ID of the transaction destination. For transactions of other types, this property represents the wallet ID of the transaction source.")
    type: Optional[TransactionType] = None
    status: TransactionStatus
    sub_status: Optional[TransactionSubStatus] = None
    failed_reason: Optional[StrictStr] = Field(default=None, description="(This property is applicable to approval failures and signature failures only) The reason why the transaction failed.")
    chain_id: Optional[StrictStr] = Field(default=None, description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains).")
    token_id: Optional[StrictStr] = Field(default=None, description="The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens).")
    asset_id: Optional[StrictStr] = Field(default=None, description="(This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account.")
    source: TransactionSource
    destination: TransactionDestination
    result: Optional[TransactionResult] = None
    fee: Optional[TransactionRequestFee] = None
    initiator: Optional[StrictStr] = Field(default=None, description="Transaction initiator")
    initiator_type: TransactionInitiatorType
    confirmed_num: Optional[StrictInt] = Field(default=None, description="Transaction confirmed number")
    confirming_threshold: Optional[StrictInt] = Field(default=None, description="Number of confirmations required for a transaction, such as 15 for ETH chain.")
    transaction_hash: Optional[StrictStr] = Field(default=None, description="The transaction hash.")
    block_info: Optional[TransactionBlockInfo] = None
    raw_tx_info: Optional[TransactionRawTxInfo] = None
    replacement: Optional[TransactionReplacement] = None
    category: Optional[List[StrictStr]] = Field(default=None, description="A custom transaction category for you to identify your transfers more easily.")
    description: Optional[StrictStr] = Field(default=None, description="The description for your transaction.")
    is_loop: Optional[StrictBool] = Field(default=None, description="Whether the transaction is a Loop transfer. For more information about Loop, see [Loop's website](https://loop.top/).  - `true`: The transaction is a Loop transfer. - `false`: The transaction is not a Loop transfer. ")
    created_timestamp: Optional[StrictInt] = Field(default=None, description="The time when the transaction was created, in Unix timestamp format, measured in milliseconds.")
    updated_timestamp: Optional[StrictInt] = Field(default=None, description="The time when the transaction was updated, in Unix timestamp format, measured in milliseconds.")
    approvers: Optional[List[TransactionApprover]] = None
    signers: Optional[List[TransactionSigner]] = None
    nonce: Optional[StrictInt] = Field(default=None, description="Transaction nonce")
    replaced_by: Optional[StrictStr] = Field(default=None, description="Replace by transaction hash")
    fueled_by: Optional[StrictStr] = Field(default=None, description="Fueled by address")
    token_approval: Optional[TransactionTokeApproval] = None
    message: Optional[StrictStr] = Field(default=None, description="Transaction raw message")
    algorithm: Optional[StrictStr] = Field(default=None, description="Transaction message signing algorithm")
    timeline: Optional[List[TransactionTimeline]] = None
    __properties: ClassVar[List[str]] = ["transaction_id", "cobo_id", "request_id", "wallet_id", "type", "status", "sub_status", "failed_reason", "chain_id", "token_id", "asset_id", "source", "destination", "result", "fee", "initiator", "initiator_type", "confirmed_num", "confirming_threshold", "transaction_hash", "block_info", "raw_tx_info", "replacement", "category", "description", "is_loop", "created_timestamp", "updated_timestamp", "approvers", "signers", "nonce", "replaced_by", "fueled_by", "token_approval", "message", "algorithm", "timeline"]

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
        """Create an instance of TransactionDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of block_info
        if self.block_info:
            _dict['block_info'] = self.block_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of raw_tx_info
        if self.raw_tx_info:
            _dict['raw_tx_info'] = self.raw_tx_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of replacement
        if self.replacement:
            _dict['replacement'] = self.replacement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in approvers (list)
        _items = []
        if self.approvers:
            for _item in self.approvers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in signers (list)
        _items = []
        if self.signers:
            for _item in self.signers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['signers'] = _items
        # override the default output from pydantic by calling `to_dict()` of token_approval
        if self.token_approval:
            _dict['token_approval'] = self.token_approval.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in timeline (list)
        _items = []
        if self.timeline:
            for _item in self.timeline:
                if _item:
                    _items.append(_item.to_dict())
            _dict['timeline'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transaction_id": obj.get("transaction_id"),
            "cobo_id": obj.get("cobo_id"),
            "request_id": obj.get("request_id"),
            "wallet_id": obj.get("wallet_id"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "sub_status": obj.get("sub_status"),
            "failed_reason": obj.get("failed_reason"),
            "chain_id": obj.get("chain_id"),
            "token_id": obj.get("token_id"),
            "asset_id": obj.get("asset_id"),
            "source": TransactionSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "destination": TransactionDestination.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "result": TransactionResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "fee": TransactionRequestFee.from_dict(obj["fee"]) if obj.get("fee") is not None else None,
            "initiator": obj.get("initiator"),
            "initiator_type": obj.get("initiator_type"),
            "confirmed_num": obj.get("confirmed_num"),
            "confirming_threshold": obj.get("confirming_threshold"),
            "transaction_hash": obj.get("transaction_hash"),
            "block_info": TransactionBlockInfo.from_dict(obj["block_info"]) if obj.get("block_info") is not None else None,
            "raw_tx_info": TransactionRawTxInfo.from_dict(obj["raw_tx_info"]) if obj.get("raw_tx_info") is not None else None,
            "replacement": TransactionReplacement.from_dict(obj["replacement"]) if obj.get("replacement") is not None else None,
            "category": obj.get("category"),
            "description": obj.get("description"),
            "is_loop": obj.get("is_loop"),
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp"),
            "approvers": [TransactionApprover.from_dict(_item) for _item in obj["approvers"]] if obj.get("approvers") is not None else None,
            "signers": [TransactionSigner.from_dict(_item) for _item in obj["signers"]] if obj.get("signers") is not None else None,
            "nonce": obj.get("nonce"),
            "replaced_by": obj.get("replaced_by"),
            "fueled_by": obj.get("fueled_by"),
            "token_approval": TransactionTokeApproval.from_dict(obj["token_approval"]) if obj.get("token_approval") is not None else None,
            "message": obj.get("message"),
            "algorithm": obj.get("algorithm"),
            "timeline": [TransactionTimeline.from_dict(_item) for _item in obj["timeline"]] if obj.get("timeline") is not None else None
        })
        return _obj


