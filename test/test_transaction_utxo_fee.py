# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_utxo_fee import TransactionUtxoFee


class TestTransactionUtxoFee(unittest.TestCase):
    """TransactionUtxoFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionUtxoFee:
        """Test TransactionUtxoFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionUtxoFee`
        """
        model = TransactionUtxoFee()
        if include_optional:
            return TransactionUtxoFee(
                fee_rate = '50',
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                fee_used = '0.1',
                max_fee_amount = '0.1'
            )
        else:
            return TransactionUtxoFee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionUtxoFee(self):
        """Test TransactionUtxoFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
