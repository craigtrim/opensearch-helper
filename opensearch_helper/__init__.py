from operator import index
from .bp import *
from .bp.opensearch_api import OpenSearchAPI
from .svc import *
from .svc.score_top_hit import ScoreTopHit
from .dmo import *
from .dto import *

from .dto.typedefs import ScoreResult
from .dto.typedefs import MultiMatchQuery
from typing import List


class SingletonApi(object):
    __api = None

    def api(self) -> OpenSearchAPI:
        if not self.__api:
            self.__api = OpenSearchAPI()
        return self.__api


sapi = SingletonApi()


def score_top_hit(d_hits: dict) -> ScoreResult:
    """ Quantify and Qualify the Score of the Top OpenSearch Result

    Args:
        d_hits (dict): a dictionary of results

    Returns:
        ScoreResult: a quantity (score) and qualification (type) of the top result
    """
    return ScoreTopHit().process(d_hits)


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


def multimatch_generator(input_text: str,
                         size: int = 5,
                         *args) -> MultiMatchQuery:
    """ Generate a Multi Match Query

    The multi_match query builds on the match query to allow multi-field queries

    Reference:
        https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-match-query.html

    Args:
        input_text (str): the text to query on
        size (int, optional): the total results to return. Defaults to 5.
        args: one-or-more fields to query on

    Returns:
        dict: the constructed query
    """

    return {
        'size': size,
        'query': {
            'multi_match': {
                'query': input_text,
                'fields': args
            }
        }
    }
