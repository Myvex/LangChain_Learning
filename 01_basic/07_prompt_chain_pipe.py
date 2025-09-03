# 07_prompt_chain_pipe.py
# 说明：Prompt‑Chain-Pipe 示例，使用 ChatPromptTemplate、ChatOpenAI 与 StrOutputParser
# 运行方式：python 01_basic/07_prompt_chain_pipe.py

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

# 1️⃣ 定义提示模板
prompt = ChatPromptTemplate.from_template(
    "tell me a joke about {topic}"
)

# 2️⃣ 初始化 LLM（请填入你的 OpenAI API Key）
model = ChatOpenAI(openai_api_key="YOUR_OPENAI_API_KEY")

# 3️⃣ 解析器：把模型输出转换为纯字符串
parser = StrOutputParser()

# 4️⃣ 用管道语法把三者串联成一个链
chain = prompt | model | parser

# 5️⃣ 通过 invoke 触发链，传入参数
response = chain.invoke({"topic": "bears"})
print(response)
