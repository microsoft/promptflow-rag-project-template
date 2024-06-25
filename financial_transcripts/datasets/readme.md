# About data

We have three QA benchmarking datasets:
* evalset.csv - 10 human-curated pairs of questions and answers, used by default as a simple example in this sample
* evalset_with_history.csv - 3 human-curated pairs of questions and answers, extended with chat history, for testing follow-up questions and QueryRewriter node
* evalset_with_history.csv - 66 AI-generated questions that received approval from a human SME, suitable for experimentation of larger scale to get more reliable evaluations of RAG performance

The datasets can be used either separately or in combinations, e.g. merging evalset.csv  with evalset_with_history.csv results in a set with extended coverage but is still small enough for quick experimentation. 