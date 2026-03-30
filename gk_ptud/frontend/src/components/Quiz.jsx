import './Quiz.css'

// ===== NEWLY ADDED - darkMode PROP =====
function Quiz({ questions, answers, onSelectAnswer, onSubmit, loading, darkMode }) {
  const answeredCount = Object.keys(answers).length

  return (
    <div className="quiz-container">
      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${(answeredCount / questions.length) * 100}%` }}
        />
      </div>
      <p className="progress-text">
        Da tra loi: {answeredCount}/{questions.length}
      </p>

      <div className="questions-list">
        {/* ===== NEWLY ADDED - darkMode CLASS ===== */}
        {questions.map((question, index) => (
          <div key={question.id} className={`question-card ${darkMode ? 'dark' : ''}`}>
            <h3>Cau {index + 1}: {question.question}</h3>
            <div className="options">
              {/* ===== NEWLY ADDED - darkMode CLASS ===== */}
              {question.options.map((option, optIndex) => (
                <button
                  key={optIndex}
                  className={`option-btn ${answers[question.id] === option ? 'selected' : ''} ${darkMode ? 'dark' : ''}`}
                  onClick={() => onSelectAnswer(question.id, option)}
                >
                  {String.fromCharCode(65 + optIndex)}. {option}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      <button
        className="submit-btn"
        onClick={onSubmit}
        disabled={loading || answeredCount === 0}
      >
        {loading ? 'Dang cham diem...' : 'Nop bai'}
      </button>
    </div>
  )
}

export default Quiz
