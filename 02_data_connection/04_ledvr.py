# 04_ledvr.py
# 说明：从文本文件读取 → 切分 → 嵌入 → FAISS/Chroma 索引 → 通过 RetrievalQA 做问答
# 运行方式：python 04_ledvr.py

import os
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS, Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# LEDVR：raw_documents是L，OpenAIEmbeddings()是E，documents是D，faiss_db是V

# 1️⃣ 读取文本文件
raw_documents = TextLoader('../../../state_of_the_union.txt').load()   # List[Document]

# 2️⃣ 文本切分（每 1000 字符一个块）
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)   # List[Document]

# 3️⃣ FAISS 向量库（如果你想用 FAISS 先做检索）
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
faiss_db = FAISS.from_documents(documents, embeddings)

# 4️⃣ 通过 FAISS 做一次检索示例
query = "What did the president say about Ketanji Brown Jackson"
docs = faiss_db.similarity_search(query)
print("\n--- FAISS 检索结果 ---")
print(docs[0].page_content)

# 5️⃣ (可选) 用 Chroma 做向量索引
chromadb = Chroma.from_documents(documents, embeddings)

# 6️⃣ 用 RetrievalQA 结合 LLM 做问答
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))  # 这里使用 ChatOpenAI
retriever = chromadb.as_retriever()   # 也可以用 faiss_db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# 7️⃣ 直接问答
question = "What did the president say about Ketanji Brown Jackson"
answer = qa_chain.run(question)
print("\n--- RetrievalQA 生成答案 ---")
print(answer)