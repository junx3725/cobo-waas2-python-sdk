# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimate_transfer_fee_params import EstimateTransferFeeParams


class TestEstimateTransferFeeParams(unittest.TestCase):
    """EstimateTransferFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimateTransferFeeParams:
        """Test EstimateTransferFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateTransferFeeParams`
        """
        model = EstimateTransferFeeParams()
        if include_optional:
            return EstimateTransferFeeParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                request_type = 'Transfer',
                source = None,
                token_id = 'ETH_USDT',
                destination = None,
                fee_type = 'EVM_EIP_1559'
            )
        else:
            return EstimateTransferFeeParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                request_type = 'Transfer',
                source = None,
                token_id = 'ETH_USDT',
                destination = None,
        )
        """

    def testEstimateTransferFeeParams(self):
        """Test EstimateTransferFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
