# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.update_exchange_wallet_params import UpdateExchangeWalletParams


class TestUpdateExchangeWalletParams(unittest.TestCase):
    """UpdateExchangeWalletParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateExchangeWalletParams:
        """Test UpdateExchangeWalletParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateExchangeWalletParams`
        """
        model = UpdateExchangeWalletParams()
        if include_optional:
            return UpdateExchangeWalletParams(
                wallet_type = 'Custodial',
                name = 'Example Wallet'
            )
        else:
            return UpdateExchangeWalletParams(
                wallet_type = 'Custodial',
        )
        """

    def testUpdateExchangeWalletParams(self):
        """Test UpdateExchangeWalletParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
