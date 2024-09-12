# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_message_sign_eip712_destination import TransactionMessageSignEIP712Destination


class TestTransactionMessageSignEIP712Destination(unittest.TestCase):
    """TransactionMessageSignEIP712Destination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionMessageSignEIP712Destination:
        """Test TransactionMessageSignEIP712Destination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionMessageSignEIP712Destination`
        """
        model = TransactionMessageSignEIP712Destination()
        if include_optional:
            return TransactionMessageSignEIP712Destination(
                destination_type = 'Address',
                structured_data = {"types": {"EIP712Domain": [{"name": "name", "type": "string"}, {"name": "version", "type": "string"}, {"name": "chainId", "type": "uint256"}, {"name": "verifyingContract", "type": "address"}], "Person": [{"name": "name", "type": "string"}, {"name": "wallet", "type": "address"}], "Mail": [{"name": "from", "type": "Person"}, {"name": "to", "type": "Person"}, {"name": "contents", "type": "string"}]}, "primaryType": "Mail", "domain": {"name": "Ether Mail", "version": "1", "chainId": 1, "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"}, "message": {"from": {"name": "Cow", "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"}, "to": {"name": "Bob", "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"}, "contents": "Hello, Bob!"}}

            )
        else:
            return TransactionMessageSignEIP712Destination(
                destination_type = 'Address',
                structured_data = {"types": {"EIP712Domain": [{"name": "name", "type": "string"}, {"name": "version", "type": "string"}, {"name": "chainId", "type": "uint256"}, {"name": "verifyingContract", "type": "address"}], "Person": [{"name": "name", "type": "string"}, {"name": "wallet", "type": "address"}], "Mail": [{"name": "from", "type": "Person"}, {"name": "to", "type": "Person"}, {"name": "contents", "type": "string"}]}, "primaryType": "Mail", "domain": {"name": "Ether Mail", "version": "1", "chainId": 1, "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"}, "message": {"from": {"name": "Cow", "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"}, "to": {"name": "Bob", "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"}, "contents": "Hello, Bob!"}}
,
        )
        """

    def testTransactionMessageSignEIP712Destination(self):
        """Test TransactionMessageSignEIP712Destination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
