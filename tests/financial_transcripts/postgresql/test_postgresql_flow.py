import pytest
import promptflow


def test_rag_postgres_flow_runs():
    """
    The goal of the test: flow runs without error
    Out of scope: accuracy/relevance of output
    """
    pf = promptflow.PFClient()

    output = pf.flows.test(
        "financial_transcripts/rag-cosmos-postgresql-pgvector/flow.dag.yaml",
        inputs={
            "chat_history": [],
            "query": "What is the growth rate of Azure ML revenue in FY23Q1?",
        },
    )
