# 02_translate.py
# 说明：使用 LangChain 的 ChatOpenAI 进行一次简单的翻译
# 运行方式：python 01_basic/02_translate.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# 创建 ChatOpenAI 实例，温度设为 0，得到更确定的答案
chat = ChatOpenAI(temperature=0)

# 发送一条 HumanMessage，得到 AI 的回复
response = chat.predict_message([
    HumanMessage(
        content=(
            "Translate this sentence from English to French "
            "I love programming"
        )
    )
])

print("AI 给出的法语翻译：")
print(response)
