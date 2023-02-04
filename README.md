# Open Search Helper (opensearch-helper)
A collection of methods for assisting with OpenSearch querying on AWS

## MultiMatch Query Generator

**Method Definition**
```python
multimatch_generator(input_text: str, size: int = 5, *args) -> MultiMatchQuery
```

**Invoke Function**

Pass in one-or-more field names after the query:
```python
from opensearch_helper import multimatch_generator

d_query = multimatch_generator("what is the average PH of rainwater?" "question", "context")
```

**Sample Output**
```json
{
   "size":5,
   "query":{
      "multi_match":{
         "query":"input_text",
         "fields":[
            "question"
         ]
      }
   }
}
```

## API Query (AWS)
**Method Definition**
```python
query(d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult
```

**Invoke Function**

The following environment variables must exist and be encrypted via `baseblock::Run-Encrypt`
1. OPENSEARCH_HOST
2. OPENSEARCH_REGION
3. OPENSEARCH_USERNAME
4. OPENSEARCH_PASSWORD

```python
from opensearch_helper import query

query(d_query, index_name='myindex')
```

## Local OpenSearch
From the terminal run
```shell
docker-compose up
```

The following environment variables must exist and be encrypted via `baseblock::Run-Encrypt`
1. OPENSEARCH_HOST
3. OPENSEARCH_USERNAME
4. OPENSEARCH_PASSWORD

Unless these have been modified, the default values can be found here
https://opensearch.org/docs/latest/opensearch/install/docker/

from a python script import
```python
from opensearch_helper import OpenSearchDEV
```

The following functions are available
```python
client = OpenSearchDEV()

client.create_index(...)
client.delete_index(...)
client.add(...)
client.query(...)
```
