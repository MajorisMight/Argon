from pathlib import Path

def list_files(path="."):
    """Returns a visual string tree of the directory structure."""
    
    def build_tree(dir_path, prefix=""):
        lines = []
        # Filter out annoying pycache or git folders to save space
        items = [p for p in Path(dir_path).iterdir() if p.name not in [".git", "__pycache__"]]
        
        for i, item in enumerate(sorted(items, key=lambda x: (x.is_file(), x.name))):
            is_last = (i == len(items) - 1)
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{item.name}")
            
            if item.is_dir():
                sub_prefix = "    " if is_last else "│   "
                lines.extend(build_tree(item, prefix=sub_prefix))
        return lines

    return "\n".join(build_tree(path))
    
    
    
    
def read_file(path):
    """Returns the data read from a file"""
    with open(path, "r") as file:
        data = file.read()
        return data
        
        
def write_file(path, content):
    """Writes or Overwrites a file"""
    with open(path, "w") as file:
        file.write(content)
    return f"Succesfully written to {path}"
        
def append_file(path, content):
    """Adds to a file"""
    with open(path, "a") as file:
        file.write(f"\n{content}")
    return f"Succesfully written to {path}"
    
def dlt_file(path):
    """Deletes a file"""
    if(Path(path).exists()):
        Path(path).unlink()
        return (f"Deleted {path} successfully.")
    else:
        return (f"{path} does not exist!")


### Tool Descriptions

files_list = {
    "name" : "list_files",
    "description" : "returns the files in current directory",
    "parameters" : {
        "type" : "object",
        "properties" : {}
    }
}

file_read = {
    "name" : "read_file",
    "description" : "returns the contents of file based on a given path",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "path" : {
                "type" : "string",
                "description" : "Path for the file to be read"
            }
        },
        "required" : ["path"]
    }
}

file_write = {
    "name" : "write_file",
    "description" : "Creates a new file or overwrite an already existing one",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "path" : {
                "type" : "string",
                "description" : "Path for the file to be written"
            },
            "content" : {
                "type" : "string",
                "description" : "The content to be written in the file"
            }
        },
        "required" : ["path", "content"]
    }
}

file_append = {
    "name" : "append_file",
    "description" : "adds content to the end of an already existing file",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "path" : {
                "type" : "string",
                "description" : "Path for the file to be appended into"
            },
            "content" : {
                "type" : "string",
                "description" : "The content to be added to the file"
            }
        },
        "required" : ["path", "content"]
    }
}

file_delete = {
    "name" : "dlt_file",
    "description" : "Deletes a file",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "path" : {
                "type" : "string",
                "description" : "Path for the file to be deleted"
            }
        }
    }
}