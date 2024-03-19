Crating a vector database is a four step process outlined below: 

1. `step1_chunk_and_extract.ipynb` chunks and extracts PDF files using Azure Form Recognizer and save to .csv files.
2. `step2_embed.ipynb` reads and embeds using Azure OpenAI and saves to .csv files. 
	- Make sure to modify this line for your `.env` file path for Azure OpenAI: `env_name = "../../llm.env"`
3. `step3_db_storing_vectorsearch.ipynb` reads and inserts data into ACS and shows examples of various search capabilities using ACS hybrid search from data.