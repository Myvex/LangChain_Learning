# 01_loader_retriever.py
# 说明：演示如何从网页抓取、切分、向量化、检索并使用 LLM 生成答案
# 运行方式：python 01_loader_retriever.py

from langchain.document_loaders import WebBaseLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

loader = WebBaseLoader("http://developers.mini1.cn/wiki/luawh.html")
data = loader.load()
embedding = OpenAIEmbeddings(openai_api_key="")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500.chunk_overlap=0)
splits = text_splitter.split_documents(data)
vectordb=FAISS.from_documents(documents=splits,embedding=embedding)
quesition = "LUA 的宿主语言是什么？"
llm = ChatOpenAI(openai_api_key="")
retriever_from_llm=MultiQueryRetriever.from_llm(
    retriever = vectordb.as_retriever(),llm=llm
)
docs = retriever_from_llm.get_relavant_documents(quesition)
