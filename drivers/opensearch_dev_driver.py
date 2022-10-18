from opensearch_helper import OpenSearchDEV
from opensearch_helper import multimatch_generator

# must have 'docker-compose up' running


def crud():

    bp = OpenSearchDEV()
    assert bp

    d_body = {
        "mappings": {
            "properties": {
                "question": {"type": "text", "analyzer": "english"},
                "context": {"type": "text", "analyzer": "english"},
                "answer": {"type": "text", "analyzer": "english"},
                "chapter": {"type": "integer"},
                "page": {"type": "integer"},
            }
        }
    }

    index_name = 'test-crud'

    bp.delete_index(index_name)
    assert bp.create_index(d_body=d_body, index_name=index_name)

    doc = {
        "question": "My Question",
        "context": "My Context",
        "answer": ["My Answer"],
        "chapter": 1,
        "page": 1,
    }

    assert bp.add(
        index_name=index_name,
        document=doc,
        document_id=3)

    d_query = multimatch_generator('my question', 'question')

    results = bp.query(
        d_query=d_query,
        index_name=index_name)

    assert results

    print(results)


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(crud)

    wrapper.deconstruct_env()


if __name__ == "__main__":
    main()
