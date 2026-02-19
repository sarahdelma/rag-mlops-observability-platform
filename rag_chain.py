from langchain_groq import ChatGroq

from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents.stuff import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_community.chat_message_histories import ChatMessageHistory

from flipkart.config import Config

class RAGChainBuilder:
    def __init__(self,vector_store):
        self.vector_store=vector_store
        self.model = ChatGroq(model=Config.RAG_MODEL , temperature=0.5)
        self.history_store={}   # empty dictionary for history store

    def _get_history(self,session_id:str) -> BaseChatMessageHistory:     
        if session_id not in self.history_store:      # if the history of the document already exist, return the session_id
            self.history_store[session_id] = ChatMessageHistory()    # if not then create a new session_id using the ChatHistory()
        return self.history_store[session_id]
    
    def build_chain(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k":3})  # converts the vector store into retriever
#rewrites user question (merging or retrieves the info from previous history)using the previous questions, done internally. 
        context_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and user question, rewrite it as a standalone question."), #system takes this command, chat_history represents this.
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}")  # input from the user
        ])
#question and answer prompt, the response how the bot has to reply
        qa_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a helpful e-commerce assistant that answers product-related questions using only the provided context (reviews, titles, descriptions).  

- Always stay **within the context**; do not invent information.  
- Keep answers **concise, clear, and actionable**.  
- Use **numbered lists** (1., 2., 3., ...) for products with newline.
- Use **bullet points** when listing features, pros/cons, or suggestions.  
- If the answer is not in the context, politely say: "I could not find relevant information in the provided context."

CONTEXT:
{context}

QUESTION:
{input}
"""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])
# a variable to understand the pattern of response from history
        history_aware_retriever = create_history_aware_retriever(
            self.model , retriever , context_prompt
        )
# a variable how to answer, to the given user input
        question_answer_chain = create_stuff_documents_chain(
            self.model , qa_prompt
        )
# 2 types of prompt commands given to rag_chain variable---RAG PIPELINE
        rag_chain = create_retrieval_chain(
            history_aware_retriever,question_answer_chain
        )
# a function that accepts the rag_chain, (the response pattern), from the user_input, also checking the history from the MessagesPlaceholder(variable_name="chat_history")
        return RunnableWithMessageHistory(
            rag_chain,
            self._get_history,    # calls the function get_history, see above
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )