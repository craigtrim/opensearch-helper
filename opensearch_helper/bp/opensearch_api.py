#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Invoke the Greetings Classifier Model """


import boto3

from opensearchpy import OpenSearch
from opensearchpy import RequestsHttpConnection
from opensearchpy import AWSV4SignerAuth

from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import CryptoBase
from baseblock import BaseObject
from baseblock import ServiceEventGenerator


class OpenSearchAPI(BaseObject):
    """ Invoke the Greetings Classifier Model """

    def __init__(self):
        """ Change Log

        Created:
            5-May-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/opensearch-helper/issues/2
        """
        BaseObject.__init__(self, __name__)
        self._generate_event = ServiceEventGenerator().process

        def host() -> str:
            return CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_HOST'))

        def region() -> str:
            return CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_REGION'))

        def username() -> str:
            return CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_USERNAME'))

        def password() -> str:
            return CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_PASSWORD'))

        credentials = boto3.Session().get_credentials()
        AWSV4SignerAuth(credentials, region())

        self._client = OpenSearch(
            hosts=[{'host': host(), 'port': 443}],
            http_auth=(username(), password()),
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection)

    def query(self,
              d_query: dict,
              index_name: str) -> tuple:

        sw = Stopwatch()

        response = self._client.search(
            body=d_query,
            index=index_name
        )

        # GRAFFL-278; Generate an Event Record
        d_event = self._generate_event(
            service_name=self.component_name(),
            event_name='generate-about-marv',
            stopwatch=sw,
            data={
                'index_name': index_name,
                'response': response,
                'd_query': d_query,
            })

        return response, d_event
