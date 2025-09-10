# 03_text_splitter.py
# 说明：演示 CharacterTextSplitter 与 RecursiveCharacterTextSplitter 的用法
# 运行方式：python 03_text_splitter.py

from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter,Language
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
text_splitter=CharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
)
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])

JS_CODE= """
    function helloWorld(){
        console.log("Hello world!");
    }

    //call
    helloWorld();
    """
js_splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.JS ,chunk_size = 60.chunk_overlap=0
)
js_docs = js_splitter.create_documents([JS_CODE])

