# Quiz App - GK PTUD

Ứng dụng trắc nghiệm đơn giản xây dựng với React (Frontend) và FastAPI (Backend).

## Tính Năng

✅ Hiển thị danh sách câu hỏi  
✅ Cho người dùng chọn đáp án  
✅ Nộp bài tập  
✅ Tính điểm tự động  
✅ Hiển thị kết quả chi tiết (đúng/sai từng câu)  
✅ Xem đáp án đúng khi làm sai

## Cấu Trúc Dự Án

```
gk_ptud/
├── backend/
│   ├── main.py                 # FastAPI server
│   └── requirements.txt        # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.jsx            # Main component
    │   ├── App.css            # Main styles
    │   └── components/
    │       ├── Quiz.jsx       # Quiz display component
    │       ├── Quiz.css       # Quiz styles
    │       ├── Results.jsx    # Results display component
    │       └── Results.css    # Results styles
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Requirements

- **Backend**: Python 3.8+
- **Frontend**: Node.js 14+ và npm/yarn

## Cài Đặt

### 1. Backend Setup (FastAPI)

```bash
# Chuyển vào thư mục backend
cd backend

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy FastAPI server
python main.py
```

Backend sẽ chạy tại: `http://localhost:8000`

**API Endpoints:**
- `GET /questions` - Lấy danh sách câu hỏi
- `POST /submit` - Nộp đáp án và tính điểm
- `GET /` - Health check

### 2. Frontend Setup (React + Vite)

```bash
# Chuyển vào thư mục frontend
cd frontend

# Cài đặt dependencies
npm install

# Chạy development server
npm run dev
```

Frontend sẽ chạy tại: `http://localhost:5173` hoặc `http://localhost:3000`

## Cách Sử Dụng

1. Mở trình duyệt, truy cập frontend URL
2. Click nút "Bắt đầu làm bài"
3. Chọn đáp án cho mỗi câu hỏi
4. Click nút "Nộp bài" khi hoàn thành
5. Xem kết quả và chi tiết từng câu
6. Click "Làm lại" để làm bài lần khác

## Cấu Trúc Dữ Liệu

### Question Object
```json
{
  "id": 1,
  "question": "React là thư viện của ngôn ngữ nào?",
  "options": ["Python", "JavaScript", "Java", "C#"],
  "correct_answer": "JavaScript"
}
```

### Submission Data
```json
{
  "answers": [
    { "question_id": 1, "selected_answer": "JavaScript" },
    { "question_id": 2, "selected_answer": "Python 3.6+" }
  ]
}
```

### Result Response
```json
{
  "correct_count": 7,
  "total_questions": 8,
  "score": 8.75,
  "results": [
    {
      "question_id": 1,
      "question": "React là thư viện của ngôn ngữ nào?",
      "selected_answer": "JavaScript",
      "correct_answer": "JavaScript",
      "is_correct": true
    }
  ]
}
```

## Điểm Số

- **Tổng điểm**: 10 điểm
- **Mỗi câu đúng**: 10 / tổng_câu_hỏi điểm
- **Ví dụ**: 8 câu đúng / 8 tổng cộng = 10 điểm

## Ghi Chú

- Backend cần chạy trước khi dùng Frontend
- Frontend được cấu hình để kết nối tới Backend tại `http://localhost:8000`
- CORS được bật để cho phép Frontend (localhost:3000/5173) gọi Backend

## Troubleshooting

**Lỗi: "Cannot connect to backend"**
- Kiểm tra Backend có đang chạy không
- Kiểm tra port 8000 không bị chiếm
- Kiểm tra CORS configuration

**Lỗi: "Module not found"**
- Chạy `pip install -r requirements.txt` cho Backend
- Chạy `npm install` cho Frontend

## License

MIT
