# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.address_transfer_destination import AddressTransferDestination


class TestAddressTransferDestination(unittest.TestCase):
    """AddressTransferDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressTransferDestination:
        """Test AddressTransferDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTransferDestination`
        """
        model = AddressTransferDestination()
        if include_optional:
            return AddressTransferDestination(
                destination_type = 'Address',
                account_output = cobo_waas2.models.address_transfer_destination_account_output.AddressTransferDestination_account_output(
                    address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku', 
                    memo = '82840924', 
                    amount = '1.5', ),
                utxo_outputs = [
                    cobo_waas2.models.address_transfer_destination_utxo_outputs_inner.AddressTransferDestination_utxo_outputs_inner(
                        address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sDEMO', 
                        amount = '1.5', 
                        script = '76a914fb37342f6275b13936799def06f2DEMO', )
                    ],
                change_address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sDEMO',
                force_internal = False,
                force_external = False
            )
        else:
            return AddressTransferDestination(
                destination_type = 'Address',
        )
        """

    def testAddressTransferDestination(self):
        """Test AddressTransferDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
