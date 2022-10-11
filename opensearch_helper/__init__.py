from operator import index
from .bp import *
from .bp.opensearch_api import OpenSearchAPI
from .svc import *
from .dmo import *
from .dto import *

from .dto.typedefs import MultiMatchQuery
from typing import List


class SingletonApi(object):
    __api = None

    def api(self) -> OpenSearchAPI:
        if not self.__api:
            self.__api = OpenSearchAPI()
        return self.__api


sapi = SingletonApi()


def query(d_query: MultiMatchQuery,
          index_name: str) -> OpenSearchResult:
    """ Query Open Search

    Args:
        d_query (MultiMatchQuery): a MultiMatch query
        index_name (str): an index to query

    Returns:
        OpenSearchResult: the OpenSearch query result
    """

    return sapi.api().query(
        d_query=d_query,
        index_name=index_name)


def generate_multi_match_query(input_text: str,
                               fields: List[str],
                               size: int = 5) -> MultiMatchQuery:
    """ Generate a Multi Match Query

    The multi_match query builds on the match query to allow multi-field queries

    Reference:
        https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-match-query.html

    Args:
        input_text (str): the text to query on
        fields (List[str]): one-or-more fields to query on
        size (int, optional): the total results to return. Defaults to 5.

    Returns:
        dict: the constructed query
    """

    return {
        'size': size,
        'query': {
            'multi_match': {
                'query': input_text,
                'fields': fields
            }
        }
    }
