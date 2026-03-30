# 📋 Quiz App - Hoàn Thành & Hướng Dẫn Sử Dụng

## ✅ Đã Hoàn Thành (Completed)

### Backend (FastAPI)
- ✅ `main.py` - API server với 3 endpoints
  - `GET /questions` - Lấy danh sách 8 câu hỏi
  - `POST /submit` - Chấm điểm và trả kết quả
  - `GET /` - Health check
- ✅ `requirements.txt` - Danh sách dependencies
- ✅ `.env.example` - Ví dụ cấu hình

### Frontend (React + Vite)
- ✅ `App.jsx` - Component chính quản lý state
- ✅ `Quiz.jsx` - Hiển thị câu hỏi và tùy chọn
- ✅ `Results.jsx` - Hiển thị kết quả chi tiết
- ✅ Tất cả CSS files (App.css, Quiz.css, Results.css)
- ✅ `main.jsx` - Entry point
- ✅ `index.html` - HTML template

### Tài Liệu & Script
- ✅ `README.md` - Tài liệu chính chi tiết
- ✅ `QUICK_START.md` - Hướng dẫn nhanh
- ✅ `run_windows.bat` - Script tự động (Windows)
- ✅ `run.sh` - Script tự động (Mac/Linux)
- ✅ `.gitignore` - Git ignore file

---

## 🚀 Cách Chạy (3 Cách)

### **Cách 1: Tự động (Bấm 1 lần) - KHUYÊN DÙNG**

**Windows:**
```
Double-click run_windows.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### **Cách 2: Dùng Terminal/CMD (Từng cái một)

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### **Cách 3: Dùng IDE**

**VS Code:**
1. Mở folder gk_ptud
2. Terminal > New Terminal
3. Chạy backend: `cd backend && pip install -r requirements.txt && python main.py`
4. Terminal > New Terminal
5. Chạy frontend: `cd frontend && npm install && npm run dev`

---

## 📍 URLs Sau Khi Chạy

| Ứng dụng | URL | Mô tả |
|---------|-----|-------|
| Frontend | http://localhost:5173 | Giao diện Quiz App |
| Backend | http://localhost:8000 | API Server |
| API Docs | http://localhost:8000/docs | Swagger UI |

---

## 📝 Câu Hỏi trong Database

Hiện có **8 câu hỏi** được cấu hình sẵn:

1. React là thư viện của ngôn ngữ nào? → **JavaScript**
2. FastAPI dùng Python version nào? → **Python 3.6+**
3. HTTP method nào dùng để lấy dữ liệu? → **GET**
4. CORS là viết tắt của gì? → **Cross-Origin Resource Sharing**
5. Component React cơ bản? → **Cả 2** (Functional & Class)
6. Hook nào quản lý state? → **useState**
7. RESTful API sử dụng methods? → **GET, POST, PUT, PATCH, DELETE**
8. JSON là viết tắt của gì? → **JavaScript Object Notation**

---

## 🎯 Tính Năng Chính

### ✨ Chức Năng Frontend
- 🖥️ Trang chào mừng với nút "Bắt đầu làm bài"
- 📊 Progress bar hiển thị tiến độ
- ✏️ Chọn đáp án bằng click button
- 📤 Nút "Nộp bài" để submit
- 🎓 Trang kết quả với:
  - 📈 Điểm số (0-10)
  - ✅ Số câu đúng/tổng
  - 📋 Chi tiết từng câu (đúng/sai)
  - 🔍 Xem đáp án đúng khi làm sai
  - 🔄 Nút "Làm lại" để restart

### 📡 Chức Năng Backend
- 🔄 CORS được bật (cho frontend)
- 📊 Tự động tính điểm (10 điểm / số câu)
- 🎯 Kiểm tra đáp án chính xác
- 📋 Trả về chi tiết từng câu

---

## 🔧 Cấu Hình & Tuỳ Chỉnh

### Thêm/Sửa Câu Hỏi
**File:** `backend/main.py`
- Tìm `QUESTIONS = [...]`
- Thêm/sửa dict câu hỏi
- Append vào list

### Thay Đổi Điểm Số
**File:** `backend/main.py` (dòng khoảng 130)
```python
score = round((correct_count / total_questions) * 10, 1)
# Sửa 10 thành số điểm tối đa mong muốn
```

### Thay Đổi Port
**Backend:** `main.py` dòng 146
```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # Đổi port ở đây
```

**Frontend:** Sửa trong `fetch('http://localhost:8000/...`

---

## 🧪 Test API bằng Swagger UI

1. Chạy backend: `python main.py`
2. Mở: http://localhost:8000/docs
3. Test các endpoint trực tiếp trong UI

---

## ❌ Troubleshooting

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-----------|----------|
| "Address already in use" | Port bị dùng | Kill process hoặc đổi port |
| "Cannot connect to backend" | Backend không chạy | Kiểm tra Terminal 1 |
| "Module not found (Python)" | Chưa cài pip packages | `pip install -r requirements.txt` |
| "Module not found (npm)" | Chưa cài npm packages | `npm install` |
| CORS Error | Frontend blocked bởi Backend | Kiểm tra CORS config |
| "Port 3000/5173 not available" | Vite port conflict | Vite sẽ tự dùng port khác |

---

## 📦 Dependencies

### Backend
- fastapi==0.104.1
- uvicorn==0.24.0
- pydantic==2.5.0
- python-multipart==0.0.6

### Frontend
- react@^18.2.0
- react-dom@^18.2.0
- vite@^5.0.8
- @vitejs/plugin-react@^4.2.1

---

## 🎨 Styling

- **Gradient backgrounds** - Purple/Blue gradient
- **Responsive design** - Tự động fit màn hình
- **Color coding** - Green (đúng), Red (sai), Blue (selected)
- **Smooth animations** - Button hover effects, transitions

---

## 🔐 Security Notes

- ✅ CORS được setup để chỉ allow localhost
- ✅ Input validation qua Pydantic
- ✅ No sensitive data stored locally

---

## 📚 File Structure Sơ Lược

```
gk_ptud/
├── backend/
│   ├── main.py              // FastAPI app
│   ├── requirements.txt     // Python deps
│   └── .env.example         // Config example
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx          // Main component + logic
│   │   ├── App.css          // Main styles
│   │   ├── main.jsx         // Entry point
│   │   └── components/
│   │       ├── Quiz.jsx     // Quiz display
│   │       ├── Quiz.css
│   │       ├── Results.jsx  // Results display
│   │       └── Results.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── README.md                // Tài liệu chi tiết
├── QUICK_START.md           // Hướng dẫn nhanh
├── SETUP.md                 // File này
├── .gitignore
├── run_windows.bat          // Auto run (Windows)
└── run.sh                   // Auto run (Mac/Linux)
```

---

## ✅ Checklist Trước Khi Submit

- [ ] Backend chạy không lỗi
- [ ] Frontend chạy không lỗi
- [ ] có thể làm quiz từ đầu đến cuối
- [ ] Điểm được tính đúng
- [ ] Kết quả hiển thị đúng
- [ ] Nút "Làm lại" hoạt động
- [ ] Responsive trên các màn hình khác nhau

---

## 🎓 Learned Concepts

- FastAPI REST API setup
- React state management (useState)
- React component composition
- Frontend-Backend integration
- CORS handling
- Fetch API usage
- Vite development setup
- Pydantic data validation

---

## 📞 Support

Nếu gặp vấn đề:
1. Kiểm tra terminal có error message
2. Đọc lại QUICK_START.md
3. Kiểm tra port không bị dùng
4. Restart cả backend & frontend

**Chúc bạn thành công! 🎉**
