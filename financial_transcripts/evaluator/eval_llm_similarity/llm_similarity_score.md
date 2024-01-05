user:
# Instructions

* There are many chatbots that can answer users questions. They try to understand users's question and answer questions based on the understanding of the question and the context.
* Your goal is to score the accuracy of the question answering model's predictions. Given a question, the ground truth answer (Answer), and the llm model's prediction (Reply), determine if the model's prediction matches the true answer. Return only a score between 0 and 1 to evaluate the accuracy of the model's prediction with respect to ground truth.
    * Score 0 if LLM Reply is semantically different than Answer
    * Score 1 if LLM Reply semantically matches the Answer
    * If there're multiple facts in the Answer and some of them are present in the given Reply while some of them not, score between 0 to 1 based on fraction of information supported by Answer
* Just respond with the score, nothing else.
  
# Real work

## Question
{{question}}

## Answer
{{answer}}

## Reply
{{reply}}

## Score