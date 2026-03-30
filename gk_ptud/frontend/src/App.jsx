import { useState, useEffect } from 'react'
import Quiz from './components/Quiz'
import Results from './components/Results'
import './App.css'

function App() {
  const [questions, setQuestions] = useState([])
  const [started, setStarted] = useState(false)
  const [submitted, setSubmitted] = useState(false)
  const [answers, setAnswers] = useState({})
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  // ===== NEWLY ADDED - DARK MODE =====
  const [darkMode, setDarkMode] = useState(false)

  useEffect(() => {
    fetchQuestions()

    // ===== NEWLY ADDED - RESTORE DARK MODE =====
    const storedDarkMode = localStorage.getItem('darkMode')
    if (storedDarkMode === 'true') {
      setDarkMode(true)
    }
  }, [])

  // ===== NEWLY ADDED - Apply dark mode to body =====
  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark-mode')
    } else {
      document.body.classList.remove('dark-mode')
    }
  }, [darkMode])

  const fetchQuestions = async () => {
    try {
      const response = await fetch('http://localhost:8000/questions')
      const data = await response.json()
      setQuestions(data)
    } catch (error) {
       console.error('Error fetching questions:', error)
    }
  }

  const handleToggleDarkMode = () => {
    setDarkMode(!darkMode)
    localStorage.setItem('darkMode', (!darkMode).toString())
  }

  // ===== NEWLY ADDED - DARK MODE FUNCTION ENDS =====
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
      const submissionData = {
        answers: Object.entries(answers).map(([questionId, selectedAnswer]) => ({
          question_id: parseInt(questionId),
          selected_answer: selectedAnswer
        }))
      }

      const response = await fetch('http://localhost:8000/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(submissionData)
      })

      const data = await response.json()
      setResults(data)
      setSubmitted(true)
    } catch (error) {
      console.error('Error submitting answers:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleRestart = () => {
    setStarted(false)
    setSubmitted(false)
    setAnswers({})
    setResults(null)
  }

  return (
    // ===== NEWLY ADDED - DARK MODE CONTAINER =====
    <div className="app">
      {/* ===== NEWLY ADDED - DARK MODE HEADER =====*/}
      <div className="app-header">
        <h1>Quiz App</h1>
        <button onClick={handleToggleDarkMode} className="theme-button" title="Toggle Dark Mode">
          {darkMode ? '☀️' : '🌙'}
        </button>
      </div>

      {!started && !submitted && (
        // ===== NEWLY ADDED - DARK MODE CLASS =====
        <div className={`start-screen ${darkMode ? 'dark' : ''}`}>
              <p>Chao mung ban den voi bai trac nghiem!</p>
              <p>Bai quiz gom {questions.length} cau hoi.</p>
              <button className="start-btn" onClick={handleStart}>
                Bat dau lam bai
              </button>
            </div>
          )}

          {/* ===== NEWLY ADDED - darkMode PROP ===== */}
          {started && !submitted && (
            <Quiz
              questions={questions}
              answers={answers}
              onSelectAnswer={handleSelectAnswer}
              onSubmit={handleSubmit}
              loading={loading}
              darkMode={darkMode}
            />
          )}

          {/* ===== NEWLY ADDED - darkMode PROP ===== */}
          {submitted && results && (
            <Results
              results={results}
              onRestart={handleRestart}
              darkMode={darkMode}
            />
          )}
        </div>
      )
    }

export default App
