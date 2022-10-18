#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Query a Connected instance of OpenSearch """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from opensearchpy import OpenSearch

from opensearch_helper.dto import OpenSearchResult
from opensearch_helper.dto import MultiMatchQuery


class QueryOpenSearch(BaseObject):
    """ Query a Connected instance of OpenSearch """

    def __init__(self,
                 client: OpenSearch) -> None:
        """ Change Log

        Created:
            18-Oct-2022
            craigtrim@gmail.com
            *   refactored out of 'opensearch-api' in pursuit of
                https://github.com/craigtrim/opensearch-helper/issues/3
        """
        BaseObject.__init__(self, __name__)
        self._client = client
        self._generate_event = ServiceEventGenerator().process

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

        sw = Stopwatch()

        response = self._client.search(
            body=d_query,
            index=index_name
        )

        # COR-80; Generate an Event Record
        d_event = self._generate_event(
            service_name=self.component_name(),
            event_name='generate-about-marv',
            stopwatch=sw,
            data={
                'index_name': index_name,
                'response': response,
                'd_query': d_query,
            })

        # return response, d_event
        return {
            'response': response,
            'events': [d_event]
        }
