# HƯỚNG DẪN CHẠY QUIZ APP

## Cách 1: Chạy tự động (Tất cả hệ điều hành)

### Windows:
```bash
run_windows.bat
```
Hoặc double-click file `run_windows.bat`

### Mac/Linux:
```bash
chmod +x run.sh
./run.sh
```

---

## Cách 2: Chạy thủ công

### Bước 1: Cài đặt Python và Node.js
- Tải Python 3.8+ từ https://www.python.org
- Tải Node.js từ https://nodejs.org

### Bước 2: Mở 2 Terminal/Command Prompt

**Terminal 1 - Chạy Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
```

Sẽ nhìn thấy:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Chạy Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Sẽ nhìn thấy:
```
Local:   http://localhost:5173
```

### Bước 3: Mở trình duyệt
- Nhập URL: `http://localhost:5173`
- Hoặc click link từ terminal

---

## Kiểm Tra Hoạt Động

1. **Kiểm tra Backend**: https://localhost:8000/docs
   - Sẽ thấy Swagger UI với các API endpoints

2. **Kiểm tra Frontend**: http://localhost:5173
   - Sẽ thấy trang Quiz App

3. **Làm bài:**
   - Click "Bắt đầu làm bài"
   - Chọn đáp án cho các câu hỏi
   - Click "Nộp bài"
   - Xem kết quả

---

## Lỗi Thường Gặp & Cách Khắc Phục

### Lỗi: "Address already in use" (Port 8000 / 5173)
**Nguyên nhân**: Port đã bị dùng bởi ứng dụng khác
**Giải pháp**: 
- Đóng các ứng dụng khác sử dụng port đó
- Hoặc đổi port trong file config

### Lỗi: "Cannot connect to backend"
**Nguyên nhân**: Backend không chạy
**Giải pháp**:
- Kiểm tra Backend có hiển thị "Uvicorn running on..." không
- Restart Backend

### Lỗi: "Module not found"
**Nguyên nhân**: Dependencies chưa cài
**Giải pháp**:
- Backend: `pip install -r requirements.txt`
- Frontend: `npm install`

### Lỗi: CORS Error
**Nguyên nhân**: Frontend không được phép gọi Backend
**Giải pháp**: 
- Kiểm tra Backend CORS setting (đã include http://localhost:5173)
- Restart Backend

---

## Cấu Trúc Thư Mục

```
gk_ptud/
├── backend/                    # FastAPI Server
│   ├── main.py                # Main application
│   └── requirements.txt       # Dependencies
│
├── frontend/                   # React App
│   ├── src/
│   │   ├── App.jsx            
│   │   └── components/
│   │       ├── Quiz.jsx
│   │       └── Results.jsx
│   ├── package.json
│   └── vite.config.js
│
├── README.md                   # Tài liệu chính
├── QUICK_START.md             # File này
├── run_windows.bat            # Auto-start (Windows)
└── run.sh                      # Auto-start (Mac/Linux)
```

---

## API Endpoints

| Method | Endpoint | Mô Tả |
|--------|----------|-------|
| GET | `/questions` | Lấy danh sách câu hỏi |
| POST | `/submit` | Nộp đáp án & tính điểm |
| GET | `/` | Health check |

---

## Thông Tin Thêm

- **Backend**: FastAPI + Uvicorn
- **Frontend**: React 18 + Vite
- **Styling**: CSS (no framework)
- **API Communication**: Fetch API

Chúc bạn thành công! 🎓
