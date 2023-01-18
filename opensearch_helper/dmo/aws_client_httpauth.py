#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to OpenSearch on AWS """


import boto3

from opensearchpy import OpenSearch
from opensearchpy import RequestsHttpConnection
from opensearchpy import AWSV4SignerAuth

from baseblock import EnvIO
from baseblock import CryptoBase
from baseblock import BaseObject


class AWSClientHttpAuth(BaseObject):
    """ Connect to OpenSearch on AWS using HTTP Auth """

    def __init__(self) -> None:
        """ Change Log

        Created:
            5-May-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/opensearch-helper/issues/2
        Updated:
            18-Oct-2022
            craigtrim@gmail.com
            *   renamed from 'opensearch-api' in pursuit of
                https://github.com/craigtrim/opensearch-helper/issues/3
        Updated:
            8-Nov-2022
            craigtrim@gmail.com
            *   replicate opensearch-dev API
        Updated:
            17-Jan-2023
            craigtrim@gmail.com
            *   refactored out of 'opensearch-aws'
        """
        BaseObject.__init__(self, __name__)

        def host() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_HOST')))

        def region() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_REGION')))

        def username() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_USERNAME')))

        def password() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_PASSWORD')))

        credentials = boto3.Session().get_credentials()
        AWSV4SignerAuth(credentials=credentials, region=region())

        self.client = OpenSearch(
            hosts=[{'host': host(), 'port': 443}],
            http_auth=(username(), password()),
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection)
