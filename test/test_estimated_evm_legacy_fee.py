# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimated_evm_legacy_fee import EstimatedEvmLegacyFee


class TestEstimatedEvmLegacyFee(unittest.TestCase):
    """EstimatedEvmLegacyFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedEvmLegacyFee:
        """Test EstimatedEvmLegacyFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimatedEvmLegacyFee`
        """
        model = EstimatedEvmLegacyFee()
        if include_optional:
            return EstimatedEvmLegacyFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                slow = None,
                recommended = None,
                fast = None
            )
        else:
            return EstimatedEvmLegacyFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                recommended = None,
        )
        """

    def testEstimatedEvmLegacyFee(self):
        """Test EstimatedEvmLegacyFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
