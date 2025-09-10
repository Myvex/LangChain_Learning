# 02_text_embedding.py
# 说明：演示 OpenAIEmbeddings 的使用、向量形状、余弦相似度计算以及 FAISS 索引检索
# 运行方式：python 02_text_embedding.py

from langchain.embeddings import OpenAIEmbeddings

embeddings_model=OpenAIEmbeddings(openai_api_key="")
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh,hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
len(embeddings),len(embeddings[0])
embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
embedded_query[:5]