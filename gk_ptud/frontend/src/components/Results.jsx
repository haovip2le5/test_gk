import './Results.css'

// ===== NEWLY ADDED - darkMode PROP =====
function Results({ results, onRestart, darkMode }) {
  const { correct_count, total_questions, score, results: questionResults } = results

  const getScoreColor = () => {
    if (score >= 8) return '#27ae60'
    if (score >= 5) return '#f39c12'
    return '#e74c3c'
  }

  {/* ===== NEWLY ADDED - darkMode CLASSES ===== */}
  return (
    <div className={`results ${darkMode ? 'dark' : ''}`}>
      <div className={`score-summary ${darkMode ? 'dark' : ''}`}>
        <h2>Kết quả</h2>
        <div className="score-circle" style={{ borderColor: getScoreColor() }}>
          <span className="score-number" style={{ color: getScoreColor() }}>
            {score}
          </span>
          <span className="score-label">điểm</span>
        </div>
        <p className="correct-count">
          Số câu đúng: <strong>{correct_count}/{total_questions}</strong>
        </p>
      </div>

      <div className={`results-detail ${darkMode ? 'dark' : ''}`}>
        <h3>Chi tiết từng câu:</h3>
        {/* ===== NEWLY ADDED - darkMode CLASS ===== */}
        {questionResults.map((result, index) => (
          <div
            key={result.question_id}
            className={`result-item ${result.is_correct ? 'correct' : 'incorrect'} ${darkMode ? 'dark' : ''}`}
          >
            <div className="result-header">
              <span className="result-icon">
                {result.is_correct ? '✓' : '✗'}
              </span>
              <span className="result-question">
                Câu {index + 1}: {result.question}
              </span>
            </div>
            <div className="result-answers">
              <p>
                <span className="label">Bạn chọn:</span>
                <span className={result.is_correct ? 'answer-correct' : 'answer-wrong'}>
                  {result.selected_answer}
                </span>
              </p>
              {!result.is_correct && (
                <p>
                  <span className="label">Đáp án đúng:</span>
                  <span className="answer-correct">{result.correct_answer}</span>
                </p>
              )}
            </div>
          </div>
        ))}
      </div>

      <button className="btn-restart" onClick={onRestart}>
        Làm lại
      </button>
    </div>
  )
}

export default Results
