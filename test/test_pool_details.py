# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.pool_details import PoolDetails


class TestPoolDetails(unittest.TestCase):
    """PoolDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolDetails:
        """Test PoolDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolDetails`
        """
        model = PoolDetails()
        if include_optional:
            return PoolDetails(
                id = 'babylon_btc',
                chain_id = 'Bitcoin',
                protocol = 'Babylon',
                protocol_icon_url = 'https://example.com/icon.png',
                supported_wallet_types = ["MPC"],
                supported_wallet_subtypes = ["Org-Controlled"],
                token_id = 'BTC',
                est_apr = 0.05,
                pool_type = 'Babylon',
                min_amount = '0.01',
                max_amount = '100.00',
                min_stake_period = 30,
                max_stake_period = 1000,
                min_stake_blocks = 100,
                max_stake_blocks = 1000,
                validators_info = [
                    null
                    ]
            )
        else:
            return PoolDetails(
                id = 'babylon_btc',
                chain_id = 'Bitcoin',
                protocol = 'Babylon',
                protocol_icon_url = 'https://example.com/icon.png',
                supported_wallet_types = ["MPC"],
                supported_wallet_subtypes = ["Org-Controlled"],
                token_id = 'BTC',
                est_apr = 0.05,
                validators_info = [
                    null
                    ],
        )
        """

    def testPoolDetails(self):
        """Test PoolDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
