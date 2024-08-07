# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.retry_webhook_event_by_id201_response import RetryWebhookEventById201Response


class TestRetryWebhookEventById201Response(unittest.TestCase):
    """RetryWebhookEventById201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetryWebhookEventById201Response:
        """Test RetryWebhookEventById201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetryWebhookEventById201Response`
        """
        model = RetryWebhookEventById201Response()
        if include_optional:
            return RetryWebhookEventById201Response(
                retried = True
            )
        else:
            return RetryWebhookEventById201Response(
        )
        """

    def testRetryWebhookEventById201Response(self):
        """Test RetryWebhookEventById201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
