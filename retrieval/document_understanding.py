# from markitdown import MarkItDown

# md = MarkItDown()

# def doc_reader(path):
#     """Converts input files to stripped down markdown, \n
#     easy for LLM to process and requires less tokens"""

#     output = md.convert(path)
#     return output.text_content
    

# doc_tool = {
#     "name" : "markdown",
#     "description" : "a tool that reads raw pdf, ppt, word etc files and converts them into markdown",
#     "parameters" : {
#         "type" : "object",
#         "properties" : {
#             "path" : {
#                 "type" : "string",
#                 "description" : "the path to the file"
#             },
#         },
#         "required" : ["path"]
    
#     }
# }
from markitdown import MarkItDown

md = MarkItDown()

def doc_reader(path):
    output = md.convert(path)
    return output.text_content