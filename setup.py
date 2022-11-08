# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opensearch_helper',
 'opensearch_helper.bp',
 'opensearch_helper.dmo',
 'opensearch_helper.dto',
 'opensearch_helper.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'boto3', 'opensearch-py>=1.1.0,<2.0.0', 'requests']

setup_kwargs = {
    'name': 'opensearch-helper',
    'version': '0.1.13',
    'description': 'OpenSearch Helper for Easy I/O',
    'long_description': '# Open Search Helper (opensearch-helper)\nA collection of methods for assisting with OpenSearch querying on AWS\n\n## MultiMatch Query Generator\n\n**Method Definition**\n```python\nmultimatch_generator(input_text: str, size: int = 5, *args) -> MultiMatchQuery\n```\n\n**Invoke Function**\n\nPass in one-or-more field names after the query:\n```python\nfrom opensearch_helper import multimatch_generator\n\nd_query = multimatch_generator("what is the average PH of rainwater?" "question", "context")\n```\n\n**Sample Output**\n```json\n{\n   "size":5,\n   "query":{\n      "multi_match":{\n         "query":"input_text",\n         "fields":[\n            "question"\n         ]\n      }\n   }\n}\n```\n\n## API Query (AWS)\n**Method Definition**\n```python\nquery(d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult\n```\n\n**Invoke Function**\n\nThe following environment variables must exist and be encrypted via `baseblock::Run-Encrypt`\n1. OPENSEARCH_HOST\n2. OPENSEARCH_REGION\n3. OPENSEARCH_USERNAME\n4. OPENSEARCH_PASSWORD\n\n```python\nfrom opensearch_helper import query\n\nquery(d_query, index_name=\'myindex\')\n```\n\n## Score Top Hit\nThis method will retrieve the top hit and both quantitatively and qualitatively score the result.\n\n**Method Definition**\n```python\nscore_top_hit(d_hits: dict) -> ScoreResult\n```\n\n**Invoke Function**\n```python\nfrom opensearch_helper import score_top_hit\n\nscore_top_hit(d_hits)\n```\n\n**Sample Output**\n```json\n{\n   "score":14.23432,\n   "type":"HIGH"\n}\n```\n\n## Local OpenSearch\nFrom the terminal run\n```shell\ndocker-compose up\n```\n\nThe following environment variables must exist and be encrypted via `baseblock::Run-Encrypt`\n1. OPENSEARCH_HOST\n3. OPENSEARCH_USERNAME\n4. OPENSEARCH_PASSWORD\n\nUnless these have been modified, the default values can be found here\nhttps://opensearch.org/docs/latest/opensearch/install/docker/\n\nfrom a python script import\n```python\nfrom opensearch_helper import OpenSearchDEV\n```\n\nThe following functions are available\n```python\nclient = OpenSearchDEV()\n\nclient.create_index(...)\nclient.delete_index(...)\nclient.add(...)\nclient.query(...)\n```',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/opensearch-helper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
