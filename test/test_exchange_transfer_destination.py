# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.exchange_transfer_destination import ExchangeTransferDestination


class TestExchangeTransferDestination(unittest.TestCase):
    """ExchangeTransferDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeTransferDestination:
        """Test ExchangeTransferDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeTransferDestination`
        """
        model = ExchangeTransferDestination()
        if include_optional:
            return ExchangeTransferDestination(
                destination_type = 'Address',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                sub_wallet_id = 'Asset',
                amount = '1.5'
            )
        else:
            return ExchangeTransferDestination(
                destination_type = 'Address',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                sub_wallet_id = 'Asset',
                amount = '1.5',
        )
        """

    def testExchangeTransferDestination(self):
        """Test ExchangeTransferDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
