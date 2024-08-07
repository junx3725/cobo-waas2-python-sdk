# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_signature_result import TransactionSignatureResult


class TestTransactionSignatureResult(unittest.TestCase):
    """TransactionSignatureResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSignatureResult:
        """Test TransactionSignatureResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSignatureResult`
        """
        model = TransactionSignatureResult()
        if include_optional:
            return TransactionSignatureResult(
                result_type = 'Address',
                signature = '0x6a8d82c2b080c18e7c1d187a95b3d9b0b9b20454d5e1d784b8a4625d16772d3f'
            )
        else:
            return TransactionSignatureResult(
                signature = '0x6a8d82c2b080c18e7c1d187a95b3d9b0b9b20454d5e1d784b8a4625d16772d3f',
        )
        """

    def testTransactionSignatureResult(self):
        """Test TransactionSignatureResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
