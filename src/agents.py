from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_verbose

load_dotenv()

set_verbose(True)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# LLMが使えるツールを準備（「ddg-search」はDuckDuckGoという検索エンジン）
tools = load_tools(["ddg-search"])

# エージェントを初期化
agent_chain = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS)

# エージェントを実行
result = agent_chain.run("東京の天気を教えて")
print(result)
