
# 📦 E-commerce Return Prediction Analysis
> **Data Science & Machine Learning Portfolio - Thực hiện bởi lkbdayyy**

## 📑 1. Tổng quan Dự án (Project Overview)
Việc hoàn trả hàng gây ra tổn thất Logistic ngược rất lớn cho các doanh nghiệp E-commerce. Dự án này xây dựng một hệ thống **Dự báo rủi ro hoàn trả** thông qua quy trình CRISP-DM hoàn chỉnh, giúp doanh nghiệp tối ưu hóa lợi nhuận.

## 📊 2. Insights Đa chiều & Báo cáo Phân tích (Core Findings)
Dự án được phân rã thành các nhánh nghiên cứu chuyên sâu, mời giảng viên và người xem truy cập thư mục `notebooks/` để xem chi tiết từng bước.

### 📈 Tình trạng Quy mô và Phân bổ
| Tỷ lệ phần trăm tổng quát (EDA) | Đặc điểm Giá trị/Số lượng (EDA) |
|---|---|
| ![Distribution](outputs/overview_distribution.png) | ![Characteristics](outputs/order_characteristics.png) |
- **Insight:** Tỷ lệ trả hàng chiếm **37%**. Đáng chú ý, các đơn hàng bị trả có giá trị trung bình **cao hơn 32%** và số lượng sản phẩm **nhiều hơn 27%** so với đơn thông thường.

### 🌍 Phân tích Địa lý & Xu hướng
| Top Khu vực rủi ro (EDA) | Xu hướng rủi ro theo Số lượng (EDA) |
|---|---|
| ![States](outputs/top_return_states.png) | ![Trend](outputs/trends_and_segments.png) |
- **Insight:** Rủi ro hoàn hàng **tăng tỉ lệ thuận** với số lượng món đồ trong đơn. Các bang lớn như SP, RJ là những 'điểm nóng' cần được bộ phận Logistics chấn chỉnh khâu vận chuyển.

### 🧬 Mô hình hóa & Đánh giá
| Mức độ ảnh hưởng biến số (Modeling) | Ma trận đánh giá hiệu quả (Evaluation) |
|---|---|
| ![Feature](outputs/feature_importance.png) | ![CM](outputs/confusion_matrix.png) |
- **Giải pháp:** Với độ chính xác cao từ Confusion Matrix, doanh nghiệp có thể gọi điện xác nhận kỹ hơn cho các đơn hàng có giá trị cao trước khi xuất kho.

---
**Author:** [lkbdayyy](https://github.com/lkbdayyy)  
*Project Goal: bridging the gap between Data Analysis and Business Decisions.*
