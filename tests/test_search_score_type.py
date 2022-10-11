# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from opensearch_helper.svc import ScoreTopHit


def test_service():

    svc = ScoreTopHit()
    assert svc
