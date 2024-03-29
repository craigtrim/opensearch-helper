#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Connect to OpenSearch on AWS """


import boto3

from json import dumps
from typing import Dict
from typing import Optional

from opensearchpy import OpenSearch
from opensearchpy import RequestsHttpConnection
from opensearchpy import AWSV4SignerAuth

from baseblock import EnvIO
from baseblock import CryptoBase
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from opensearch_helper.dto import OpenSearchResult
from opensearch_helper.dto import MultiMatchQuery
from opensearch_helper.svc import QueryOpenSearch
from opensearch_helper.dto import CreateIndexResult
from opensearch_helper.dto import AddDocumentResult
from opensearch_helper.dto import AWSClientType


class OpenSearchAWS(BaseObject):
    """ Connect to OpenSearch on AWS """

    def __init__(self,
                 client_type: AWSClientType) -> None:
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

        Args:
            client_type (AWSClientType): the client type
        """
        BaseObject.__init__(self, __name__)
        self.client = self._get_client(client_type)
        self._query = QueryOpenSearch(self.client).query
        self._generate_event = ServiceEventGenerator().process

    @staticmethod
    def _get_client(client_type: AWSClientType):
        if AWSClientType.HTTP_AUTH == client_type:
            from opensearch_helper.dmo import AWSClientHttpAuth
            return AWSClientHttpAuth().client

        if AWSClientType.SERVERLESS == client_type:
            from opensearch_helper.dmo import AWSClientServerless
            return AWSClientServerless().client

        raise NotImplementedError(client_type)

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

    def add(self,
            index_name: str,
            document: Dict[str, str],
            document_id: int) -> AddDocumentResult:
        """ Add Document to OpenSearch

        Args:
            index_name (str): the index to update
            document (dict): the document to add
            document_id (int): the ID of the document being added

        Returns:
            AddDocumentResult: the add document result
        """
        return self.client.index(
            index=index_name,
            body=document,
            id=document_id,
            refresh=True
        )

    def create_index(self,
                     d_body: Dict[str, str],
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
        if not self.client.indices.exists(index_name):
            return self.client.indices.create(index_name, body=d_body)

    def delete_index(self,
                     index_name: str) -> None:
        """ Delete Index (if exists)

        Args:
            index_name (str): the index to delete
        """

        if self.client.indices.exists(index_name):
            self.client.indices.delete(index_name)

    def count(self,
              index_name: str) -> int:
        """ Count Document in the Index

        Args:
            index_name (str): the index to count in

        Returns:
            int: the total documents
        """
        self.client.indices.refresh(index_name)
        return self.client.count(index=index_name, body={})["count"]
