#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" OpenSearch Query DSL Generator """


from math import pow

from typing import List

from nltk.stem import PorterStemmer


class Stemmer(object):

    def __init__(self):
        self._ps = PorterStemmer()

    def process(self,
                input_text: str,
                unigrams: bool = False) -> str:

        if not unigrams and ' ' not in input_text.strip():
            return input_text

        result = self._ps.stem(input_text)
        if result.endswith('i'):
            result = result[:-1].strip()

        return result


def exact_match_by_field_name(field_name: str,
                              field_value: str) -> dict:
    return {
        "query": {
            "term": {
                field_name: field_value
            }
        }
    }


def progressive_bigram_query(input_text: str,
                             stem_terms: bool = True,
                             analyzer: str = "standard",
                             max_expansions: int = 100) -> dict:
    """ Match a User Description of a Concept

    Implementation:
        This query works best when the user is describing a single concept

    Sample:
        a user query of ("cloud-based core banking platforms") would result in
        {
            "query":{
                "bool":{
                    "should":[
                        [
                            {
                                "match_phrase_prefix":{
                                    "text":{
                                        "analyzer":"standard",
                                        "boost":1.0,
                                        "max_expansions":100,
                                        "query":"banking platforms"
                                    }
                                }
                            },
                            {
                                "match_phrase_prefix":{
                                    "text":{
                                        "analyzer":"standard",
                                        "boost":2.0,
                                        "max_expansions":100,
                                        "query":"core banking platforms"
                                    }
                                }
                            },
                            {
                                "match_phrase_prefix":{
                                    "text":{
                                        "analyzer":"standard",
                                        "boost":4.0,
                                        "max_expansions":100,
                                        "query":"cloud-based core banking platforms"
                                    }
                                }
                            }
                        ]
                    ]
                }
            }
        }

        Notice how the exact match has the highest boost, while the less descriptive the query becomes
        the less boosted the results are.  This maintains a high balance of precision and recall.

    Reference:
        https://github.com/craigtrim/slidefinder-mdl-builder/issues/17#issuecomment-1454278453

    Args:
        input_text (str): the user query
        stem_terms (bool, optional): perform term stemming. Defaults to False.
            if enabled, will only stem bigrams and higher
        analyzer (str, optional): the query analyzer to use. Defaults to "standard".
        max_expansions (int, optional): the max expansions in fuzzy searching. Defaults to 100.
            https://stackoverflow.com/questions/50033895/elasticsearch-fuzzy-query-max-expansions#50041650

    Returns:
        dict: _description_
    """

    def get_tokens() -> List[str]:
        if input_text.count(' ') == 1:
            return [input_text]

        i = 2
        terms = []

        tokens = input_text.split()
        while i <= len(tokens):
            terms.append(' '.join(tokens[-i:]).strip())
            i += 1

        return terms

    def must_queries(tokens: List[str]) -> List[dict]:
        queries = []

        for i in range(len(tokens)):
            queries.append({
                "match_phrase_prefix": {
                    "text": {
                        "query": tokens[i],
                        "analyzer": analyzer,
                        "max_expansions": max_expansions,
                        "boost": pow(2, i)
                    }
                }
            })

        return queries

    terms = get_tokens()
    if stem_terms:
        stem = Stemmer().process
        terms = [stem(x) for x in terms]

    return {
        "query": {
            "bool": {
                "should": must_queries(terms)
            }
        }
    }


def multi_phrase_prefix(terms: List[str],
                        stem_terms: bool = False,
                        analyzer: str = "standard",
                        max_expansions: int = 100) -> dict:
    """ Match Multiple Phrases (with optional Stemming)

    Sample:
        a user query of ("netflix" AND "video games") would result in
        {
            "query": {
                "bool": {
                    "must": [
                        {   "match_phrase_prefix": {
                                "text": {
                                    "query": "netflix",
                                    "analyzer" : "standard",
                                    "max_expansions" : 100
                                }
                        }},
                        {   "match_phrase_prefix": {
                                "text": {
                                    "query": "video gam",
                                    "analyzer" : "standard",
                                    "max_expansions" : 100
                                }
                        }}
                    ]
                }
            }
        }

    Reference:
        https://github.com/craigtrim/slidefinder-mdl-builder/issues/17#issuecomment-1454253026

    Args:
        terms (List[str]): a list of terms
            each term can be of any length or n-gram level, but should express a single concept only
        stem_terms (bool, optional): perform term stemming. Defaults to False.
            if enabled, will only stem bigrams and higher
        analyzer (str, optional): the query analyzer to use. Defaults to "standard".
        max_expansions (int, optional): the max expansions in fuzzy searching. Defaults to 100.
            https://stackoverflow.com/questions/50033895/elasticsearch-fuzzy-query-max-expansions#50041650

    Returns:
        dict: the OpenSearch query
    """

    if stem_terms:
        stem = Stemmer().process
        terms = [stem(x) for x in terms]

    def must_bool_queries() -> List[dict]:
        queries = []

        for term in terms:
            queries.append({
                "match_phrase_prefix": {
                    "text": {
                        "query": term,
                        "analyzer": analyzer,
                        "max_expansions": max_expansions
                    }
                }
            })

        return queries

    return {
        "query": {
            "bool": {
                "must": must_bool_queries()
            }
        }
    }
