# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.contract_call_destination import ContractCallDestination


class TestContractCallDestination(unittest.TestCase):
    """ContractCallDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractCallDestination:
        """Test ContractCallDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractCallDestination`
        """
        model = ContractCallDestination()
        if include_optional:
            return ContractCallDestination(
                destination_type = 'EVM_Contract',
                address = '0x0406db8351aa6839169bb363f63c2c808fee8f99',
                value = '1.5',
                calldata = '[B@6f7b8ae1'
            )
        else:
            return ContractCallDestination(
                destination_type = 'EVM_Contract',
                address = '0x0406db8351aa6839169bb363f63c2c808fee8f99',
                calldata = '[B@6f7b8ae1',
        )
        """

    def testContractCallDestination(self):
        """Test ContractCallDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
