#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to OpenSearch on AWS """


import boto3
from requests_aws4auth import AWS4Auth

from opensearchpy import OpenSearch
from opensearchpy import RequestsHttpConnection

from baseblock import EnvIO
from baseblock import CryptoBase
from baseblock import BaseObject


class AWSClientServerless(BaseObject):
    """ Connect to OpenSearch on AWS using HTTP Auth """

    def __init__(self) -> None:
        """ Change Log

        Created:
            17-Jan-2023
            craigtrim@gmail.com
            *   refactored out of 'opensearch-aws'
        """
        BaseObject.__init__(self, __name__)

        def aws_profile() -> str:
            return EnvIO.str_or_exception('AWS_PROFILE_NAME')

        def host() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_HOST')))

        def region() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_REGION')))

        service = 'aoss'
        credentials = boto3.Session(
            profile_name=aws_profile()).get_credentials()

        awsauth = AWS4Auth(credentials.access_key,
                           credentials.secret_key,
                           region(), service,
                           session_token=credentials.token)

        self.client = OpenSearch(
            hosts=[{'host': host(), 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection)
