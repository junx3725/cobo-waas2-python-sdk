# coding: utf-8

# flake8: noqa

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.0"

# import apis into sdk package
from cobo_waas2.api.developers_webhooks_api import DevelopersWebhooksApi
from cobo_waas2.api.o_auth_api import OAuthApi
from cobo_waas2.api.transactions_api import TransactionsApi
from cobo_waas2.api.wallets_api import WalletsApi
from cobo_waas2.api.wallets_mpc_wallets_api import WalletsMPCWalletsApi

# import ApiClient
from cobo_waas2.api_response import ApiResponse
from cobo_waas2.api_client import ApiClient
from cobo_waas2.configuration import Configuration
from cobo_waas2.exceptions import OpenApiException
from cobo_waas2.exceptions import ApiTypeError
from cobo_waas2.exceptions import ApiValueError
from cobo_waas2.exceptions import ApiKeyError
from cobo_waas2.exceptions import ApiAttributeError
from cobo_waas2.exceptions import ApiException

# import models into sdk package
from cobo_waas2.models.activity import Activity
from cobo_waas2.models.activity_action import ActivityAction
from cobo_waas2.models.activity_initiator import ActivityInitiator
from cobo_waas2.models.activity_status import ActivityStatus
from cobo_waas2.models.activity_timeline import ActivityTimeline
from cobo_waas2.models.activity_type import ActivityType
from cobo_waas2.models.address_encoding import AddressEncoding
from cobo_waas2.models.address_info import AddressInfo
from cobo_waas2.models.address_transfer_destination import AddressTransferDestination
from cobo_waas2.models.address_transfer_destination_account_output import AddressTransferDestinationAccountOutput
from cobo_waas2.models.address_transfer_destination_utxo_outputs_inner import AddressTransferDestinationUtxoOutputsInner
from cobo_waas2.models.amount_details_inner import AmountDetailsInner
from cobo_waas2.models.amount_status import AmountStatus
from cobo_waas2.models.asset_balance import AssetBalance
from cobo_waas2.models.asset_info import AssetInfo
from cobo_waas2.models.babylon_stake_extra import BabylonStakeExtra
from cobo_waas2.models.babylon_validator import BabylonValidator
from cobo_waas2.models.base_contract_call_source import BaseContractCallSource
from cobo_waas2.models.base_estimate_staking_fee import BaseEstimateStakingFee
from cobo_waas2.models.base_stake_extra import BaseStakeExtra
from cobo_waas2.models.chain_info import ChainInfo
from cobo_waas2.models.check_address_validity200_response import CheckAddressValidity200Response
from cobo_waas2.models.cobo_safe_delegate import CoboSafeDelegate
from cobo_waas2.models.cobo_safe_delegate_type import CoboSafeDelegateType
from cobo_waas2.models.contract_call_destination import ContractCallDestination
from cobo_waas2.models.contract_call_destination_type import ContractCallDestinationType
from cobo_waas2.models.contract_call_params import ContractCallParams
from cobo_waas2.models.contract_call_source import ContractCallSource
from cobo_waas2.models.contract_call_source_type import ContractCallSourceType
from cobo_waas2.models.create_address_request import CreateAddressRequest
from cobo_waas2.models.create_custodial_wallet_params import CreateCustodialWalletParams
from cobo_waas2.models.create_exchange_wallet_params import CreateExchangeWalletParams
from cobo_waas2.models.create_key_share_holder import CreateKeyShareHolder
from cobo_waas2.models.create_key_share_holder_group_request import CreateKeyShareHolderGroupRequest
from cobo_waas2.models.create_mpc_project_request import CreateMpcProjectRequest
from cobo_waas2.models.create_mpc_vault_request import CreateMpcVaultRequest
from cobo_waas2.models.create_mpc_wallet_params import CreateMpcWalletParams
from cobo_waas2.models.create_safe_wallet_params import CreateSafeWalletParams
from cobo_waas2.models.create_smart_contract_wallet_params import CreateSmartContractWalletParams
from cobo_waas2.models.create_stake_activity import CreateStakeActivity
from cobo_waas2.models.create_stake_activity_extra import CreateStakeActivityExtra
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.create_tss_request_request import CreateTssRequestRequest
from cobo_waas2.models.create_unstake_activity import CreateUnstakeActivity
from cobo_waas2.models.create_wallet_params import CreateWalletParams
from cobo_waas2.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest
from cobo_waas2.models.create_withdraw_activity import CreateWithdrawActivity
from cobo_waas2.models.created_wallet_info import CreatedWalletInfo
from cobo_waas2.models.curve_type import CurveType
from cobo_waas2.models.custodial_transfer_source import CustodialTransferSource
from cobo_waas2.models.custodial_wallet_info import CustodialWalletInfo
from cobo_waas2.models.delete_key_share_holder_group_by_id201_response import DeleteKeyShareHolderGroupById201Response
from cobo_waas2.models.delete_wallet_by_id201_response import DeleteWalletById201Response
from cobo_waas2.models.eigen_layer_lst_stake_extra import EigenLayerLstStakeExtra
from cobo_waas2.models.eigen_layer_native_stake_extra import EigenLayerNativeStakeExtra
from cobo_waas2.models.eigenlayer_validator import EigenlayerValidator
from cobo_waas2.models.error_response import ErrorResponse
from cobo_waas2.models.estimate_contract_call_fee_params import EstimateContractCallFeeParams
from cobo_waas2.models.estimate_fee_params import EstimateFeeParams
from cobo_waas2.models.estimate_fee_request_type import EstimateFeeRequestType
from cobo_waas2.models.estimate_stake_fee import EstimateStakeFee
from cobo_waas2.models.estimate_transfer_fee_params import EstimateTransferFeeParams
from cobo_waas2.models.estimate_unstake_fee import EstimateUnstakeFee
from cobo_waas2.models.estimate_withdraw_fee import EstimateWithdrawFee
from cobo_waas2.models.estimated_evm_eip1559_fee import EstimatedEvmEip1559Fee
from cobo_waas2.models.estimated_evm_eip1559_fee_slow import EstimatedEvmEip1559FeeSlow
from cobo_waas2.models.estimated_evm_legacy_fee import EstimatedEvmLegacyFee
from cobo_waas2.models.estimated_evm_legacy_fee_slow import EstimatedEvmLegacyFeeSlow
from cobo_waas2.models.estimated_fee import EstimatedFee
from cobo_waas2.models.estimated_fixed_fee import EstimatedFixedFee
from cobo_waas2.models.estimated_utxo_fee import EstimatedUtxoFee
from cobo_waas2.models.estimated_utxo_fee_slow import EstimatedUtxoFeeSlow
from cobo_waas2.models.evm_contract_call_destination import EvmContractCallDestination
from cobo_waas2.models.evm_eip191_message_sign_destination import EvmEIP191MessageSignDestination
from cobo_waas2.models.evm_eip712_message_sign_destination import EvmEIP712MessageSignDestination
from cobo_waas2.models.evm_eip1559_fee_base_price import EvmEip1559FeeBasePrice
from cobo_waas2.models.evm_eip1559_fee_rate import EvmEip1559FeeRate
from cobo_waas2.models.evm_legacy_fee_base_price import EvmLegacyFeeBasePrice
from cobo_waas2.models.evm_legacy_fee_rate import EvmLegacyFeeRate
from cobo_waas2.models.exchange_id import ExchangeId
from cobo_waas2.models.exchange_transfer_destination import ExchangeTransferDestination
from cobo_waas2.models.exchange_transfer_source import ExchangeTransferSource
from cobo_waas2.models.exchange_wallet_info import ExchangeWalletInfo
from cobo_waas2.models.extended_token_info import ExtendedTokenInfo
from cobo_waas2.models.fee_amount import FeeAmount
from cobo_waas2.models.fee_gas_limit import FeeGasLimit
from cobo_waas2.models.fee_rate import FeeRate
from cobo_waas2.models.fee_type import FeeType
from cobo_waas2.models.fixed_fee_rate import FixedFeeRate
from cobo_waas2.models.get_token200_response import GetToken200Response
from cobo_waas2.models.get_token4_xx_response import GetToken4XXResponse
from cobo_waas2.models.key_share_holder import KeyShareHolder
from cobo_waas2.models.key_share_holder_group import KeyShareHolderGroup
from cobo_waas2.models.key_share_holder_group_status import KeyShareHolderGroupStatus
from cobo_waas2.models.key_share_holder_group_type import KeyShareHolderGroupType
from cobo_waas2.models.key_share_holder_status import KeyShareHolderStatus
from cobo_waas2.models.key_share_holder_type import KeyShareHolderType
from cobo_waas2.models.list_addresses200_response import ListAddresses200Response
from cobo_waas2.models.list_key_share_holder_groups200_response import ListKeyShareHolderGroups200Response
from cobo_waas2.models.list_mpc_projects200_response import ListMpcProjects200Response
from cobo_waas2.models.list_mpc_vaults200_response import ListMpcVaults200Response
from cobo_waas2.models.list_supported_chains200_response import ListSupportedChains200Response
from cobo_waas2.models.list_supported_tokens200_response import ListSupportedTokens200Response
from cobo_waas2.models.list_token_balances_for_address200_response import ListTokenBalancesForAddress200Response
from cobo_waas2.models.list_transactions200_response import ListTransactions200Response
from cobo_waas2.models.list_tss_requests200_response import ListTssRequests200Response
from cobo_waas2.models.list_utxos200_response import ListUtxos200Response
from cobo_waas2.models.list_wallets200_response import ListWallets200Response
from cobo_waas2.models.list_webhook_endpoints200_response import ListWebhookEndpoints200Response
from cobo_waas2.models.list_webhook_event_definitions200_response_inner import ListWebhookEventDefinitions200ResponseInner
from cobo_waas2.models.list_webhook_event_logs200_response import ListWebhookEventLogs200Response
from cobo_waas2.models.list_webhook_events200_response import ListWebhookEvents200Response
from cobo_waas2.models.lock_utxos201_response import LockUtxos201Response
from cobo_waas2.models.lock_utxos_request import LockUtxosRequest
from cobo_waas2.models.lock_utxos_request_utxos_inner import LockUtxosRequestUtxosInner
from cobo_waas2.models.mpc_delegate import MPCDelegate
from cobo_waas2.models.mpc_project import MPCProject
from cobo_waas2.models.mpc_vault import MPCVault
from cobo_waas2.models.mpc_vault_type import MPCVaultType
from cobo_waas2.models.mpc_wallet_info import MPCWalletInfo
from cobo_waas2.models.max_fee_amount import MaxFeeAmount
from cobo_waas2.models.max_transferable_value import MaxTransferableValue
from cobo_waas2.models.message_sign_destination import MessageSignDestination
from cobo_waas2.models.message_sign_destination_type import MessageSignDestinationType
from cobo_waas2.models.message_sign_params import MessageSignParams
from cobo_waas2.models.message_sign_source import MessageSignSource
from cobo_waas2.models.message_sign_source_type import MessageSignSourceType
from cobo_waas2.models.mpc_contract_call_source import MpcContractCallSource
from cobo_waas2.models.mpc_message_sign_source import MpcMessageSignSource
from cobo_waas2.models.mpc_signing_group import MpcSigningGroup
from cobo_waas2.models.mpc_transfer_source import MpcTransferSource
from cobo_waas2.models.pagination import Pagination
from cobo_waas2.models.pool_details import PoolDetails
from cobo_waas2.models.pool_details_all_of_validators_info import PoolDetailsAllOfValidatorsInfo
from cobo_waas2.models.pool_summary import PoolSummary
from cobo_waas2.models.refresh_token_request import RefreshTokenRequest
from cobo_waas2.models.replace_type import ReplaceType
from cobo_waas2.models.retry_webhook_event_by_id201_response import RetryWebhookEventById201Response
from cobo_waas2.models.root_pubkey import RootPubkey
from cobo_waas2.models.safe_contract_call_source import SafeContractCallSource
from cobo_waas2.models.safe_transfer_source import SafeTransferSource
from cobo_waas2.models.safe_wallet import SafeWallet
from cobo_waas2.models.smart_contract_initiator import SmartContractInitiator
from cobo_waas2.models.smart_contract_wallet_info import SmartContractWalletInfo
from cobo_waas2.models.smart_contract_wallet_operation_type import SmartContractWalletOperationType
from cobo_waas2.models.smart_contract_wallet_type import SmartContractWalletType
from cobo_waas2.models.source_group import SourceGroup
from cobo_waas2.models.staking_pool_type import StakingPoolType
from cobo_waas2.models.staking_source import StakingSource
from cobo_waas2.models.stakings import Stakings
from cobo_waas2.models.stakings_validator_info import StakingsValidatorInfo
from cobo_waas2.models.sub_wallet_asset_balance import SubWalletAssetBalance
from cobo_waas2.models.tss_groups import TSSGroups
from cobo_waas2.models.tss_request import TSSRequest
from cobo_waas2.models.tss_request_status import TSSRequestStatus
from cobo_waas2.models.tss_request_type import TSSRequestType
from cobo_waas2.models.token_balance import TokenBalance
from cobo_waas2.models.token_balance_balance import TokenBalanceBalance
from cobo_waas2.models.token_info import TokenInfo
from cobo_waas2.models.transaction import Transaction
from cobo_waas2.models.transaction_approver import TransactionApprover
from cobo_waas2.models.transaction_block_info import TransactionBlockInfo
from cobo_waas2.models.transaction_custodial_asset_wallet_source import TransactionCustodialAssetWalletSource
from cobo_waas2.models.transaction_deposit_from_address_source import TransactionDepositFromAddressSource
from cobo_waas2.models.transaction_deposit_from_loop_source import TransactionDepositFromLoopSource
from cobo_waas2.models.transaction_deposit_from_wallet_source import TransactionDepositFromWalletSource
from cobo_waas2.models.transaction_deposit_to_address_destination import TransactionDepositToAddressDestination
from cobo_waas2.models.transaction_deposit_to_wallet_destination import TransactionDepositToWalletDestination
from cobo_waas2.models.transaction_destination import TransactionDestination
from cobo_waas2.models.transaction_destination_type import TransactionDestinationType
from cobo_waas2.models.transaction_detail import TransactionDetail
from cobo_waas2.models.transaction_details import TransactionDetails
from cobo_waas2.models.transaction_evm_contract_destination import TransactionEvmContractDestination
from cobo_waas2.models.transaction_evm_eip1559_fee import TransactionEvmEip1559Fee
from cobo_waas2.models.transaction_evm_legacy_fee import TransactionEvmLegacyFee
from cobo_waas2.models.transaction_exchange_wallet_source import TransactionExchangeWalletSource
from cobo_waas2.models.transaction_fee import TransactionFee
from cobo_waas2.models.transaction_fee_station_wallet_source import TransactionFeeStationWalletSource
from cobo_waas2.models.transaction_fixed_fee import TransactionFixedFee
from cobo_waas2.models.transaction_initiator_type import TransactionInitiatorType
from cobo_waas2.models.transaction_mpc_wallet_source import TransactionMPCWalletSource
from cobo_waas2.models.transaction_message_sign_eip191_destination import TransactionMessageSignEIP191Destination
from cobo_waas2.models.transaction_message_sign_eip712_destination import TransactionMessageSignEIP712Destination
from cobo_waas2.models.transaction_raw_tx_info import TransactionRawTxInfo
from cobo_waas2.models.transaction_rbf import TransactionRbf
from cobo_waas2.models.transaction_rbf_source import TransactionRbfSource
from cobo_waas2.models.transaction_replacement import TransactionReplacement
from cobo_waas2.models.transaction_request_evm_eip1559_fee import TransactionRequestEvmEip1559Fee
from cobo_waas2.models.transaction_request_evm_legacy_fee import TransactionRequestEvmLegacyFee
from cobo_waas2.models.transaction_request_fee import TransactionRequestFee
from cobo_waas2.models.transaction_request_fixed_fee import TransactionRequestFixedFee
from cobo_waas2.models.transaction_request_utxo_fee import TransactionRequestUtxoFee
from cobo_waas2.models.transaction_resend import TransactionResend
from cobo_waas2.models.transaction_result import TransactionResult
from cobo_waas2.models.transaction_result_type import TransactionResultType
from cobo_waas2.models.transaction_signature_result import TransactionSignatureResult
from cobo_waas2.models.transaction_signer import TransactionSigner
from cobo_waas2.models.transaction_smart_contract_safe_wallet_source import TransactionSmartContractSafeWalletSource
from cobo_waas2.models.transaction_source import TransactionSource
from cobo_waas2.models.transaction_source_type import TransactionSourceType
from cobo_waas2.models.transaction_status import TransactionStatus
from cobo_waas2.models.transaction_sub_status import TransactionSubStatus
from cobo_waas2.models.transaction_timeline import TransactionTimeline
from cobo_waas2.models.transaction_toke_approval import TransactionTokeApproval
from cobo_waas2.models.transaction_token_amount import TransactionTokenAmount
from cobo_waas2.models.transaction_transfer_to_address_destination import TransactionTransferToAddressDestination
from cobo_waas2.models.transaction_transfer_to_address_destination_account_output import TransactionTransferToAddressDestinationAccountOutput
from cobo_waas2.models.transaction_transfer_to_address_destination_utxo_outputs_inner import TransactionTransferToAddressDestinationUtxoOutputsInner
from cobo_waas2.models.transaction_transfer_to_wallet_destination import TransactionTransferToWalletDestination
from cobo_waas2.models.transaction_type import TransactionType
from cobo_waas2.models.transaction_utxo import TransactionUtxo
from cobo_waas2.models.transaction_utxo_fee import TransactionUtxoFee
from cobo_waas2.models.transaction_webhook_event_data import TransactionWebhookEventData
from cobo_waas2.models.transfer_destination import TransferDestination
from cobo_waas2.models.transfer_destination_type import TransferDestinationType
from cobo_waas2.models.transfer_params import TransferParams
from cobo_waas2.models.transfer_source import TransferSource
from cobo_waas2.models.utxo import UTXO
from cobo_waas2.models.update_custodial_wallet_params import UpdateCustodialWalletParams
from cobo_waas2.models.update_exchange_wallet_params import UpdateExchangeWalletParams
from cobo_waas2.models.update_group_action import UpdateGroupAction
from cobo_waas2.models.update_key_share_holder_group_by_id_request import UpdateKeyShareHolderGroupByIdRequest
from cobo_waas2.models.update_mpc_project_by_id_request import UpdateMpcProjectByIdRequest
from cobo_waas2.models.update_mpc_vault_by_id_request import UpdateMpcVaultByIdRequest
from cobo_waas2.models.update_mpc_wallet_params import UpdateMpcWalletParams
from cobo_waas2.models.update_smart_contract_wallet_params import UpdateSmartContractWalletParams
from cobo_waas2.models.update_wallet_params import UpdateWalletParams
from cobo_waas2.models.update_webhook_endpoint_by_id_request import UpdateWebhookEndpointByIdRequest
from cobo_waas2.models.utxo_fee_base_price import UtxoFeeBasePrice
from cobo_waas2.models.utxo_fee_rate import UtxoFeeRate
from cobo_waas2.models.wallet_info import WalletInfo
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
from cobo_waas2.models.webhook_endpoint import WebhookEndpoint
from cobo_waas2.models.webhook_endpoint_status import WebhookEndpointStatus
from cobo_waas2.models.webhook_event import WebhookEvent
from cobo_waas2.models.webhook_event_data import WebhookEventData
from cobo_waas2.models.webhook_event_data_type import WebhookEventDataType
from cobo_waas2.models.webhook_event_log import WebhookEventLog
from cobo_waas2.models.webhook_event_status import WebhookEventStatus
from cobo_waas2.models.webhook_event_type import WebhookEventType
