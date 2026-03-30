from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import hashlib

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== AUTHENTICATION MODELS =====
class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    user: Optional[dict] = None

class RegisterRequest(BaseModel):
    username: str
    password: str
    confirmPassword: str
    role: str = "user"

class RegisterResponse(BaseModel):
    success: bool
    message: str

class User(BaseModel):
    username: str
    role: str

# ===== QUIZ MODELS =====
class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str

class Answer(BaseModel):
    question_id: int
    selected_answer: str

class SubmissionData(BaseModel):
    username: Optional[str] = None
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

# ===== ADMIN MODELS =====
class RecentSubmission(BaseModel):
    username: str
    score: float
    timestamp: str

class UserStat(BaseModel):
    username: str
    submission_count: int
    average_score: float

class AdminStatistics(BaseModel):
    total_users: int
    total_submissions: int
    average_score: float
    highest_score: float
    recent_submissions: List[RecentSubmission]
    user_statistics: List[UserStat]

# ===== QUESTION MANAGEMENT MODELS =====
class CreateQuestionRequest(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

class UpdateQuestionRequest(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None

class QuestionResponse(BaseModel):
    success: bool
    message: str
    question: Optional[dict] = None

# ===== DATABASE (In-Memory) =====
USERS_DATABASE = {
    "admin": {
        "password": hashlib.sha256("pass123".encode()).hexdigest(),
        "role": "admin"
    },
    "user1": {
        "password": hashlib.sha256("pass123".encode()).hexdigest(),
        "role": "user"
    },
    "user2": {
        "password": hashlib.sha256("pass123".encode()).hexdigest(),
        "role": "user"
    }
}

SUBMISSIONS_HISTORY = []

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

# ===== AUTHENTICATION ENDPOINTS =====
@app.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """User login endpoint"""
    user_data = USERS_DATABASE.get(request.username)
    
    if not user_data:
        return LoginResponse(
            success=False,
            message="Username không tồn tại"
        )
    
    hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
    if user_data["password"] != hashed_password:
        return LoginResponse(
            success=False,
            message="Mật khẩu không chính xác"
        )
    
    return LoginResponse(
        success=True,
        message="Đăng nhập thành công",
        user={
            "username": request.username,
            "role": user_data["role"]
        }
    )

@app.post("/register", response_model=RegisterResponse)
async def register(request: RegisterRequest):
    """User registration endpoint"""
    if request.username in USERS_DATABASE:
        return RegisterResponse(
            success=False,
            message="Tên người dùng đã tồn tại"
        )
    
    if request.password != request.confirmPassword:
        return RegisterResponse(
            success=False,
            message="Mật khẩu không khớp"
        )
    
    if len(request.password) < 6:
        return RegisterResponse(
            success=False,
            message="Mật khẩu phải có ít nhất 6 ký tự"
        )
    
    hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
    USERS_DATABASE[request.username] = {
        "password": hashed_password,
        "role": request.role
    }
    
    return RegisterResponse(
        success=True,
        message="Đăng ký thành công"
    )

# ===== QUIZ ENDPOINTS =====
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
    
    # Track submission in history
    if submission.username:
        SUBMISSIONS_HISTORY.append({
            "username": submission.username,
            "score": score,
            "timestamp": datetime.now().isoformat()
        })
    
    return SubmissionResult(
        correct_count=correct_count,
        total_questions=total_questions,
        score=score,
        results=question_results
    )

# ===== ADMIN ENDPOINTS =====
@app.get("/admin/users")
async def get_all_users():
    """Get all users with submission count"""
    user_list = []
    for username, user_data in USERS_DATABASE.items():
        submission_count = sum(1 for s in SUBMISSIONS_HISTORY if s["username"] == username)
        user_list.append({
            "username": username,
            "role": user_data["role"],
            "submission_count": submission_count
        })
    return user_list

@app.get("/admin/statistics", response_model=AdminStatistics)
async def get_admin_statistics():
    """Get overall quiz statistics"""
    total_users = len(USERS_DATABASE)
    total_submissions = len(SUBMISSIONS_HISTORY)
    
    if total_submissions == 0:
        return AdminStatistics(
            total_users=total_users,
            total_submissions=0,
            average_score=0.0,
            highest_score=0.0,
            recent_submissions=[],
            user_statistics=[]
        )
    
    scores = [s["score"] for s in SUBMISSIONS_HISTORY]
    average_score = round(sum(scores) / len(scores), 1)
    highest_score = round(max(scores), 1)
    
    # Get recent submissions (last 5)
    recent = []
    for submission in SUBMISSIONS_HISTORY[-5:]:
        recent.append(RecentSubmission(
            username=submission["username"],
            score=submission["score"],
            timestamp=submission["timestamp"]
        ))
    recent.reverse()  # Most recent first
    
    # Calculate user statistics
    user_stats = {}
    for submission in SUBMISSIONS_HISTORY:
        username = submission["username"]
        if username not in user_stats:
            user_stats[username] = []
        user_stats[username].append(submission["score"])
    
    user_statistics = []
    for username, scores in user_stats.items():
        user_statistics.append(UserStat(
            username=username,
            submission_count=len(scores),
            average_score=round(sum(scores) / len(scores), 1)
        ))
    
    return AdminStatistics(
        total_users=total_users,
        total_submissions=total_submissions,
        average_score=average_score,
        highest_score=highest_score,
        recent_submissions=recent,
        user_statistics=user_statistics
    )

@app.delete("/admin/users/{username}")
async def delete_user(username: str):
    """Delete a user (admin only)"""
    if username not in USERS_DATABASE:
        return {"success": False, "message": "User không tồn tại"}
    
    if USERS_DATABASE[username]["role"] == "admin":
        return {"success": False, "message": "Không thể xóa admin"}
    
    del USERS_DATABASE[username]
    return {"success": True, "message": f"Đã xóa user {username}"}

# ===== QUESTION MANAGEMENT ENDPOINTS =====
@app.post("/admin/questions", response_model=QuestionResponse)
async def create_question(request: CreateQuestionRequest):
    """Tạo câu hỏi mới (admin only)"""
    # Validate options has 4 items
    if len(request.options) != 4:
        return QuestionResponse(
            success=False,
            message="Câu hỏi phải có đúng 4 lựa chọn"
        )
    
    # Validate correct answer is in options
    if request.correct_answer not in request.options:
        return QuestionResponse(
            success=False,
            message="Đáp án chính xác phải nằm trong các lựa chọn"
        )
    
    # Find next ID
    next_id = max([q["id"] for q in QUESTIONS]) + 1 if QUESTIONS else 1
    
    new_question = {
        "id": next_id,
        "question": request.question,
        "options": request.options,
        "correct_answer": request.correct_answer
    }
    
    QUESTIONS.append(new_question)
    
    return QuestionResponse(
        success=True,
        message=f"Đã thêm câu hỏi mới với ID {next_id}",
        question=new_question
    )

@app.put("/admin/questions/{question_id}", response_model=QuestionResponse)
async def update_question(question_id: int, request: UpdateQuestionRequest):
    """Cập nhật câu hỏi (admin only)"""
    # Find question
    question = None
    for q in QUESTIONS:
        if q["id"] == question_id:
            question = q
            break
    
    if not question:
        return QuestionResponse(
            success=False,
            message=f"Câu hỏi với ID {question_id} không tồn tại"
        )
    
    # Update fields if provided
    if request.question is not None:
        question["question"] = request.question
    
    if request.options is not None:
        if len(request.options) != 4:
            return QuestionResponse(
                success=False,
                message="Câu hỏi phải có đúng 4 lựa chọn"
            )
        question["options"] = request.options
    
    if request.correct_answer is not None:
        # Check if correct answer is in options
        if request.correct_answer not in question["options"]:
            return QuestionResponse(
                success=False,
                message="Đáp án chính xác phải nằm trong các lựa chọn"
            )
        question["correct_answer"] = request.correct_answer
    
    return QuestionResponse(
        success=True,
        message=f"Đã cập nhật câu hỏi ID {question_id}",
        question=question
    )

@app.delete("/admin/questions/{question_id}", response_model=QuestionResponse)
async def delete_question(question_id: int):
    """Xóa câu hỏi (admin only)"""
    global QUESTIONS
    
    # Find and remove question
    original_length = len(QUESTIONS)
    QUESTIONS = [q for q in QUESTIONS if q["id"] != question_id]
    
    if len(QUESTIONS) == original_length:
        return QuestionResponse(
            success=False,
            message=f"Câu hỏi với ID {question_id} không tồn tại"
        )
    
    return QuestionResponse(
        success=True,
        message=f"Đã xóa câu hỏi ID {question_id}"
    )

# ===== HEALTH CHECK =====
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
