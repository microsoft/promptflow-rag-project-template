from typing import List
from promptflow import tool


@tool
def aggregate(relevance_scores: List[float], coherence_scores: list[float], fluency_scores: list[float], groundedness_scores: list[float], gpt_similarity_scores: List[float]):
    """
    This tool aggregates the processed result of all lines to the variant level and log metric for each variant.

    :param processed_results: List of the output of line_process node.
    :param variant_ids: List of variant ids that can be used to group the results by variant.
    :param line_numbers: List of line numbers of the variants. If provided, this can be used to
                        group the results by line number.
    """

    aggregated_results = {"relevance": 0.0,
                          "coherence": 0.0,
                          "fluency": 0.0,
                          "groundedness": 0.0, 
                          "gpt_similarity": 0.0,
                          "count": 0}

    # Calculate average groundedness score for each variant
    for i in range(len(gpt_similarity_scores)):
        aggregated_results["relevance"] += relevance_scores[i]
        aggregated_results["coherence"] += coherence_scores[i]
        aggregated_results["fluency"] += fluency_scores[i]
        aggregated_results["groundedness"] += groundedness_scores[i]
        aggregated_results["gpt_similarity"] += gpt_similarity_scores[i] 
        aggregated_results["count"] += 1

    aggregated_results["relevance"] /= aggregated_results["count"]
    aggregated_results["coherence"]  /=aggregated_results["count"]
    aggregated_results["fluency"]  /= aggregated_results["count"]
    aggregated_results["groundedness"] /= aggregated_results["count"]
    aggregated_results["gpt_similarity"] /= aggregated_results["count"]
    # Log metric for each variant
    from promptflow import log_metric

    log_metric(key="relevance", value=aggregated_results["relevance"])
    log_metric(key="coherence", value=aggregated_results["coherence"])
    log_metric(key="fluency", value=aggregated_results["fluency"])
    log_metric(key="groundedness", value=aggregated_results["groundedness"])
    log_metric(key="gpt_similarity", value=aggregated_results["gpt_similarity"])
    return aggregated_results
