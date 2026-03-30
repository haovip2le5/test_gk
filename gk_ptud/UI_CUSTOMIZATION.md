# Hướng Dẫn Tùy Chỉnh Giao Diện Quiz App

## Mục Lục
1. [Cấu Trúc File CSS](#cấu-trúc-file-css)
2. [Tùy Chỉnh Màu Sắc](#tùy-chỉnh-màu-sắc)
3. [Tùy Chỉnh Bố Cục & Vị Trí](#tùy-chỉnh-bố-cục--vị-trí)
4. [Tùy Chỉnh Kích Thước & Spacing](#tùy-chỉnh-kích-thước--spacing)
5. [Các Ví Dụ Thực Tế](#các-ví-dụ-thực-tế)

---

## Cấu Trúc File CSS

```
frontend/src/
├── App.css                          # Giao diện chính (header, start screen)
├── components/
│   ├── Quiz.css                     # Quiz interface
│   ├── Results.css                  # Kết quả quiz
│   ├── Login.css                    # Form đăng nhập
│   └── AdminDashboard.css           # Bảng điều khiển admin
└── styles/
    ├── Login.css                    # CSS Login (nếu có)
    └── AdminDashboard.css           # CSS Admin (nếu có)
```

---

## Tùy Chỉnh Màu Sắc

### 1. Thay Đổi Màu Nền Chính

**File:** `App.css`

```css
body {
  background: #f0f0f0;              /* Thay đổi màu nền */
}

body.dark-mode {
  background: #1a1a1a;              /* Thay đổi màu nền dark mode */
}
```

**Các Màu Thường Dùng:**
- Xám nhạt: `#f0f0f0`, `#f5f5f5`
- Xám đậm: `#333`, `#444`, `#555`
- Đen: `#1a1a1a`, `#0f0f0f`
- Trắng: `#fff`, `#ffffff`

### 2. Thay Đổi Màu Button

**File:** `App.css`

```css
.start-btn {
  background: #333;                  /* Màu nền button */
  color: white;                      /* Màu text */
}

.start-btn:hover {
  background: #555;                  /* Màu khi hover */
}
```

### 3. Thay Đổi Màu Chữ

```css
h1 {
  color: #333;                       /* Màu heading chính */
}

body.dark-mode h1 {
  color: #fff;                       /* Màu heading dark mode */
}

p {
  color: #666;                       /* Màu text thường */
}

body.dark-mode p {
  color: #ccc;                       /* Màu text dark mode */
}
```

---

## Tùy Chỉnh Bố Cục & Vị Trí

### 1. Canh Giữa Nội Dung

**Canh giữa theo chiều ngang:**
```css
.container {
  margin: 0 auto;                    /* Tự động canh giữa */
  max-width: 800px;                  /* Giới hạn chiều rộng */
}
```

**Canh giữa theo chiều dọc:**
```css
.flex-center {
  display: flex;
  justify-content: center;           /* Canh giữa ngang */
  align-items: center;               /* Canh giữa dọc */
  min-height: 100vh;                 /* Chiều cao toàn màn hình */
}
```

### 2. Tùy Chỉnh Layout Header

**File:** `App.css`

```css
.app-header {
  display: flex;
  justify-content: space-between;    /* Phân tán các phần tử */
  align-items: center;               /* Canh giữa dọc */
  margin-bottom: 20px;               /* Khoảng cách dưới */
  gap: 15px;                         /* Khoảng cách giữa các item */
}

/* Để các item ở bên phải: */
.header-right {
  display: flex;
  gap: 10px;                         /* Khoảng cách giữa buttons */
  margin-left: auto;                 /* Đẩy sang phải */
}
```

### 3. Tùy Chỉnh Layout Grid (Thống Kê)

**File:** `components/AdminDashboard.css`

```css
.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* 4 cột bằng nhau */
  gap: 15px;                               /* Khoảng cách giữa các box */
}

/* Hoặc responsive: */
.stats-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}
```

### 4. Tùy Chỉnh Layout Flex (Quiz)

**File:** `components/Quiz.css`

```css
.questions-list {
  display: flex;
  flex-direction: column;            /* Xếp theo chiều dọc */
  gap: 15px;                         /* Khoảng cách giữa câu hỏi */
}

.options {
  display: flex;
  flex-direction: column;            /* Xếp buttons theo chiều dọc */
  gap: 8px;                          /* Khoảng cách giữa buttons */
}

/* Nếu muốn xếp ngang: */
.options {
  flex-direction: row;               /* Xếp theo chiều ngang */
  flex-wrap: wrap;                   /* Tự động xuống dòng */
}
```

---

## Tùy Chỉnh Kích Thước & Spacing

### 1. Padding (Khoảng Cách Trong)

```css
.container {
  padding: 20px;                     /* Áp dụng cho 4 cạnh */
  /* Hoặc chi tiết hơn: */
  padding-top: 20px;
  padding-right: 15px;
  padding-bottom: 20px;
  padding-left: 15px;
}
```

**Giá Trị Thường Dùng:** `5px`, `10px`, `15px`, `20px`, `25px`, `30px`

### 2. Margin (Khoảng Cách Ngoài)

```css
.element {
  margin-bottom: 20px;               /* Khoảng cách dưới */
  margin-top: 15px;                  /* Khoảng cách trên */
}
```

### 3. Width & Height

```css
.button {
  width: 100%;                       /* Chiều rộng 100% */
  max-width: 200px;                  /* Giới hạn chiều rộng tối đa */
  height: 40px;                      /* Chiều cao */
}
```

### 4. Font Size (Kích Thước Chữ)

```css
h1 {
  font-size: 1.8rem;                 /* Heading 1 (to) */
}

h2 {
  font-size: 1.5rem;                 /* Heading 2 */
}

p {
  font-size: 1rem;                   /* Text thường */
}

small {
  font-size: 0.85rem;                /* Text nhỏ */
}
```

**Qui Tắc:**
- `1rem` = 16px (mặc định)
- `0.85rem` = 13.6px
- `1.2rem` = 19.2px
- `1.5rem` = 24px

---

## Các Ví Dụ Thực Tế

### Ví Dụ 1: Tùy Chỉnh Start Screen

**File:** `App.css`

```css
.start-screen {
  background: white;
  padding: 30px;                     /* Tăng padding từ 20px */
  text-align: center;
  border-radius: 8px;
  max-width: 500px;                  /* Giới hạn chiều rộng */
  margin: 50px auto;                 /* Canh giữa + khoảng cách trên */
}

.start-btn {
  background: #333;
  padding: 12px 30px;                /* Thay đổi kích thước button */
  font-size: 1rem;                   /* Thay đổi kích thước chữ */
  border-radius: 4px;                /* Giảm độ cong */
}
```

### Ví Dụ 2: Tùy Chỉnh Quiz Interface

**File:** `components/Quiz.css`

```css
.quiz-container {
  max-width: 900px;                  /* Tăng từ 800px */
  margin: 20px auto;
  padding: 30px;                     /* Tăng padding */
  background: white;
  border-radius: 8px;
}

.question-card {
  background: #f9f9f9;
  padding: 20px;                     /* Tùy chỉnh padding */
  margin-bottom: 15px;               /* Khoảng cách giữa card */
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.option-btn {
  padding: 12px 15px;                /* Tùy chỉnh vừa button */
  margin-bottom: 8px;                /* Khoảng cách giữa buttons */
  text-align: left;
  border-radius: 4px;
}
```

### Ví Dụ 3: Tùy Chỉnh Admin Dashboard

**File:** `components/AdminDashboard.css`

```css
.stat-box {
  padding: 20px;                     /* Khoảng cách trong box */
  border-radius: 8px;
  text-align: center;
  border: 1px solid #e0e0e0;
}

.stat-number {
  font-size: 2rem;                   /* Kích thước số lớn */
  margin-bottom: 10px;
}

.stat-name {
  font-size: 0.85rem;                /* Kích thước chữ nhỏ */
  text-transform: uppercase;         /* Chữ hoa */
  color: #666;                       /* Màu chữ */
}

.users-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;                  /* Khoảng cách trên */
}

.users-table th {
  padding: 12px;                     /* Khoảng cách trong cell */
  text-align: left;
  background: #e0e0e0;
  border-bottom: 1px solid #ddd;
}

.users-table td {
  padding: 12px;
  border-bottom: 1px solid #e0e0e0;
}
```

### Ví Dụ 4: Tùy Chỉnh Login Form

**File:** `styles/Login.css`

```css
.login-container {
  display: flex;
  justify-content: center;           /* Canh giữa ngang */
  align-items: center;               /* Canh giữa dọc */
  min-height: 100vh;                 /* Toàn chiều cao */
  padding: 20px;
}

.login-box {
  width: 100%;
  max-width: 400px;                  /* Giới hạn chiều rộng */
  padding: 30px;                     /* Khoảng cách trong */
  background: white;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;               /* Khoảng cách giữa input */
}

.form-group input {
  width: 100%;
  padding: 10px;                     /* Khoảng cách trong input */
  border: 1px solid #ddd;
  border-radius: 4px;
}

.submit-btn {
  width: 100%;
  padding: 12px;                     /* Kích thước button */
  margin-top: 10px;
}
```

---

## Các Unit Đo Lường Thường Dùng

| Unit | Ý Nghĩa | Ví Dụ |
|------|---------|-------|
| `px` | Pixel (tuyệt đối) | `16px`, `20px` |
| `rem` | Tương đối với root (16px) | `1rem` = 16px, `1.5rem` = 24px |
| `em` | Tương đối với font-size cha | `1em` = font-size cha |
| `%` | Phần trăm | `100%`, `50%` |
| `vh` | Chiều cao viewport | `100vh` = toàn chiều cao màn hình |
| `vw` | Chiều rộng viewport | `100vw` = toàn chiều rộng màn hình |

---

## Các Thuộc Tính CSS Quan Trọng

### Display
```css
display: flex;           /* Dạng flex */
display: grid;           /* Dạng grid */
display: block;          /* Khối (mặc định) */
display: inline;         /* Inline */
```

### Flexbox (cõng hàng)
```css
display: flex;
flex-direction: row;              /* Xếp ngang */
/* flex-direction: column;        */ /* Xếp dọc */
justify-content: center;          /* Canh giữa ngang */
align-items: center;              /* Canh giữa dọc */
gap: 10px;                        /* Khoảng cách giữa items */
```

### Grid (lưới)
```css
display: grid;
grid-template-columns: 1fr 1fr 1fr;     /* 3 cột bằng nhau */
grid-template-columns: repeat(4, 1fr);  /* 4 cột */
grid-template-columns: 200px 1fr;       /* Cột 1: 200px, cột 2: phần còn lại */
gap: 15px;                               /* Khoảng cách */
```

### Border & Border-Radius
```css
border: 1px solid #ddd;           /* Viền 1px, màu xám */
border-bottom: 2px solid #333;    /* Chỉ viền dưới */
border-radius: 4px;               /* Góc bo 4px */
border-radius: 50%;               /* Hình tròn */
```

### Box Shadow
```css
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
/* offset-x, offset-y, blur, color */
```

---

## Mẹo Hữu Ích

1. **Kiểm Tra CSS bằng DevTools:**
   - Nhấn F12 → Inspect Element → Chỉnh CSS trực tiếp
   - Copy CSS hoàn chỉnh vào file

2. **Responsive Design:**
   ```css
   @media (max-width: 768px) {
     .stats-row {
       grid-template-columns: repeat(2, 1fr);  /* 2 cột trên mobile */
     }
   }
   ```

3. **Dark Mode:**
   - Thêm `body.dark-mode` selector để style dark mode
   - Sử dụng CSS variables (optional):
   ```css
   :root {
     --primary-color: #333;
     --bg-color: #fff;
   }
   
   body.dark-mode {
     --primary-color: #fff;
     --bg-color: #1a1a1a;
   }
   ```

4. **Transition & Animation:**
   ```css
   button {
     transition: all 0.2s ease;     /* Hiệu ứng mượt */
   }
   ```

---

## Hỗ Trợ Thêm

Nếu cần tùy chỉnh giao diện chi tiết hơn, hãy sửa các CSS properties sau:

- **Spacing:** `padding`, `margin`, `gap`
- **Size:** `width`, `height`, `font-size`
- **Color:** `color`, `background`, `border-color`
- **Layout:** `display`, `flex-direction`, `justify-content`, `align-items`
- **Style:** `border-radius`, `box-shadow`, `border`

Chúc bạn thiết kế thành công! 🎨
