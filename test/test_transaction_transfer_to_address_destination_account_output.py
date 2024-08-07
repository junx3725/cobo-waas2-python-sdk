# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_transfer_to_address_destination_account_output import TransactionTransferToAddressDestinationAccountOutput


class TestTransactionTransferToAddressDestinationAccountOutput(unittest.TestCase):
    """TransactionTransferToAddressDestinationAccountOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionTransferToAddressDestinationAccountOutput:
        """Test TransactionTransferToAddressDestinationAccountOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionTransferToAddressDestinationAccountOutput`
        """
        model = TransactionTransferToAddressDestinationAccountOutput()
        if include_optional:
            return TransactionTransferToAddressDestinationAccountOutput(
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                memo = '82840924',
                amount = '1.5'
            )
        else:
            return TransactionTransferToAddressDestinationAccountOutput(
        )
        """

    def testTransactionTransferToAddressDestinationAccountOutput(self):
        """Test TransactionTransferToAddressDestinationAccountOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
