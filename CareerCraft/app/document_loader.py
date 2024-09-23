import os
from flask import current_app
from werkzeug.utils import secure_filename, safe_join
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, WebBaseLoader

def load_document(file_or_text, file_type):
    if file_type == 'file':
        file_extension = os.path.splitext(file_or_text.filename)[1].lower()
        temp_path = safe_join(current_app.root_path, 'temp', secure_filename(file_or_text.filename))
        file_or_text.save(temp_path)
        
        if file_extension == '.pdf':
            loader = PyPDFLoader(temp_path)
            pages = loader.load_and_split()
            content = ' '.join([page.page_content for page in pages])
        elif file_extension in ['.doc', '.docx']:
            loader = Docx2txtLoader(temp_path)
            data = loader.load()
            content = data[0].page_content
        else:
            with open(temp_path, 'r') as file:
                content = file.read()
        
        os.remove(temp_path)
        return content
    elif file_type == 'url':
        loader = WebBaseLoader(file_or_text)
        data = loader.load()
        return data[0].page_content
    elif file_type == 'text':
        return file_or_text
    else:
        raise ValueError(f"Unsupported file type: {file_type}")