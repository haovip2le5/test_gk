# Hướng Dẫn Thao Tác Backend

## Mục Lục
1. [Chạy Backend](#chạy-backend)
2. [Cấu Trúc Backend](#cấu-trúc-backend)
3. [API Endpoints](#api-endpoints)
4. [Thay Đổi Dữ Liệu Test](#thay-đổi-dữ-liệu-test)
5. [Thêm Endpoints Mới](#thêm-endpoints-mới)
6. [Cơ Sở Dữ Liệu (In-Memory)](#cơ-sở-dữ-liệu-in-memory)
7. [Debug & Logging](#debug--logging)
8. [Cấu Hình Backend](#cấu-hình-backend)

---

## Chạy Backend

### Cách 1: Chạy Trực Tiếp

```bash
cd backend
python main.py
```

**Output mong đợi:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Cách 2: Chạy với Venv (Ưu Tiên)

```bash
# Tạo virtual environment (lần đầu)
cd backend
python -m venv venv

# Kích hoạt venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy server
python main.py
```

### Cách 3: Chạy Cùng Frontend

```bash
# Terminal 1 - Backend
cd backend
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

---

## Cấu Trúc Backend

```
backend/
├── main.py                  # File chính (FastAPI app)
├── requirements.txt         # Dependencies
└── __pycache__/            # Cache files (bỏ qua)
```

---

## API Endpoints

### 1. **Xác Thực (Authentication)**

#### POST /login
Đăng nhập người dùng

**Request:**
```json
{
  "username": "user1",
  "password": "pass123"
}
```

**Response (Thành công):**
```json
{
  "success": true,
  "message": "Đăng nhập thành công",
  "user": {
    "username": "user1",
    "role": "user"
  }
}
```

**Response (Thất bại):**
```json
{
  "success": false,
  "message": "Mật khẩu không chính xác"
}
```

#### POST /register
Đăng ký người dùng mới

**Request:**
```json
{
  "username": "newuser",
  "password": "pass123",
  "confirmPassword": "pass123",
  "role": "user"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Đăng ký thành công"
}
```

---

### 2. **Quiz (Kiến Thức)**

#### GET /questions
Lấy danh sách câu hỏi

**Response:**
```json
[
  {
    "id": 1,
    "question": "React là thư viện của ngôn ngữ nào?",
    "options": ["Python", "JavaScript", "Java", "C#"],
    "correct_answer": "JavaScript"
  },
  ...
]
```

#### POST /submit
Nộp bài quiz

**Request:**
```json
{
  "username": "user1",
  "answers": [
    {
      "question_id": 1,
      "selected_answer": "JavaScript"
    },
    {
      "question_id": 2,
      "selected_answer": "Python 3.6+"
    }
  ]
}
```

**Response:**
```json
{
  "correct_count": 2,
  "total_questions": 8,
  "score": 2.5,
  "results": [
    {
      "question_id": 1,
      "question": "React là thư viện của ngôn ngữ nào?",
      "selected_answer": "JavaScript",
      "correct_answer": "JavaScript",
      "is_correct": true
    },
    ...
  ]
}
```

---

### 3. **Admin (Thống Kê)**

#### GET /admin/users
Lấy danh sách toàn bộ người dùng

**Response:**
```json
[
  {
    "username": "user1",
    "role": "user",
    "submission_count": 3
  },
  {
    "username": "admin",
    "role": "admin",
    "submission_count": 0
  }
]
```

#### GET /admin/statistics
Lấy thống kê toàn bộ

**Response:**
```json
{
  "total_users": 3,
  "total_submissions": 5,
  "average_score": 6.2,
  "highest_score": 9.5,
  "recent_submissions": [
    {
      "username": "user1",
      "score": 7.5,
      "timestamp": "2024-03-30T10:30:00.000000"
    }
  ],
  "user_statistics": [
    {
      "username": "user1",
      "submission_count": 3,
      "average_score": 6.8
    }
  ]
}
```

#### DELETE /admin/users/{username}
Xóa người dùng

**Response:**
```json
{
  "success": true,
  "message": "Đã xóa user user1"
}
```

---

## Thay Đổi Dữ Liệu Test

### Thay Đổi Tài Khoản Test

**File:** `backend/main.py`

```python
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
        "password": hashlib.sha256("password123".encode()).hexdigest(),  # Đổi password
        "role": "user"
    }
}
```

### Thêm Tài Khoản Mới

```python
USERS_DATABASE = {
    # ... tài khoản cũ ...
    "newuser": {
        "password": hashlib.sha256("mypassword".encode()).hexdigest(),
        "role": "user"
    }
}
```

### Thay Đổi Câu Hỏi Test

**File:** `backend/main.py`

```python
QUESTIONS = [
    {
        "id": 1,
        "question": "Câu tùy chỉnh của bạn?",
        "options": ["Lựa chọn 1", "Lựa chọn 2", "Lựa chọn 3", "Lựa chọn 4"],
        "correct_answer": "Lựa chọn 2"
    },
    # ... thêm câu hỏi khác ...
]
```

---

## Thêm Endpoints Mới

### Ví Dụ 1: Endpoint GET Đơn Giản

```python
@app.get("/api/hello")
async def hello():
    """Endpoint hello world"""
    return {
        "message": "Hello from FastAPI",
        "status": "success"
    }
```

**Test với URL:** `http://localhost:8000/api/hello`

### Ví Dụ 2: Endpoint POST với Dữ Liệu

```python
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    email: str
    age: int

@app.post("/api/create-user")
async def create_user(request: CreateUserRequest):
    """Tạo người dùng mới"""
    return {
        "success": True,
        "message": f"User {request.username} created",
        "user": {
            "username": request.username,
            "email": request.email,
            "age": request.age
        }
    }
```

**Test với Request:**
```json
POST http://localhost:8000/api/create-user
Content-Type: application/json

{
  "username": "john",
  "email": "john@example.com",
  "age": 25
}
```

### Ví Dụ 3: Endpoint GET với Path Parameter

```python
@app.get("/api/user/{username}")
async def get_user(username: str):
    """Lấy thông tin user theo username"""
    if username in USERS_DATABASE:
        return {
            "username": username,
            "role": USERS_DATABASE[username]["role"]
        }
    else:
        return {
            "success": False,
            "message": f"User {username} not found"
        }
```

**Test với URL:** `http://localhost:8000/api/user/user1`

### Ví Dụ 4: Endpoint với Query Parameters

```python
@app.get("/api/search")
async def search(keyword: str, limit: int = 10):
    """Tìm kiếm"""
    return {
        "keyword": keyword,
        "limit": limit,
        "results": []
    }
```

**Test với URL:** `http://localhost:8000/api/search?keyword=react&limit=5`

---

## Cơ Sở Dữ Liệu (In-Memory)

### Hiểu Về In-Memory Database

- **Dữ liệu lưu trong RAM** (bộ nhớ tạm)
- **Dữ liệu mất khi restart** server
- **Dùng cho testing/development** (không dùng cho production)

### Dữ Liệu Được Lưu

```python
USERS_DATABASE = {}              # Lưu người dùng
SUBMISSIONS_HISTORY = []         # Lưu kết quả submission
```

### Cách Đọc/Ghi Dữ Liệu

**Đọc user:**
```python
user = USERS_DATABASE.get("user1")
if user:
    print(user["role"])
```

**Thêm user:**
```python
USERS_DATABASE["newuser"] = {
    "password": hashlib.sha256("pass".encode()).hexdigest(),
    "role": "user"
}
```

**Đọc submissions:**
```python
for submission in SUBMISSIONS_HISTORY:
    print(submission["username"], submission["score"])
```

**Thêm submission:**
```python
SUBMISSIONS_HISTORY.append({
    "username": "user1",
    "score": 7.5,
    "timestamp": datetime.now().isoformat()
})
```

### Cách Chuyển Sang Database Thực (PostgreSQL)

1. **Cài `sqlalchemy` và `psycopg2`:**
```bash
pip install sqlalchemy psycopg2-binary
```

2. **Tạo file `models.py`:**
```python
from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/quiz_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    password = Column(String)
    role = Column(String)

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    score = Column(Float)
    timestamp = Column(DateTime)
```

3. **Sử dụng trong `main.py`:**
```python
from models import SessionLocal, User
db = SessionLocal()
user = db.query(User).filter(User.username == "user1").first()
```

---

## Debug & Logging

### Thêm Print Debug

```python
@app.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """User login endpoint"""
    print(f"Login attempt: {request.username}")  # Debug
    
    user_data = USERS_DATABASE.get(request.username)
    print(f"User found: {user_data is not None}")  # Debug
    
    if not user_data:
        return LoginResponse(success=False, message="Username không tồn tại")
    
    # ...
```

### Sử dụng Logging (Ưu Tiên)

```python
import logging

# Cấu hình logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    logger.info(f"Login attempt from {request.username}")
    logger.debug(f"Request data: {request}")
    
    # ...
    
    logger.info(f"Login successful for {request.username}")
    return LoginResponse(success=True, user={"username": request.username})
```

### Xem Logs

```bash
# Logs sẽ hiển thị trong terminal nơi chạy server
tail -f server.log  # On Mac/Linux
Get-Content server.log -Tail 10  # On Windows
```

---

## Cấu Hình Backend

### Thay Đổi Port

**File:** `backend/main.py`

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8001  # Thay đổi port từ 8000 thành 8001
    )
```

**Sau đó cập nhật frontend:**

**File:** `frontend/src/App.jsx`

```javascript
const response = await fetch('http://localhost:8001/questions')  // Thay 8000 -> 8001
// ... và tất cả fetch URLs khác
```

### Thay Đổi Host

```python
# Chỉ localhost (mặc định):
uvicorn.run(app, host="127.0.0.1", port=8000)

# Cho phép mạng truy cập:
uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Thêm CORS Domains

**File:** `backend/main.py`

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",      # Thêm domain mới
        "https://example.com"         # Production domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Kiểm Tra Endpoints với Tools

### 1. Postman
```
Tải từ: https://www.postman.com/downloads/
```

Ví dụ test:
```
POST http://localhost:8000/login
Content-Type: application/json

{
  "username": "user1",
  "password": "pass123"
}
```

### 2. Curl (Command Line)

```bash
# GET
curl http://localhost:8000/questions

# POST
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"pass123"}'

# DELETE
curl -X DELETE http://localhost:8000/admin/users/user1
```

### 3. FastAPI Interactive Docs

Truy cập: `http://localhost:8000/docs`

Hoặc: `http://localhost:8000/redoc`

---

## Cấu Trúc FastAPI

```python
# 1. Import
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 2. Khởi tạo app
app = FastAPI()

# 3. Định nghĩa models (Pydantic)
class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str

# 4. Định nghĩa endpoints
@app.get("/questions")
async def get_questions():
    return QUESTIONS

@app.post("/login")
async def login(request: LoginRequest):
    return LoginResponse(...)

# 5. Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

---

## Thường Gặp Lỗi

### Lỗi: Address already in use (Port bị chiếm)
```bash
# Đóng process đang sử dụng port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -i :8000
kill -9 <PID>
```

### Lỗi: Module not found
```bash
pip install -r requirements.txt
```

### Lỗi: CORS error
Cập nhật `allow_origins` trong CORS middleware:
```python
allow_origins=["http://localhost:5173", "http://your-domain.com"]
```

### Lỗi: Password không khớp
Password phải **match exactly** (case-sensitive):
```python
# Khi đăng ký:
hashed = hashlib.sha256("MyPass123".encode()).hexdigest()

# Khi đăng nhập phải dùng:
"MyPass123"  # Chứ không phải "mypass123"
```

---

## Mẹo Hữu Ích

1. **Hot reload:** Cài `uvicorn[standard]`:
```bash
pip install uvicorn[standard]
# Server sẽ tự reload khi có thay đổi file
```

2. **Lưu dữ liệu persistent:** Để dữ liệu không mất khi restart, chuyển sang database thực (PostgreSQL, MongoDB, etc.)

3. **Validate input:** Luôn dùng Pydantic models để validate input từ client

4. **Error handling:** Sử dụng try/except:
```python
try:
    hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
except Exception as e:
    logger.error(f"Error hashing password: {e}")
    return {"success": False, "message": "Server error"}
```

---

## Liên Kết Hữu Ích

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Uvicorn**: https://www.uvicorn.org/
- **Pydantic**: https://docs.pydantic.dev/
- **SQLAlchemy**: https://docs.sqlalchemy.org/

Chúc bạn phát triển backend thành công! 🚀
