# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_approver import TransactionApprover


class TestTransactionApprover(unittest.TestCase):
    """TransactionApprover unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionApprover:
        """Test TransactionApprover
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionApprover`
        """
        model = TransactionApprover()
        if include_optional:
            return TransactionApprover(
                name = 'Approver #1',
                status = 'Pending'
            )
        else:
            return TransactionApprover(
        )
        """

    def testTransactionApprover(self):
        """Test TransactionApprover"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
