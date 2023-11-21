from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, SQLChatMessageHistory

load_dotenv()

MEMORY_SQLITE_FILE = "memory.sqlite"
SESSION_ID = "123"

llm = ChatOpenAI(model="gpt-4", temperature=0)

history = SQLChatMessageHistory(
    session_id=SESSION_ID,
    connection_string=f"sqlite:///{MEMORY_SQLITE_FILE}",
)
memory = ConversationBufferMemory(chat_memory=history)

chain = ConversationChain(llm=llm, memory=memory)

while True:
    user_message = input("You: ")
    ai_message = chain.run(user_message)
    print(f"AI:  {ai_message}")
