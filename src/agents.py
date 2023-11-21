from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_verbose

load_dotenv()

set_verbose(True)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = load_tools(["ddg-search"])

agent_chain = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS)

result = agent_chain.run("東京の天気を教えて")
print(result)
