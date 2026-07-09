from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import types
#from tools import document_understanding
from tools import file_access
from retrieval import index_document
from retrieval import retrieve
from dotenv import load_dotenv
import os


client = genai.Client(api_key=os.getenv("API"))
flag = True

chat = client.chats.create(model="gemini-2.5-flash")

### Tools Description

tools = types.Tool(
    function_declarations=[
        #document_understanding.doc_tool,
        index_document.index_document_tool, #for indexing used in chunks creation
        retrieve.retrieve_document_tool, #for retrieval of a query
        file_access.file_read, 
        file_access.file_append, 
        file_access.file_write,
        file_access.files_list,
        file_access.file_delete,
        ],
    # google_search=types.GoogleSearch(),
    # file_search=types.fileSearch,
    # code_execution=types.CodeExecutionResult
    
    )

config = types.GenerateContentConfig(tools=[tools])


tool_registry = {

    #"markdown" : document_understanding.doc_reader,
    "index_document": index_document.index_document,
    "retrieve_document":retrieve.retrieve_document,
    "list_files" : file_access.list_files,
    "read_file" : file_access.read_file,
    "write_file" : file_access.write_file,
    "append_file" : file_access.append_file,
    "dlt_file" : file_access.dlt_file
}

while True:
    
    prompt = input("\nUser: ")

    if(prompt == "/quit"):
        break
    
    else:
        print("Gemini: ", end="")
        response = chat.send_message_stream(prompt, config=config)
        
        for chunk in response: 
            if(chunk.function_calls):
                fc = chunk.function_calls[0]
                
                try:
                    tool_result = tool_registry[fc.name](**fc.args)

                except Exception as e:
                    tool_result = f"Tool Error: {str(e)}"
                print(tool_result)
                second_msg = chat.send_message(
                        f"""
                User Question:
                {prompt}

                Retrieved Context:
                {tool_result}

                Using ONLY the retrieved context, answer the user's question naturally.
                """
                )
                print(second_msg.text)
            elif(chunk.text):
                print(chunk.text, end="", flush=True),
            
                # match(fc.name):
                #     case("doc_reader"):
                #         markdown = document_understanding.doc_reader(fc.args['path'])
                #         print("\nFunction Response: ", markdown[:100], "\n...")
                #         summary = chat.send_message(f"Summarize this:{markdown}")
                #         print("\nGemini: ",summary.text)
                #         break