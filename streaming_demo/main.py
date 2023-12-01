from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import dotenv
from pydantic import BaseModel
from langchain.chat_models import ChatAnthropic
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate

dotenv.load_dotenv(".env")

app = FastAPI()

class Request(BaseModel):
    query: str = "Hello, how are you?"

class Response(BaseModel):
    text: str

@app.post("/")
async def root(request: Request) -> Response:
    prompt = ChatPromptTemplate.from_messages(
        (
            ("assistant", "You're helpful assistant. Answer user's question."),
            ("human", "{question}"),
        )
    )
    chain = (
        prompt |
        ChatAnthropic() |
        StrOutputParser()
    )

    return StreamingResponse(chain.astream({"question": request.query}))
