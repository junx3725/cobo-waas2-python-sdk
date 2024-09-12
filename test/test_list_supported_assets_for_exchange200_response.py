# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_supported_assets_for_exchange200_response import ListSupportedAssetsForExchange200Response


class TestListSupportedAssetsForExchange200Response(unittest.TestCase):
    """ListSupportedAssetsForExchange200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSupportedAssetsForExchange200Response:
        """Test ListSupportedAssetsForExchange200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSupportedAssetsForExchange200Response`
        """
        model = ListSupportedAssetsForExchange200Response()
        if include_optional:
            return ListSupportedAssetsForExchange200Response(
                data = [
                    cobo_waas2.models.asset_info.AssetInfo(
                        asset_id = 'USDT', 
                        display_code = 'USDT', 
                        description = 'Tether USDT', 
                        icon_url = 'https://d.cobo.com/public/logos/USDT.png', )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListSupportedAssetsForExchange200Response(
        )
        """

    def testListSupportedAssetsForExchange200Response(self):
        """Test ListSupportedAssetsForExchange200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
