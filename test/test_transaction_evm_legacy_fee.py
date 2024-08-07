# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_evm_legacy_fee import TransactionEvmLegacyFee


class TestTransactionEvmLegacyFee(unittest.TestCase):
    """TransactionEvmLegacyFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionEvmLegacyFee:
        """Test TransactionEvmLegacyFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionEvmLegacyFee`
        """
        model = TransactionEvmLegacyFee()
        if include_optional:
            return TransactionEvmLegacyFee(
                gas_price = '100000000',
                gas_limit = '21000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                fee_used = '0.1',
                gas_used = '100000000'
            )
        else:
            return TransactionEvmLegacyFee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionEvmLegacyFee(self):
        """Test TransactionEvmLegacyFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
