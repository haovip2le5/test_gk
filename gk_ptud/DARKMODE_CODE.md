# Hướng Dẫn Thêm Chức Năng Dark Mode

---

## 🌙 CODE DARK MODE

### Cập nhật file `frontend/src/App.jsx`

**Vị trí cập nhật:** Thêm state cho dark mode

Tìm dòng:
```jsx
const [user, setUser] = useState(null)
const [questions, setQuestions] = useState([])
```

Thêm dòng này ngay sau:
```jsx
const [darkMode, setDarkMode] = useState(false)
```

---

**Vị trí cập nhật:** Thêm hàm toggle dark mode

Thêm hàm này trước hàm `handleStart`:
```jsx
const handleToggleDarkMode = () => {
  setDarkMode(!darkMode)
  localStorage.setItem('darkMode', (!darkMode).toString())
}
```

---

**Vị trí cập nhật:** Khôi phục dark mode khi load trang

Tìm dòng:
```jsx
useEffect(() => {
  const storedUser = localStorage.getItem('username')
  if (storedUser) {
    setUser(storedUser)
    fetchQuestions()
  }
}, [])
```

Thay bằng:
```jsx
useEffect(() => {
  const storedUser = localStorage.getItem('username')
  if (storedUser) {
    setUser(storedUser)
    fetchQuestions()
  }

  const storedDarkMode = localStorage.getItem('darkMode')
  if (storedDarkMode === 'true') {
    setDarkMode(true)
  }
}, [])
```

---

**Vị trí cập nhật:** Thêm class dark mode vào container

Tìm dòng:
```jsx
<div className="app-container">
```

Sửa thành:
```jsx
<div className="app-container" style={{ background: darkMode ? '#1a1a1a' : '#fff' }}>
```

---

**Vị trí cập nhật:** Thêm nút toggle dark mode vào header

Tìm phần:
```jsx
<header className="app-header">
  <h1>Quiz Application</h1>
  <div className="user-info">
    <span>Xin chào, {user}!</span>
    <button onClick={handleLogout} className="logout-button">
      Đăng Xuất
    </button>
  </div>
</header>
```

Sửa thành:
```jsx
<header className={`app-header ${darkMode ? 'dark' : ''}`}>
  <h1>Quiz Application</h1>
  <div className="user-info">
    <span>Xin chào, {user}!</span>
    <button onClick={handleToggleDarkMode} className="theme-button" title="Toggle Dark Mode">
      {darkMode ? '☀️' : '🌙'}
    </button>
    <button onClick={handleLogout} className="logout-button">
      Đăng Xuất
    </button>
  </div>
</header>
```

---

**Vị trí cập nhật:** Thêm class dark mode cho main content

Tìm dòng:
```jsx
<main className="app-main">
```

Sửa thành:
```jsx
<main className={`app-main ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Thêm class dark mode cho quiz intro

Tìm dòng:
```jsx
<div className="quiz-intro">
```

Sửa thành:
```jsx
<div className={`quiz-intro ${darkMode ? 'dark' : ''}`}>
```

---

### Cập nhật file `frontend/src/App.css`

**Vị trí cập nhật:** Thêm CSS cho dark mode vào cuối file

Thêm những dòng này:

```css
/* ===== DARK MODE ===== */
.theme-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  margin-right: 10px;
  transition: transform 0.3s;
}

.theme-button:hover {
  transform: scale(1.2);
}

.app-header.dark {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}

.app-main.dark {
  background: #0f0f0f;
}

.quiz-intro.dark {
  background: #1a1a1a;
  color: #fff;
}

.quiz-intro.dark h2 {
  color: #fff;
}

.quiz-intro.dark p {
  color: #ccc;
}

/* Dark mode Quiz Component */
.question.dark {
  background: #1a1a1a;
  border: 1px solid #333;
}

.question.dark h3 {
  color: #fff;
}

.option.dark {
  background: #2a2a2a;
  border: 1px solid #444;
  color: #fff;
}

.option.dark:hover {
  border-color: #667eea;
}

.option.dark input[type="radio"] {
  accent-color: #667eea;
}

/* Dark mode Results Component */
.results-container.dark {
  background: #1a1a1a;
}

.results-container.dark h2 {
  color: #fff;
}

.results-summary.dark {
  background: #2a2a2a;
  color: #fff;
}

.result-item.dark {
  background: #2a2a2a;
  border-left: 4px solid #667eea;
}

.result-item.dark h4 {
  color: #fff;
}

.result-item.dark p {
  color: #ccc;
}

.result-item.correct.dark {
  border-left: 4px solid #4caf50;
}

.result-item.wrong.dark {
  border-left: 4px solid #f44336;
}
```

---

### Cập nhật file `frontend/src/components/Quiz.jsx`

**Vị trí cập nhật:** Thêm prop dark mode

Tìm dòng:
```jsx
function Quiz({ questions, answers, onSelectAnswer, onSubmit, loading }) {
```

Sửa thành:
```jsx
function Quiz({ questions, answers, onSelectAnswer, onSubmit, loading, darkMode }) {
```

---

**Vị trị cập nhật:** Sửa className của question container

Tìm dòng:
```jsx
<div className="question">
```

Sửa thành:
```jsx
<div className={`question ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Sửa className của option input

Tìm dòng:
```jsx
<div className="option">
```

Sửa thành:
```jsx
<div className={`option ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Truyền prop darkMode vào Quiz component

Tìm dòng:
```jsx
<Quiz
  questions={questions}
  answers={answers}
  onSelectAnswer={handleSelectAnswer}
  onSubmit={handleSubmit}
  loading={loading}
/>
```

Sửa thành:
```jsx
<Quiz
  questions={questions}
  answers={answers}
  onSelectAnswer={handleSelectAnswer}
  onSubmit={handleSubmit}
  loading={loading}
  darkMode={darkMode}
/>
```

---

### Cập nhật file `frontend/src/components/Results.jsx`

**Vị trí cập nhật:** Thêm prop dark mode

Tìm dòng:
```jsx
function Results({ results, onReset }) {
```

Sửa thành:
```jsx
function Results({ results, onReset, darkMode }) {
```

---

**Vị trí cập nhật:** Sửa className của results container

Tìm dòng:
```jsx
<div className="results-container">
```

Sửa thành:
```jsx
<div className={`results-container ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Sửa className của results summary

Tìm dòng:
```jsx
<div className="results-summary">
```

Sửa thành:
```jsx
<div className={`results-summary ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Sửa className của result item

Tìm dòng (sẽ có nhiều dòng tương tự):
```jsx
<div className="result-item">
```

Sửa mỗi dòng thành:
```jsx
<div className={`result-item ${result.is_correct ? 'correct' : 'wrong'} ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Truyền prop darkMode vào Results component

Tìm dòng:
```jsx
<Results
  results={results}
  onReset={handleReset}
/>
```

Sửa thành:
```jsx
<Results
  results={results}
  onReset={handleReset}
  darkMode={darkMode}
/>
```

---

### Cập nhật file `frontend/src/styles/Login.css`

**Vị trí cập nhật:** Thêm CSS dark mode cho Login vào cuối file

Thêm những dòng này:

```css
/* Dark mode for Login */
.login-container.dark {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}

.login-card.dark {
  background: #1a1a1a;
}

.login-card.dark h1 {
  color: #fff;
}

.login-card.dark .form-group label {
  color: #ccc;
}

.login-card.dark .form-group input {
  background: #2a2a2a;
  border: 1px solid #444;
  color: #fff;
}

.login-card.dark .form-group input:focus {
  border-color: #667eea;
}

.login-card.dark .error-message {
  background-color: #3a2a2a;
  color: #ff6b6b;
}

.login-card.dark .toggle-text {
  color: #ccc;
}
```

---

**Vị trí cập nhật:** Thêm logic dark mode detect cho Login component

Mở file `frontend/src/components/Login.jsx`

Tìm dòng:
```jsx
function Login({ onLoginSuccess }) {
```

Sửa thành:
```jsx
function Login({ onLoginSuccess }) {
  const [darkMode, setDarkMode] = useState(false)

  useEffect(() => {
    const storedDarkMode = localStorage.getItem('darkMode')
    if (storedDarkMode === 'true') {
      setDarkMode(true)
    }
  }, [])
```

---

**Vị trí cập nhật:** Import useEffect vào Login

Tìm dòng:
```jsx
import { useState } from 'react'
```

Sửa thành:
```jsx
import { useState, useEffect } from 'react'
```

---

**Vị trí cập nhật:** Thêm class dark mode cho login container

Tìm dòng:
```jsx
<div className="login-container">
```

Sửa thành:
```jsx
<div className={`login-container ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Thêm class dark mode cho login card

Tìm dòng:
```jsx
<div className="login-card">
```

Sửa thành:
```jsx
<div className={`login-card ${darkMode ? 'dark' : ''}`}>
```

---

**Vị trí cập nhật:** Thêm nút toggle dark mode trên trang Login

Tìm dòng:
```jsx
<h1>{isRegister ? 'Đăng Ký' : 'Đăng Nhập'}</h1>
```

Sửa thành:
```jsx
<div className="login-header">
  <h1>{isRegister ? 'Đăng Ký' : 'Đăng Nhập'}</h1>
  <button
    type="button"
    onClick={() => setDarkMode(!darkMode)}
    className="login-theme-button"
    title="Toggle Dark Mode"
  >
    {darkMode ? '☀️' : '🌙'}
  </button>
</div>
```

---

**Vị trí cập nhật:** Thêm CSS cho login header

Thêm vào `frontend/src/styles/Login.css`:

```css
.login-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.login-header h1 {
  margin: 0;
  flex: 1;
}

.login-theme-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  padding: 0;
  transition: transform 0.3s;
}

.login-theme-button:hover {
  transform: scale(1.2);
}
```

---

## 📋 TÓM TẮT CÔNG VIỆC DARK MODE

| Công việc | Loại | File |
|-----------|------|------|
| Thêm state darkMode | Thêm | `App.jsx` |
| Thêm hàm toggle dark mode | Thêm | `App.jsx` |
| Khôi phục dark mode từ localStorage | Sửa | `App.jsx` |
| Thêm class dark mode vào containers | Sửa | `App.jsx` |
| Thêm nút toggle dark mode | Sửa | `App.jsx` |
| Truyền darkMode prop tới Quiz | Sửa | `App.jsx` |
| Truyền darkMode prop tới Results | Sửa | `App.jsx` |
| Thêm CSS dark mode | Thêm vào cuối | `App.css` |
| Thêm prop darkMode vào Quiz | Sửa | `Quiz.jsx` |
| Thêm class dark mode vào Quiz | Sửa | `Quiz.jsx` |
| Thêm prop darkMode vào Results | Sửa | `Results.jsx` |
| Thêm class dark mode vào Results | Sửa | `Results.jsx` |
| Thêm CSS dark mode cho Login | Thêm vào cuối | `Login.css` |
| Thêm dark mode logic vào Login | Sửa | `Login.jsx` |
| Thêm nút toggle dark mode trên Login | Sửa | `Login.jsx` |
| Thêm CSS cho login header | Thêm vào | `Login.css` |

---

## ✨ TÍNH NĂNG DARK MODE

✅ Tự động lưu lựa chọn dark mode vào localStorage  
✅ Khôi phục dark mode khi reload trang  
✅ Nút toggle 🌙/☀️ trên header  
✅ Dark mode áp dụng cho tất cả components  
✅ Màu sắc hài hòa cho dark mode  
✅ Hiệu ứng smooth transition  

---

## 🎨 MÀU SẮC DARK MODE

| Phần tử | Light | Dark |
|---------|-------|------|
| Background | #ffffff | #1a1a1a |
| Container | #f5f5f5 | #0f0f0f |
| Header | Linear gradient | #1a1a2e |
| Card | #ffffff | #2a2a2a |
| Text | #333 | #ffffff |
| Accent | #667eea | #667eea |

---

## 🚀 KIỂM THỬ DARK MODE

1. Reload trang, dark mode sẽ bắt đầu bằng light mode
2. Click nút 🌙 để bật dark mode
3. Reload trang, dark mode sẽ được khôi phục
4. Dark mode áp dụng cho tất cả trang (Login, Quiz, Results)
