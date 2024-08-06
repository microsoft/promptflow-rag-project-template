# PROMPT TEMPLATES FOR THE USER
gen_prompt = """
        You are given two chunks of text, a ticker e.g. MSFT, Quarter, Year, as input. You will generate 10 relevant questions and answers pairs based on the input.
        The question should be formed based on information in both the chunks of text.
        The answers should be available in the two chunks of text. Do not generate answers on your own.  If answer is not available in the text, just write N/A.
               
        An example output for this example is: 

        Question: For {ticker} FY{year} Q{quarter}, what is the <question goes here>?
        Answer: example answer paraphrased from the relevant information in the given text goes here 

        Based on ticker, quarter, year, the question can be phrased in different ways e.g. MSFT FY23 Q1, MSFT FY2023 1st quarter, e.t.c.
        In case the text question is not relevant, please skip the question and answer pair.
        input_text1: 
        {chunk_text1}
        input_text2:
        {chunk_text2}
        ticker: {ticker}
        quarter: {quarter}
        year: {year}
        """

gen_prompt2 = """<Try your custom prompt here>"""
eval_prompt = """ For the given set of questions and answers, determine if the answer is relevant to either of the contexts.
    Set of questions and answers: {question_answer_set}
    Context1: {chunk1}
    Context2: {chunk2}
    Evaluate the accuracy of the answers. Given a set of 10 questions and answers, the context sources Context1 and Context2,  determine if the model's question and answer is relevant to at least one of the contexts.
    Return only a single score of 0 or 1 indicating whether the model's question and answer is grounded in either of the contexts. Rewrite each of the questions and answers, and add a line for score you give. For example:
    Question: <question goes here>
    Answer: <answer goes here>
    Score: <score goes here>
    """ 
eval_prompt2 = """ For the given set of questions and answers, determine if the answer is relevant to either of the contexts.
    Set of questions and answers: {question_answer_set}
    Context1: {chunk1}
    Context2: {chunk2}
    Evaluate the accuracy of the answers. Given a set of 10 questions and answers, the context sources Context1 and Context2,  determine if the model's question and answer is relevant to at least one of the contexts.
    Return only a single score on a scale of 1 to 5 considering this rating strategy:
    5 - question is good, information from both chunks is necessary to answer it
    4 - question is OK, information from only one chunk is sufficient to answer it
    3 - question is grounded on information from the chunks, but it's not good question (e.g. not clear what is asked, or too simplistic)
    2 - question is good, but not based on information from the chunks
    1 - question is bad and not based on information from the chunks or relevant to the topic
     
    Rewrite each of the questions and answers, and add a line for score you give and description of why you gave that score. For example:
    Question: <question goes here>
    Answer: <answer goes here>
    Score: <score goes here>
    Description: <description goes here>

    """ 

eval_prompt3 = """<Try your custom prompt here>"""