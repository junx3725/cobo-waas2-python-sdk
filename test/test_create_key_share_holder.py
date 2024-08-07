# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_key_share_holder import CreateKeyShareHolder


class TestCreateKeyShareHolder(unittest.TestCase):
    """CreateKeyShareHolder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateKeyShareHolder:
        """Test CreateKeyShareHolder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateKeyShareHolder`
        """
        model = CreateKeyShareHolder()
        if include_optional:
            return CreateKeyShareHolder(
                name = 'Key share holder name',
                type = 'API',
                tss_node_id = 'coboAbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghi',
                signer = True
            )
        else:
            return CreateKeyShareHolder(
        )
        """

    def testCreateKeyShareHolder(self):
        """Test CreateKeyShareHolder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
