import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: Gemini API key not found!")
else:
    try:
        # Connect Gemini AI
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash-lite",
            google_api_key=api_key,
            temperature=0.7
        )

        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful Study Assistant. "
             "Explain topics in simple language for students."),
            ("human", "{question}")
        ])

        # Connect prompt with AI model
        chain = prompt | llm

        print("Welcome to AI Study Assistant!")
        print("Type exit to stop.")

        while True:
            question = input("\nAsk your question: ")

            if question.lower() == "exit":
                print("Thank you!")
                break

            if not question.strip():
                print("Please enter a question.")
                continue

            try:
                response = chain.invoke({"question": question})
                print("\nAI Answer:")
                print(response.content)

            except Exception as e:
                print("Error getting answer:", e)

    except Exception as e:
        print("Error connecting to Gemini:", e)