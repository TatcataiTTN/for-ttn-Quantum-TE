# for-ttn-Quantum-TE

Trang tự học song ngữ (Việt/Anh) cho chuỗi Technology Engineering · Quantum. Chạy 100% trong trình duyệt, không cần máy chủ.

- Mảng 01, Xử lý tín hiệu: 26 module từ hai giáo trình Bracewell (*The Fourier Transform and Its Applications*) và Barkat (*Signal Detection and Estimation*). Mỗi module có slide, công thức, notebook Jupyter và quiz.
- Mảng 02 đến 04 (Cơ học lượng tử, Tính toán lượng tử, Quang học lượng tử): đang chờ.

Tiến độ chi tiết: [TASKS.md](TASKS.md). Cách viết module: [build/AUTHORING.md](build/AUTHORING.md).

## Dựng lại trang
```bash
pip install numpy scipy matplotlib nbformat nbconvert nbclient ipykernel
python3 build/build.py          # chạy notebook thật, điền số liệu, sinh HTML
python3 -m http.server 8765     # mở http://localhost:8765/
```
Mọi con số trên trang do notebook in ra và được kiểm bằng hai phương pháp độc lập.
