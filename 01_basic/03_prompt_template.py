# 03_prompt_template.py
# 说明：使用 LangChain 的 PromptTemplate 构造一个可复用的翻译提示
# 运行方式：python 01_basic/03_prompt_template.py

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 定义提示模板字符串
template = (
    "You are a helpful assistant that translates {input_language} to "
    " {output_language}"
)

# 创建系统消息提示模板
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 人类消息提示模板
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 组合成完整的 ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# 填充变量得到最终的消息列表
messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming."
)

print("生成的消息列表：")
for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")
