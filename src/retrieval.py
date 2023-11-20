from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores.faiss import FAISS

load_dotenv()

# 文書をベクトル化してVector Storeに格納
vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

# 「検索 => プロンプトの穴埋め => LLMで回答を生成」というchainを作成
prompt = ChatPromptTemplate.from_template(
    """以下のcontextだけに基づいて回答してください。

{context}

質問: {question}
"""
)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

# chainを実行
result = chain.invoke("where did harrison work?")
print(result.content)
