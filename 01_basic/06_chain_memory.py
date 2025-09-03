# 06_chain_memory.py
# 说明：ConversationChain 示例，配合记忆与 ChatOpenAI
# 运行方式：python 01_basic/06_chain_memory.py

from langchain.prompts import (
    ChatPromptTemplate,
    MessagePlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# 1️⃣ 定义对话模板
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        """
        The following is a friendly conversation between a human and an AI.
        The AI is talkative and provides lots of specific details from its
        context. If the AI does not know the answer to a question, it truthfully
        says it does not know.
        """
    ),
    MessagePlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# 2️⃣ 初始化 LLM 与记忆
llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)

# 3️⃣ 创建 ConversationChain
conversation = ConversationChain(
    memory=memory,
    prompt=prompt,
    llm=llm
)

# 4️⃣ 进行一次对话
response = conversation.predict(input="你好,我是Vex!")
print(response)
