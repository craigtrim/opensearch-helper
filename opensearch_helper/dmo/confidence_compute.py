#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Compute a Confidence Internval between 0 - 100 for each OpenSearch result """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from opensearchpy import OpenSearch

from opensearch_helper.dto import OpenSearchResult
from opensearch_helper.dto import MultiMatchQuery


class ConfidenceCompute(BaseObject):
    """ Compute a Confidence Internval between 0 - 100 for each OpenSearch result """

    def __init__(self) -> None:
        """ Change Log

        Created:
            4-Feb-2023
            craigtrim@gmail.com
            *   compute a confidence for each search result
                https://github.com/craigtrim/opensearch-helper/issues/5
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                response: dict) -> dict:
        """ Entry Point

        Args:
            response (dict): the OpenSearch response

        Returns:
            dict: the modified response
        """

        max_score = response['hits']['max_score']
        if not max_score or max_score is None:
            return response

        hits = response['hits']['hits']
        if not hits or not len(hits):
            return response

        for hit in response['hits']['hits']:
            hit['confidence'] = int(round(hit['_score'] / max_score, 2) * 100)

        return response
