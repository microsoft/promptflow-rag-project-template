import pytest

def test_rag_postgres_flow_runs():
    '''
    The goal of the test: flow runs without error
    Out of scope: accuracy/relevance of output 
    '''
    import promptflow
    pf = promptflow.PFClient()

    output = pf.flows.test(
    "../../rag-cosmos-postgres/flow.dag.yaml",
        inputs={
            "chat_history": [],
            "query": "What is the growth rate of Azure ML revenue in FY23Q1?",
        },
    )
