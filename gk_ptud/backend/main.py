from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str

class Answer(BaseModel):
    question_id: int
    selected_answer: str

class SubmissionData(BaseModel):
    answers: List[Answer]

class QuestionResult(BaseModel):
    question_id: int
    question: str
    selected_answer: str
    correct_answer: str
    is_correct: bool

class SubmissionResult(BaseModel):
    correct_count: int
    total_questions: int
    score: float
    results: List[QuestionResult]

# Sample Questions Database
QUESTIONS = [
    {
        "id": 1,
        "question": "React là thư viện của ngôn ngữ nào?",
        "options": ["Python", "JavaScript", "Java", "C#"],
        "correct_answer": "JavaScript"
    },
    {
        "id": 2,
        "question": "FastAPI được xây dựng dựa trên bản nào của Python?",
        "options": ["Python 2.7", "Python 3.6+", "Python 3.4+", "Python 3.8+"],
        "correct_answer": "Python 3.6+"
    },
    {
        "id": 3,
        "question": "HTTP method nào dùng để lấy dữ liệu từ server?",
        "options": ["POST", "PUT", "GET", "DELETE"],
        "correct_answer": "GET"
    },
    {
        "id": 4,
        "question": "CORS là viết tắt của?",
        "options": [
            "Cross-Origin Resource Security",
            "Cross-Origin Resource Sharing",
            "Cross-Origin Remote Server",
            "Cross-Origin Request Shipping"
        ],
        "correct_answer": "Cross-Origin Resource Sharing"
    },
    {
        "id": 5,
        "question": "Component nào là component cơ bản trong React?",
        "options": ["Functional Component", "Class Component", "Cả 2", "Redux Component"],
        "correct_answer": "Cả 2"
    },
    {
        "id": 6,
        "question": "Hook nào dùng để quản lý state trong React Functional Component?",
        "options": ["useEffect", "useState", "useContext", "useReducer"],
        "correct_answer": "useState"
    },
    {
        "id": 7,
        "question": "RESTful API sử dụng những HTTP methods nào?",
        "options": [
            "GET, POST, PUT, PATCH, DELETE",
            "GET, POST, PUT, DELETE",
            "GET, POST",
            "Tất cả HTTP methods"
        ],
        "correct_answer": "GET, POST, PUT, PATCH, DELETE"
    },
    {
        "id": 8,
        "question": "JSON là viết tắt của?",
        "options": [
            "Java Script Object Notation",
            "JavaScript Object Notation",
            "Java Server Object Notation",
            "JavaScript Open Network"
        ],
        "correct_answer": "JavaScript Object Notation"
    },
]

@app.get("/questions", response_model=List[Question])
async def get_questions():
    """Lấy danh sách tất cả câu hỏi"""
    return QUESTIONS

@app.post("/submit", response_model=SubmissionResult)
async def submit_answers(submission: SubmissionData):
    """Nhận đáp án và trả về kết quả chấm điểm"""
    
    correct_count = 0
    question_results = []
    
    # Create a map of questions for quick lookup
    questions_map = {q["id"]: q for q in QUESTIONS}
    
    # Check each answer
    for answer in submission.answers:
        question = questions_map.get(answer.question_id)
        
        if question:
            is_correct = answer.selected_answer == question["correct_answer"]
            if is_correct:
                correct_count += 1
            
            question_results.append(QuestionResult(
                question_id=answer.question_id,
                question=question["question"],
                selected_answer=answer.selected_answer,
                correct_answer=question["correct_answer"],
                is_correct=is_correct
            ))
    
    # Calculate score (10 points each question)
    total_questions = len(QUESTIONS)
    score = round((correct_count / total_questions) * 10, 1) if total_questions > 0 else 0
    
    return SubmissionResult(
        correct_count=correct_count,
        total_questions=total_questions,
        score=score,
        results=question_results
    )

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Quiz App Backend API",
        "endpoints": {
            "questions": "GET /questions",
            "submit": "POST /submit"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
