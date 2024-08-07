# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.base_contract_call_source import BaseContractCallSource


class TestBaseContractCallSource(unittest.TestCase):
    """BaseContractCallSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseContractCallSource:
        """Test BaseContractCallSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseContractCallSource`
        """
        model = BaseContractCallSource()
        if include_optional:
            return BaseContractCallSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
            )
        else:
            return BaseContractCallSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
        )
        """

    def testBaseContractCallSource(self):
        """Test BaseContractCallSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
