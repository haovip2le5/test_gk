# Hướng Dẫn Thêm Code Login Vào Các File Chính

---

## 🔐 CODE LOGIN PHẦN BACKEND

### Code thêm vào file `backend/main.py`

**Vị trí thêm:** Đầu file, sau các import hiện tại

```python
# Thêm những import này:
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from pathlib import Path
import json
```

---

**Vị trí thêm:** Sau CORS middleware, trước QUESTIONS

```python
# ===== SECURITY CONFIGURATION =====
SECRET_KEY = "your-secret-key-change-this-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== DATA MODELS =====
class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

# ===== USER DATABASE =====
USERS_DB_FILE = Path("users.json")

def load_users_db():
    if USERS_DB_FILE.exists():
        with open(USERS_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users_db(users_dict):
    with open(USERS_DB_FILE, "w") as f:
        json.dump(users_dict, f, indent=4)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    users_dict = load_users_db()
    if username not in users_dict:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    return users_dict[username]
```

---

**Vị trí thêm:** Trước endpoint `/questions` (hoặc trước dòng `@app.get("/questions")`)

```python
# ===== AUTHENTICATION ENDPOINTS =====

@app.post("/register", response_model=Token)
async def register(user_data: UserRegister):
    """Đăng ký tài khoản mới"""
    users_dict = load_users_db()
    
    if user_data.username in users_dict:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    hashed_password = hash_password(user_data.password)
    new_user = {
        "username": user_data.username,
        "email": user_data.email,
        "full_name": user_data.full_name or user_data.username,
        "hashed_password": hashed_password
    }
    
    users_dict[user_data.username] = new_user
    save_users_db(users_dict)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_data.username},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    """Đăng nhập"""
    users_dict = load_users_db()
    
    if user_login.username not in users_dict:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    user_data = users_dict[user_login.username]
    
    if not verify_password(user_login.password, user_data["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_login.username},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
```

---

**Vị trí thêm:** Sửa endpoint `/submit` để yêu cầu token

Tìm dòng:
```python
@app.post("/submit", response_model=SubmissionResult)
async def submit_quiz(submission: SubmissionData):
```

Sửa thành:
```python
@app.post("/submit", response_model=SubmissionResult)
async def submit_quiz(
    submission: SubmissionData,
    current_user: dict = Depends(get_current_user)
):
```

---

**Vị trí thêm:** Cập nhật `requirements.txt`

Thêm 2 dòng này vào cuối file:
```
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
```

---

## 🎨 CODE LOGIN PHẦN FRONTEND

### Code thêm vào file `frontend/src/components/Login.jsx` (FILE MỚI)

Tạo file mới: `frontend/src/components/Login.jsx`

Dán toàn bộ code này:

```jsx
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../styles/Login.css'

function Login({ onLoginSuccess }) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isRegister, setIsRegister] = useState(false)
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')

  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      })

      const data = await response.json()

      if (!response.ok) {
        setError(data.detail || 'Đăng nhập thất bại')
        return
      }

      localStorage.setItem('access_token', data.access_token)
      localStorage.setItem('username', username)

      onLoginSuccess(username)
      navigate('/')
    } catch (err) {
      setError('Lỗi kết nối đến server')
    } finally {
      setIsLoading(false)
    }
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      const response = await fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          password,
          email,
          full_name: fullName,
        }),
      })

      const data = await response.json()

      if (!response.ok) {
        setError(data.detail || 'Đăng ký thất bại')
        return
      }

      localStorage.setItem('access_token', data.access_token)
      localStorage.setItem('username', username)

      onLoginSuccess(username)
      navigate('/')
    } catch (err) {
      setError('Lỗi kết nối đến server')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <h1>{isRegister ? 'Đăng Ký' : 'Đăng Nhập'}</h1>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={isRegister ? handleRegister : handleLogin}>
          <div className="form-group">
            <label>Tên đăng nhập</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Nhập tên đăng nhập"
              required
            />
          </div>

          {isRegister && (
            <>
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Nhập email"
                  required
                />
              </div>

              <div className="form-group">
                <label>Họ và tên</label>
                <input
                  type="text"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  placeholder="Nhập họ và tên"
                />
              </div>
            </>
          )}

          <div className="form-group">
            <label>Mật khẩu</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Nhập mật khẩu"
              required
            />
          </div>

          <button type="submit" disabled={isLoading} className="login-button">
            {isLoading ? 'Đang xử lý...' : isRegister ? 'Đăng Ký' : 'Đăng Nhập'}
          </button>
        </form>

        <p className="toggle-text">
          {isRegister ? 'Đã có tài khoản? ' : 'Chưa có tài khoản? '}
          <button
            type="button"
            onClick={() => {
              setIsRegister(!isRegister)
              setError('')
            }}
            className="toggle-button"
          >
            {isRegister ? 'Đăng nhập' : 'Đăng ký'}
          </button>
        </p>
      </div>
    </div>
  )
}

export default Login
```

---

### Code thêm vào file `frontend/src/styles/Login.css` (FILE MỚI)

Tạo folder: `frontend/src/styles/`

Tạo file: `frontend/src/styles/Login.css`

Dán toàn bộ code này:

```css
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
}

.login-card h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
  font-size: 28px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #555;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
}

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 12px;
  border-radius: 5px;
  margin-bottom: 20px;
  border-left: 4px solid #c33;
}

.login-button {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.login-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.login-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.toggle-text {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.toggle-button {
  background: none;
  border: none;
  color: #667eea;
  cursor: pointer;
  font-weight: 600;
  text-decoration: underline;
}

.toggle-button:hover {
  color: #764ba2;
}
```

---

### Cập nhật file `frontend/src/App.jsx`

**Vị trí cập nhật:** Thay thế toàn bộ import ở đầu file

Xóa dòng cũ:
```jsx
import { useState, useEffect } from 'react'
import Quiz from './components/Quiz'
import Results from './components/Results'
import './App.css'
```

Thay bằng:
```jsx
import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Quiz from './components/Quiz'
import Results from './components/Results'
import Login from './components/Login'
import './App.css'
```

---

**Vị trí cập nhật:** Thay thế hàm `App()` và return

Thay toàn bộ nội dung function `App()` bằng:

```jsx
function App() {
  const [user, setUser] = useState(null)
  const [questions, setQuestions] = useState([])
  const [started, setStarted] = useState(false)
  const [submitted, setSubmitted] = useState(false)
  const [answers, setAnswers] = useState({})
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const storedUser = localStorage.getItem('username')
    if (storedUser) {
      setUser(storedUser)
      fetchQuestions()
    }
  }, [])

  const fetchQuestions = async () => {
    try {
      const response = await fetch('http://localhost:8000/questions')
      const data = await response.json()
      setQuestions(data)
    } catch (error) {
      console.error('Error fetching questions:', error)
    }
  }

  const handleLoginSuccess = (username) => {
    setUser(username)
    fetchQuestions()
  }

  const handleLogout = () => {
    setUser(null)
    localStorage.removeItem('username')
    localStorage.removeItem('access_token')
    setStarted(false)
    setSubmitted(false)
    setAnswers({})
    setResults(null)
  }

  const handleStart = () => {
    setStarted(true)
    setSubmitted(false)
    setAnswers({})
    setResults(null)
  }

  const handleSelectAnswer = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }))
  }

  const handleSubmit = async () => {
    setLoading(true)
    try {
      const token = localStorage.getItem('access_token')
      const submissionData = {
        answers: Object.entries(answers).map(([questionId, selectedAnswer]) => ({
          question_id: parseInt(questionId),
          selected_answer: selectedAnswer
        }))
      }

      const response = await fetch('http://localhost:8000/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(submissionData)
      })

      const data = await response.json()
      if (response.ok) {
        setResults(data)
        setSubmitted(true)
      } else {
        alert('Lỗi khi nộp bài: ' + data.detail)
      }
    } catch (error) {
      console.error('Error submitting quiz:', error)
      alert('Lỗi kết nối đến server')
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setStarted(false)
    setSubmitted(false)
    setAnswers({})
    setResults(null)
  }

  return (
    <Router>
      <Routes>
        <Route
          path="/login"
          element={
            user ? <Navigate to="/" /> : <Login onLoginSuccess={handleLoginSuccess} />
          }
        />

        <Route
          path="/"
          element={
            !user ? (
              <Navigate to="/login" />
            ) : (
              <div className="app-container">
                <header className="app-header">
                  <h1>Quiz Application</h1>
                  <div className="user-info">
                    <span>Xin chào, {user}!</span>
                    <button onClick={handleLogout} className="logout-button">
                      Đăng Xuất
                    </button>
                  </div>
                </header>

                <main className="app-main">
                  {!started ? (
                    <div className="quiz-intro">
                      <h2>Welcome to Quiz Application</h2>
                      <p>Kiểm tra kiến thức của bạn với {questions.length} câu hỏi</p>
                      <button
                        onClick={handleStart}
                        className="start-button"
                        disabled={questions.length === 0}
                      >
                        Bắt Đầu Quiz
                      </button>
                    </div>
                  ) : !submitted ? (
                    <Quiz
                      questions={questions}
                      answers={answers}
                      onSelectAnswer={handleSelectAnswer}
                      onSubmit={handleSubmit}
                      loading={loading}
                    />
                  ) : (
                    <Results
                      results={results}
                      onReset={handleReset}
                    />
                  )}
                </main>
              </div>
            )
          }
        />
      </Routes>
    </Router>
  )
}

export default App
```

---

### Cập nhật file `frontend/package.json`

**Vị trí cập nhật:** Thay đổi phần `dependencies`

Tìm phần:
```json
"dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
  },
```

Sửa thành:
```json
"dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.17.0"
  },
```

---

### Cập nhật file `frontend/src/App.css`

**Vị trí cập nhật:** Thêm CSS vào cuối file

Thêm những dòng này vào cuối `App.css`:

```css
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.app-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.app-header h1 {
  margin: 0;
  font-size: 28px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-info span {
  font-size: 16px;
}

.logout-button {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid white;
  padding: 8px 16px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.logout-button:hover {
  background: white;
  color: #667eea;
}

.app-main {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: #f5f5f5;
}

.quiz-intro {
  text-align: center;
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.quiz-intro h2 {
  color: #333;
  font-size: 32px;
  margin-bottom: 10px;
}

.quiz-intro p {
  color: #666;
  font-size: 18px;
  margin-bottom: 30px;
}

.start-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 30px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  transition: transform 0.2s, box-shadow 0.2s;
}

.start-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.start-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
```

---

## 📋 TÓM TẮT CÔNG VIỆC

| Công việc | Loại | File |
|-----------|------|------|
| Thêm import + hàm helper | Thêm vào | `backend/main.py` |
| Thêm endpoints login/register | Thêm vào | `backend/main.py` |
| Sửa endpoint /submit thêm token | Sửa | `backend/main.py` |
| Cập nhật requirements | Thêm vào | `backend/requirements.txt` |
| Tạo Login component | Tạo mới | `frontend/src/components/Login.jsx` |
| Tạo Login CSS | Tạo mới | `frontend/src/styles/Login.css` |
| Sửa imports + function App | Sửa toàn bộ | `frontend/src/App.jsx` |
| Thêm react-router-dom | Sửa | `frontend/package.json` |
| Thêm CSS cho header | Thêm vào | `frontend/src/App.css` |

---

## 🚀 CHẠY LỆnh SETUP

```bash
# Backend
cd backend
pip install -r requirements.txt
python main.py

# Frontend (terminal mới)
cd frontend
npm install
npm run dev
```

Truy cập: `http://localhost:5173`
