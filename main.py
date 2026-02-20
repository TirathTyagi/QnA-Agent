from dotenv import load_dotenv
load_dotenv()

from graph.graph import app
import os




if __name__ == "__main__":
    print("Welcome to the QnA Agent!")
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        print("Langchain Tracing is enabled. You can view the traces in the Langchain Studio.")
    if os.getenv("OPENAI_API_KEY") is not None:
        print("OpenAI API Key is set.")
    else:
        print("Warning: OpenAI API Key is not set. Please set it in the .env file to enable answer generation and evaluation.")
    answer = app.invoke({"question": input("Enter your question: ")})
    print("\nFinal Answer:")
    print(answer["generation"].content)

    