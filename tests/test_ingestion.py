from ingest import ingest_pdf


def test_ingestion():

    chunk_count = ingest_pdf(
        "tests/testSample/research1.pdf"
    )

    assert chunk_count > 0
    