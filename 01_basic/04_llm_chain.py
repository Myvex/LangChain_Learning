# 04_llm_chain.py
# 说明：使用 LLMChain + ChatPromptTemplate 进行一次翻译任务
# 运行方式：python 01_basic/04_llm_chain.py

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 1️⃣ 创建 ChatOpenAI 实例
chat = ChatOpenAI(temperature=0)

# 2️⃣ 定义系统与人类消息模板
template = (
    "You are a helpful assistant that translates {input_language} to "
    " {output_language}"
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 3️⃣ 组合成完整的 ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# 4️⃣ 构建 LLMChain
chain = LLMChain(llm=chat, prompt=chat_prompt)

# 5️⃣ 运行链
result = chain.run(
    input_language="English",
    output_language="French",
    text="I love programming."
)

print("翻译结果：")
print(result)
