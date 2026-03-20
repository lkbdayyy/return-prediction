# 📦 E-commerce Return Prediction Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Machine Learning](https://img.shields.io/badge/Random--Forest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📖 Tổng quan
Dự án phân tích hành vi trả hàng trong thương mại điện tử. Mục tiêu là dự đoán khả năng một đơn hàng bị hủy/trả dựa trên giá trị, số lượng và vị trí địa lý.
Dự án tập trung vào việc nghiên cứu và ứng dụng các kỹ thuật Khai phá dữ liệu (Data Mining) để giải quyết bài toán dự báo hành vi hoàn trả đơn hàng trong thương mại điện tử. Thông qua việc phân tích dữ liệu lịch sử từ các bảng giao dịch, khách hàng và thanh toán, chúng tôi xây dựng hệ thống phân loại chính xác các đơn hàng có rủi ro bị hủy cao.

Các mục tiêu chính bao gồm:
* Phân tích các yếu tố tác động đến tâm lý khách hàng khi thực hiện hủy đơn.
* Xây dựng mô hình học máy để tự động hóa việc đánh giá rủi ro đơn hàng.
* Cung cấp cái nhìn trực quan về xu hướng vận hành của doanh nghiệp.

## 📊 Hình ảnh kết quả tiêu biểu
| Tỷ lệ trả hàng | Yếu tố quan trọng | Ma trận nhầm lẫn |
|:---:|:---:|:---:|
| ![Pie](outputs/return_ratio_pie.png) | ![Importance](outputs/feature_importance.png) | ![CM](outputs/confusion_matrix.png) |

## 📂 Cấu trúc thư mục chuyên nghiệp
```text
Nhom12_BaiTapLon_DataMining/
├── app/                      # Ứng dụng Demo (Giao diện web Streamlit)
│   └── streamlit_app.py      # Script chạy ứng dụng dự báo
├── configs/                  # Tham số cấu hình (Paths, Hyperparameters)
├── data/
│   ├── raw/                  # Tập dữ liệu gốc chưa xử lý (.csv)
│   └── processed/            # Dữ liệu sau khi làm sạch và chuẩn hóa
├── notebooks/                # Jupyter Notebooks chi tiết từng giai đoạn
│   ├── 01_eda.ipynb          # Khám phá dữ liệu qua biểu đồ (EDA)
│   ├── 02_preprocess.ipynb   # Tiền xử lý & Kỹ thuật đặc trưng
│   ├── 03_mining_clustering.ipynb # Khai phá luật kết hợp & Phân cụm
│   ├── 04_modeling.ipynb     # Xây dựng mô hình học máy có giám sát
│   ├── 05_time_series.ipynb  # Phân tích & Dự báo chuỗi thời gian
│   └── 06_evaluation.ipynb   # Tổng hợp chỉ số & Báo cáo đánh giá
├── outputs/                  # Lưu trữ kết quả hình ảnh (Charts/Plots)
├── src/                      # Mã nguồn module xử lý (Loader, Cleaner)
└── README.md                 # Tài liệu hướng dẫn dự án
🔍 Phương pháp tiếp cận
Phân tích EDA: Sử dụng Matplotlib và Seaborn để tìm kiếm mối tương quan giữa giá trị đơn hàng và tỷ lệ trả hàng.

Tiền xử lý: Sử dụng Label Encoding cho các biến phân loại và chuẩn hóa dữ liệu để đảm bảo độ tin cậy.

Mô hình hóa: Áp dụng thuật toán Random Forest - một phương pháp mạnh mẽ giúp xử lý dữ liệu phi tuyến tính hiệu quả.

Đánh giá: Sử dụng Ma trận nhầm lẫn (Confusion Matrix) và Báo cáo phân loại để đo lường hiệu suất thực tế.

Nhóm thực hiện: Nhóm 12 - Khoa Công nghệ Thông tin
---
**Author:** lkbdayyy | **Status:** Completed ✅
