# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint


from opensearch_helper.dmo import multi_phrase_prefix


def test_multi_phrase_prefix():

    d_query = multi_phrase_prefix(
        terms=[
            'COVID-19 pandemic',
            'Rapid technology development',
            'Evolving consumer demand'
        ],
        stem_terms=True)

    pprint(d_query)

    assert d_query == {
        "query": {
            "bool": {
                "must": [
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "max_expansions": 100,
                                "query": "covid-19 pandem"
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "max_expansions": 100,
                                "query": "rapid technology develop"
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "max_expansions": 100,
                                "query": "evolving consumer demand"
                            }
                        }
                    }
                ]
            }
        }
    }


def main():
    test_multi_phrase_prefix()


if __name__ == "__main__":
    main()
