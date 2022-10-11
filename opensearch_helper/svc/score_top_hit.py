# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# type: ignore
""" Score the top OpenSearch Result """


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

    def process(self,
                d_top_hit: dict) -> ScoreResult:

        if not d_top_hit:

            return {
                'score': 0.0,
                'type': None
            }

        score = d_top_hit['_score']

        return {
            'score': score,
            'type': find_score_type(score).name
        }
