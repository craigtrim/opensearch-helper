# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Score the top OpenSearch Result """


from typing import Dict
from typing import Optional

from baseblock import BaseObject


from opensearch_helper.dto import ScoreResult
from opensearch_helper.dto import find_score_type


class ScoreTopHit(BaseObject):
    """ Score the top OpenSearch Result """

    def __init__(self) -> None:
        """ Change Log

        Created:
            10-Oct-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)

    def _top_hit(self,
                 d_hits: dict) -> dict:
        if 'hits' in d_hits:
            if 'hits' in d_hits['hits']:
                return d_hits['hits']['hits'][0]

    def process(self,
                d_hits: dict) -> ScoreResult:

        d_top = self._top_hit(d_hits)

        if not d_top:

            return {
                'score': 0.0,
                'type': None
            }

        return {
            'score': d_top['score'],
            'type': find_score_type(d_top['_score']).name
        }
