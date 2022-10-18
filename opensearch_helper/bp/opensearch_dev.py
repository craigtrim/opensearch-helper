#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to a Local Dev Instance of OpenSearch (via docker-compose.yml) """


from typing import Optional

from opensearchpy import OpenSearch

from baseblock import EnvIO
from baseblock import CryptoBase
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from opensearch_helper.dto import OpenSearchResult
from opensearch_helper.dto import CreateIndexResult
from opensearch_helper.dto import MultiMatchQuery
from opensearch_helper.dto import AddDocumentResult
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

        self._client = client
        self._query = QueryOpenSearch(client).query

    def add(self,
            index_name: str,
            document: dict,
            document_id: int) -> AddDocumentResult:
        """ Add Document to OpenSearch

        Args:
            index_name (str): the index to update
            document (dict): the document to add
            document_id (int): the ID of the document being added

        Returns:
            AddDocumentResult: the add document result
        """
        return self._client.index(
            index=index_name,
            body=document,
            id=document_id,
            refresh=True
        )

    def create_index(self,
                     d_body: dict,
                     index_name: str) -> Optional[CreateIndexResult]:
        """ Create Index (if not exists)

        Args:
            d_body (dict): the mapping for documents within this index
            Sample Mapping:
                {
                    "mappings": {
                        "properties": {
                            "question": {
                                "type": "text", 
                                "analyzer": "english"
                            },
                            "context": {
                                "type": "text", 
                                "analyzer": "english"
                            },
                            "answer": {
                                "type": "text", 
                                "analyzer": "english"
                            },
                            "chapter": {
                                "type": "integer"
                            },
                            "page": {
                                "type": "integer"
                            },
                        }
                    }
                }
            index_name (str): the index to create

        Returns:
            CreateIndexResult: the result
        """
        if not self._client.indices.exists(index_name):
            return self._client.indices.create(index_name, body=d_body)

    def delete_index(self,
                     index_name: str) -> None:
        """ Delete Index (if exists)

        Args:
            index_name (str): the index to delete
        """

        if self._client.indices.exists(index_name):
            self._client.indices.delete(index_name)

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
