import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
import config
from search_tool import search_documents
from ticket_tool import raise_ticket

kernel = sk.Kernel()

chat_service = AzureChatCompletion(
    deployment_name=config.AZURE_OPENAI_DEPLOYMENT,
    endpoint=config.AZURE_OPENAI_ENDPOINT,
    api_key=config.AZURE_OPENAI_KEY
)

kernel.add_service(chat_service)


def run_agent():

    while True:

        query = input("\nAsk Question: ")

        if query == "exit":
            break

        context = search_documents(query)

        prompt = f"""
You are a helpful support assistant.

Context:
{context}

User Question:
{query}

Answer using the context.
"""

        response = kernel.invoke_prompt(prompt)

        print("\nAI Response:")
        print(response)

        escalate = input("\nDo you want to create a ticket? (yes/no): ")

        if escalate.lower() == "yes":
            raise_ticket()