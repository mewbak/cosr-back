import pytest


@pytest.mark.elasticsearch
def test_simple_insert_and_search(indexer, searcher):

    res = indexer.client.index_corpus([{
        "content": """<html><title>hello world</title><body>hello body</body></html>""",
        "url": "http://example.com"
    }, {
        "content": """<html><title>another world</title><body>document body</body></html>""",
        "url": "http://example2.com/page2"
    }])

    indexed = res[0]
    indexed2 = res[1]

    indexer.client.flush()
    indexer.client.refresh()

    assert indexed["docid"]
    assert indexed["url"].url == "http://example.com"
    assert indexed["rank"] > 0

    assert indexed2["docid"] != indexed["docid"]

    search_results = searcher.client.search("hello")
    assert len(search_results["hits"]) == 1
    assert search_results["hits"][0]["docid"] == indexed["docid"]
    assert search_results["hits"][0]["score"] > 0

    search_results = searcher.client.search("world")
    assert len(search_results["hits"]) == 2

    search_results = searcher.client.search("world", domain="example2.com")
    assert len(search_results["hits"]) == 1
    assert search_results["hits"][0]["docid"] == indexed2["docid"]
