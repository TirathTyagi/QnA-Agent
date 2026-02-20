from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(model="gpt-5-mini", temperature=0.0)

generator_prompt = ChatPromptTemplate.from_messages(
    [
        ("system"
         ,"You are a professional assistant that generates answers to user asked questions"
          "Use the documents retrieved from web search results to generate answer to the question"
          "Make sure that the answer is provided in an appropriate format and is supported by the provided documents"
          "You may also receive a feedback on your previously generated answer, use that feedback to improve the quality of your answer"
          "Do not provide further recommendations to ask more questions to user, just generate the best possible answer based on the provided information"
         ),
         ("human", "User Question: {question} \n\n Web Search Results: {documents} \n\n Feedback: {feedback} \n\n Previously Generated Answer: {generation}")
    ]
)

answer_chain = generator_prompt | llm