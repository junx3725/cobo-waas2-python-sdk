# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.base_estimate_staking_fee import BaseEstimateStakingFee


class TestBaseEstimateStakingFee(unittest.TestCase):
    """BaseEstimateStakingFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseEstimateStakingFee:
        """Test BaseEstimateStakingFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseEstimateStakingFee`
        """
        model = BaseEstimateStakingFee()
        if include_optional:
            return BaseEstimateStakingFee(
                activity_type = 'Stake'
            )
        else:
            return BaseEstimateStakingFee(
                activity_type = 'Stake',
        )
        """

    def testBaseEstimateStakingFee(self):
        """Test BaseEstimateStakingFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
