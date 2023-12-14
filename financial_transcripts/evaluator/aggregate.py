from typing import List
from promptflow import tool

from typing import List
from promptflow import tool
from promptflow import log_metric


# @tool
# def accuracy_aggregate(processed_results: List[int]):

#     num_exception = 0
#     num_correct = 0

#     for i in range(len(processed_results)):
#         if processed_results[i] == -1:
#             num_exception += 1
#         elif processed_results[i] == 1:
#             num_correct += 1

#     num_total = len(processed_results)
#     accuracy = round(1.0 * num_correct / num_total, 2)
#     error_rate = round(1.0 * num_exception / num_total, 2)

#     log_metric(key="accuracy", value=accuracy)
#     log_metric(key="error_rate", value=error_rate)

#     return {
#         "num_total": num_total,
#         "num_correct": num_correct,
#         "num_exception": num_exception,
#         "accuracy": accuracy,
#         "error_rate": error_rate
#     }


# if __name__ == "__main__":
#     numbers = [1, 1, 1, 1, 0, -1, -1]
#     accuracy = accuracy_aggregate(numbers)
#     print("The accuracy is", accuracy)

@tool
def aggregate(processed_results: List[str]):
    """
    This tool aggregates the processed result of all lines and log metric.

    :param processed_results: List of the output of line_process node.
    """

    # Add your aggregation logic here

    aggregated_results = {}

    # Log metric
    # from promptflow import log_metric
    # log_metric(key="<my-metric-name>", value=aggregated_results["<my-metric-name>"])
    results_num = len(processed_results)
    print(results_num)
    print(processed_results)
    aggregated_results['results_num']=results_num 
    # # Log metric for each variant
    # from promptflow import log_metric
    # log_metric(key="results_num", value=results_num)

    return aggregated_results
