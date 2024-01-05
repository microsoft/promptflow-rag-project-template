from typing import List
from promptflow import tool


@tool
def aggregate(llm_similarity_scores: List[float], llm_groundedness_score: List[float]):
    """
    This tool aggregates the processed result of all lines to the variant level and log metric for each variant.

    :param processed_results: List of the output of line_process node.
    :param variant_ids: List of variant ids that can be used to group the results by variant.
    :param line_numbers: List of line numbers of the variants. If provided, this can be used to
                        group the results by line number.
    """

    aggregated_results = {"llm_similarity": 0.0,
                          "llm_groundedness": 0.0,
                        "count": 0}

    # Calculate average groundedness score for each variant
    for i in range(len(llm_similarity_scores)):
        aggregated_results["llm_similarity"] += llm_similarity_scores[i]
        aggregated_results["llm_groundedness"] +=llm_groundedness_score[i]
        aggregated_results["count"] += 1

    aggregated_results["llm_similarity"] /= aggregated_results["count"]
    aggregated_results["llm_groundedness"] /=aggregated_results["count"]

    # Log metric for each variant
    from promptflow import log_metric

    log_metric(key="llm_similarity", value=aggregated_results["llm_similarity"])
    log_metric(key="llm_groundedness", value=aggregated_results["llm_groundedness"])

    return aggregated_results
