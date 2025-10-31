# Báo Cáo Bài Tập Lớn Giải Tích 1

## Đề tài: Vẽ Quỹ Đạo và Xác Định Vector Mômen Động Lượng Của Chuyển Động

### Cấu trúc thư mục

```
report/
├── main.tex                          # File LaTeX chính
├── main.bib                          # File tài liệu tham khảo
├── bai8_momen_dong_luong.py         # Code Python chính
├── pictures/                         # Thư mục chứa hình ảnh
│   ├── logobk.png
│   ├── logobk.jpg
│   ├── minh_hoa_khai_niem.png
│   ├── vi_du_1_chuyen_dong_tron.png
│   └── vi_du_2_quy_dao_xoan_oc.png
└── README.md                         # File hướng dẫn này
```

### Cách sử dụng với Overleaf

#### Bước 1: Tải toàn bộ thư mục `report`
Tải toàn bộ nội dung thư mục `report` về máy tính.

#### Bước 2: Upload lên Overleaf

1. Đăng nhập vào [Overleaf](https://www.overleaf.com/)
2. Nhấn "New Project" → "Upload Project"
3. Nén toàn bộ thư mục `report` thành file ZIP
4. Upload file ZIP lên Overleaf

#### Bước 3: Cấu hình Compiler

1. Nhấn vào biểu tượng Menu (góc trên bên trái)
2. Trong phần "Settings":
   - **Compiler**: chọn **pdfLaTeX** hoặc **XeLaTeX**
   - **Main document**: chọn **main.tex**
   - **TeX Live version**: chọn phiên bản mới nhất (2024 hoặc 2023)

#### Bước 4: Compile

1. Nhấn nút "Recompile" 
2. Lần đầu compile có thể mất vài phút do cần tải các package
3. Nếu gặp lỗi với `biblatex`, compile lại 2-3 lần (LaTeX cần nhiều lần compile để xử lý references)

### Compile trên máy local

#### Yêu cầu
- TeX Live (Linux/Windows) hoặc MacTeX (macOS)
- Biber (cho bibliography)

#### Các lệnh compile

```bash
cd report

# Compile LaTeX
pdflatex main.tex

# Compile bibliography
biber main

# Compile lại để cập nhật references
pdflatex main.tex
pdflatex main.tex
```

Hoặc sử dụng latexmk (đơn giản hơn):

```bash
latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" main.tex
```

### Tùy chỉnh nội dung

#### Thay đổi thông tin nhóm

Mở file `main.tex`, tìm và sửa các phần sau:

```latex
% Dòng ~233: Tên nhóm trên trang bìa
{\fontsize{20pt}{1}\selectfont
    \bf NHÓM ____}

% Dòng ~251: Thông tin thành viên
\begin{tabular}{|c|c|c|p{3cm}|}
\hline
\textbf{STT}&\textbf{MSSV}& \textbf{Họ và tên} & \textbf{Ghi chú}\\
\hline 	1&2400001& Nguyễn Văn A&\\
\hline 	2&2400002& Trần Thị B&\\
...
\end{tabular}

% Dòng ~265: Giáo viên hướng dẫn
{\fontsize{16pt}{1}\selectfont
    \bf GVHD:\hskip1em TS. Nguyễn Văn X}
```

#### Thêm/bớt hình ảnh

Để chèn thêm hình ảnh:

```latex
\insertimage{pictures/ten_file_anh}{0.7}{Chú thích hình ảnh}
```

Tham số:
- `pictures/ten_file_anh`: Đường dẫn file (không cần đuôi .png/.jpg)
- `0.7`: Tỷ lệ chiều rộng (0.7 = 70% chiều rộng trang)
- `Chú thích hình ảnh`: Tiêu đề hiển thị dưới hình

### Xử lý lỗi thường gặp

#### Lỗi: "File not found"
- Kiểm tra đường dẫn file hình ảnh
- Đảm bảo thư mục `pictures/` có đủ file

#### Lỗi: "Undefined control sequence"
- Một số package chưa được cài đặt
- Trên Overleaf: thường tự động cài, chờ vài phút
- Trên local: cài đặt package bị thiếu qua TeX package manager

#### Lỗi với `biblatex`
- Compile nhiều lần (3-4 lần)
- Thứ tự: pdflatex → biber → pdflatex → pdflatex

#### Lỗi font tiếng Việt
- Trên Overleaf: dùng compiler **XeLaTeX** thay vì pdfLaTeX
- File đã cấu hình sẵn package `vietnam` để hỗ trợ tiếng Việt

### Code Python

File `bai8_momen_dong_luong.py` được nhúng trong báo cáo. Để chạy thử:

```bash
cd report
python bai8_momen_dong_luong.py
```

### Tài liệu tham khảo

File `main.bib` chứa các tài liệu tham khảo theo định dạng BibTeX. Để thêm tài liệu mới:

```bibtex
@book{unique_key,
  title={Tên sách},
  author={Tác giả},
  year={Năm},
  publisher={Nhà xuất bản}
}
```

Sau đó trích dẫn trong văn bản: `\cite{unique_key}`

### Liên hệ

Nếu gặp vấn đề khi compile, vui lòng:
1. Kiểm tra log file để xem lỗi cụ thể
2. Đảm bảo đã upload đầy đủ file
3. Thử compile trên Overleaf (đơn giản nhất)

---

**Lưu ý**: File LaTeX này được tối ưu cho Overleaf và các bản phân phối TeX Live hiện đại. Nếu sử dụng MiKTeX trên Windows, có thể cần cài thêm một số package thủ công.
