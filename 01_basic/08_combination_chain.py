# 08_combination_chain.py
# 说明：RunnableMap 多步链示例，演示如何在 LangChain 中串联多条子链
# 运行方式：python 01_basic/08_combination_chain.py

from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.chat_models import ChatOpenAI

# 1️⃣ 初始化 LLM（请填入你的 OpenAI API Key）
model = ChatOpenAI(openai_api_key="YOUR_OPENAI_API_KEY")

# 2️⃣ 子链：生成随机颜色
prompt1 = ChatPromptTemplate.from_template("generate a random color")
chain1 = prompt1 | model | StrOutputParser()

# 3️⃣ 子链：根据颜色查询水果
prompt2 = ChatPromptTemplate.from_template("What is a fruit of color {color}")
chain2 = prompt2 | model | StrOutputParser()

# 4️⃣ 子链：根据颜色查询国家
prompt3 = ChatPromptTemplate.from_template("What is a country whose flag has the color {color}")
chain3 = prompt3 | model | StrOutputParser()

# 5️⃣ 子链：根据水果和国家输出一句话
prompt4 = ChatPromptTemplate.from_template(
    "The fruit {fruit} is often found in the country whose flag color is {color}."
)

# 6️⃣ 组合成 RunnableMap
runnable = RunnableMap(
    steps={
        "color": chain1,
        "fruit": chain2,
        "country": chain3,
    }
) | prompt4

# 7️⃣ 触发链
response = runnable.invoke({})
print(response)
