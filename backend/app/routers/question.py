from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.chains import QAWithSourcesChain
from ..database import get_db
from ..models import Document

router = APIRouter()

# Define a Pydantic model for the request body
class AskQuestionRequest(BaseModel):
    document_id: int
    question: str

@router.post("/ask")
async def ask_question(request: AskQuestionRequest, db: Session = Depends(get_db)):
    # Retrieve the document from the database
    document = db.query(Document).filter(Document.id == request.document_id).first()
    if not document:
        return {"error": "Document not found"}
    
    # Retrieve text content from the document for NLP processing
    text_content = document.text_content
    
    # Initialize LangChain components
    llm = OpenAI(model_name="text-davinci-003")  # Make sure your API keys are configured
    chain = QAWithSourcesChain(llm=llm)

    # Run the QA chain with the text content of the document and the input question
    answer = chain({"input_documents": [{"page_content": text_content}], "question": request.question})
    
    return {"answer": answer['output_text']}
