import { useState, useEffect } from 'react'
import '../styles/AdminDashboard.css'

// ===== NEWLY ADDED - ADMIN DASHBOARD COMPONENT =====
function AdminDashboard({ darkMode, onLogout }) {
  const [statistics, setStatistics] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    loadStatistics()
  }, [])

  const loadStatistics = async () => {
    setLoading(true)
    try {
      const response = await fetch('http://localhost:8000/admin/statistics')
      const data = await response.json()
      setStatistics(data)
    } catch (err) {
      console.error('Error loading statistics:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className={`admin-container ${darkMode ? 'dark' : ''}`}>
      <div className="admin-header">
        <h1>Admin Dashboard</h1>
        <button className="logout-btn" onClick={onLogout}>
          Logout
        </button>
      </div>

      {loading && <div className="loading">Loading...</div>}

      {statistics && (
        <div className="dashboard">
          <div className="stats-row">
            <div className="stat-box">
              <div className="stat-number">{statistics.total_users}</div>
              <div className="stat-name">Total Users</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{statistics.total_submissions}</div>
              <div className="stat-name">Total Submissions</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{statistics.average_score?.toFixed(1) || '0'}</div>
              <div className="stat-name">Average Score</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{statistics.highest_score || '0'}</div>
              <div className="stat-name">Highest Score</div>
            </div>
          </div>

          {statistics.recent_submissions?.length > 0 && (
            <div className="recent">
              <h3>Bài đã nộp gần đây</h3>
              <div className="submission-list">
                {statistics.recent_submissions.map((sub, idx) => (
                  <div key={idx} className="submission-item">
                    <span className="username">{sub.username}</span>
                    <span className="score">Điểm: {sub.score}/10</span>
                    <span className="time">{sub.timestamp}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {statistics.user_statistics && statistics.user_statistics.length > 0 && (
            <div className="user-stats">
              <h3>Thống kê theo user</h3>
              <table className="users-table">
                <thead>
                  <tr>
                    <th>Tên đăng nhập</th>
                    <th>Số lần nộp</th>
                    <th>Điểm trung bình</th>
                  </tr>
                </thead>
                <tbody>
                  {statistics.user_statistics.map(user => (
                    <tr key={user.username}>
                      <td>{user.username}</td>
                      <td>{user.submission_count}</td>
                      <td>{user.average_score?.toFixed(2) || '-'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default AdminDashboard
// ===== NEWLY ADDED - ADMIN DASHBOARD COMPONENT ENDS =====
