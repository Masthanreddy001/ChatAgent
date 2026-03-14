from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import config

search_client = SearchClient(
    endpoint=config.AZURE_SEARCH_ENDPOINT,
    index_name=config.AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(config.AZURE_SEARCH_KEY)
)

def search_documents(query):
    results = search_client.search(query)

    context = ""
    for result in results:
        context += result["content"] + "\n"

    return context