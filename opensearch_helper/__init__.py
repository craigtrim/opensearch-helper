# LOGGING Statements must remain first
import logging
logging.getLogger('urllib3').setLevel(logging.ERROR)
logging.getLogger('opensearch').setLevel(logging.ERROR)
# END Logging Statements

from typing import Optional

from .bp import *
from .bp.opensearch_aws import OpenSearchAWS
from .bp.opensearch_dev import OpenSearchDEV
from .svc import *
from .svc.score_top_hit import ScoreTopHit
from .dmo import *
from .dto import *

from .dto.typedefs import ScoreResult
from .dto.typedefs import MultiMatchQuery


class SingletonApi(object):
    __api = None

    def api(self) -> OpenSearchAWS:
        if not self.__api:
            self.__api = OpenSearchAWS()
        return self.__api


sapi = SingletonApi()


def top_hit(d_hits: dict) -> Optional[dict]:
    if 'hits' in d_hits:
        if 'hits' in d_hits['hits']:
            if d_hits['hits']['hits'] and len(d_hits['hits']['hits']):
                return d_hits['hits']['hits'][0]


def score_top_hit(d_top: dict) -> ScoreResult:
    """ Quantify and Qualify the Score of the Top OpenSearch Result

    Args:
        d_hits (dict): a dictionary of results

    Returns:
        ScoreResult: a quantity (score) and qualification (type) of the top result
    """
    return ScoreTopHit().process(d_top)


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
                         *args) -> MultiMatchQuery:
    """ Generate a Multi Match Query

    The multi_match query builds on the match query to allow multi-field queries

    Reference:
        https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-match-query.html

    Args:
        input_text (str): the text to query on
        args: one-or-more fields to query on

    Returns:
        dict: the constructed query
    """

    fields = list(args)
    fields = [x for x in fields if x and len(x)]

    return {
        'size': 5,
        'query': {
            'multi_match': {
                'query': input_text,
                'fields': fields
            }
        }
    }
