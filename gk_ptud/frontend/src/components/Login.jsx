import { useState } from 'react'
import '../styles/Login.css'

// ===== NEWLY ADDED - LOGIN COMPONENT =====
function Login({ onLoginSuccess, darkMode }) {
  const [isRegister, setIsRegister] = useState(false)
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    confirmPassword: ''
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const endpoint = isRegister ? '/register' : '/login'
      const body = isRegister
        ? {
            username: formData.username,
            password: formData.password,
            confirmPassword: formData.confirmPassword
          }
        : {
            username: formData.username,
            password: formData.password
          }

      const response = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      })

      const data = await response.json()

      if (data.success) {
        onLoginSuccess({
          username: formData.username,
          role: data.user?.role || 'user'
        })
      } else {
        setError(data.message || 'An error occurred')
      }
    } catch (error) {
      console.error('Error:', error)
      setError('Failed to connect to server')
    } finally {
      setLoading(false)
    }
  }

  const toggleMode = () => {
    setIsRegister(!isRegister)
    setError('')
    setFormData({
      username: '',
      password: '',
      confirmPassword: ''
    })
  }

  return (
    <div className={`login-container ${darkMode ? 'dark' : ''}`}>
      <div className="login-box">
        <h2>{isRegister ? 'Đăng ký' : 'Đăng nhập'}</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Tên đăng nhập</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              placeholder="Nhập tên đăng nhập"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Mật khẩu</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              placeholder="Nhập mật khẩu"
              required
            />
          </div>

          {isRegister && (
            <div className="form-group">
              <label htmlFor="confirmPassword">Xác nhận mật khẩu</label>
              <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleInputChange}
                placeholder="Xác nhận mật khẩu"
                required
              />
            </div>
          )}

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? 'Đang xử lý...' : (isRegister ? 'Đăng ký' : 'Đăng nhập')}
          </button>
        </form>

        <p className="toggle-text">
          {isRegister ? 'Đã có tài khoản? ' : 'Chưa có tài khoản? '}
          <button type="button" className="toggle-btn" onClick={toggleMode}>
            {isRegister ? 'Đăng nhập' : 'Đăng ký'}
          </button>
        </p>

        <div className="demo-credentials">
          <p><strong>Demo Accounts:</strong></p>
          <p>👤 User: user1 / Pass: pass123</p>
          <p>👤 User: user2 / Pass: pass123</p>
          <p>👮 Admin: admin / Pass: pass123</p>
        </div>
      </div>
    </div>
  )
}

export default Login
// ===== NEWLY ADDED - LOGIN COMPONENT ENDS =====
