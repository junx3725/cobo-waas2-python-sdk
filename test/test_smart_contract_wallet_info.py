# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.smart_contract_wallet_info import SmartContractWalletInfo


class TestSmartContractWalletInfo(unittest.TestCase):
    """SmartContractWalletInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartContractWalletInfo:
        """Test SmartContractWalletInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmartContractWalletInfo`
        """
        model = SmartContractWalletInfo()
        if include_optional:
            return SmartContractWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                chain_id = 'ETH',
                smart_contract_wallet_type = 'Safe{Wallet}',
                safe_address = '0x1234567890123456789012345678901234567890',
                signers = [
                    '0x1234567890123456789012345678901234567890'
                    ],
                threshold = 2,
                cobo_safe_address = '0x1234567890123456789012345678901234567890',
                initiator = cobo_waas2.models.initiator_wallets.Initiator Wallets(
                    wallet_id = '123e4567-e89b-12d3-a456-426614174000', 
                    address = '0x1234567890123456789012345678901234567890', )
            )
        else:
            return SmartContractWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                smart_contract_wallet_type = 'Safe{Wallet}',
        )
        """

    def testSmartContractWalletInfo(self):
        """Test SmartContractWalletInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
