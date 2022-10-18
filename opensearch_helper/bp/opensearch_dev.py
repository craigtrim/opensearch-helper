#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to a Local Dev Instance of OpenSearch (via docker-compose.yml) """


import boto3

from typing import Any
from typing import Dict

from opensearchpy import OpenSearch
from opensearchpy import RequestsHttpConnection
from opensearchpy import AWSV4SignerAuth

from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import CryptoBase
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from opensearch_helper.dto import OpenSearchResult
from opensearch_helper.dto import MultiMatchQuery
from opensearch_helper.svc import QueryOpenSearch


class OpenSearchDEV(BaseObject):
    """ Connect to a Local Dev Instance of OpenSearch (via docker-compose.yml) """

    def __init__(self) -> None:
        """ Change Log

        Created:
            18-Oct-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/opensearch-helper/issues/3
        """
        BaseObject.__init__(self, __name__)
        self._generate_event = ServiceEventGenerator().process

        def host() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_HOST')))

        def username() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_USERNAME')))

        def password() -> str:
            return str(CryptoBase().decrypt_str(
                EnvIO.str_or_exception('OPENSEARCH_PASSWORD')))

        client = OpenSearch(
            hosts=[{'host': host(), 'port': 9200}],
            http_auth=(username(), password()))

        self._query = QueryOpenSearch(client).query

    def query(self,
              d_query: MultiMatchQuery,
              index_name: str) -> OpenSearchResult:
        """ Entry Point to Query Open Search

        Args:
            d_query (MultiMatchQuery): a valid OpenSearch document query
            index_name (str): the index to query

        Returns:
            OpenSearchResult: the result
        """

        return self._query(d_query=d_query,
                           index_name=index_name)
