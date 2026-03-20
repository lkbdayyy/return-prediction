
# 📦 E-commerce Return Prediction Portfolio
> **Phân tích hành vi khách hàng & Mô hình hóa rủi ro hoàn trả - lkbdayyy**

## 📑 1. Tổng quan dự án (Executive Summary)
Dự án được xây dựng nhằm mục tiêu tối ưu hóa lợi nhuận cho doanh nghiệp bằng cách dự báo các đơn hàng có xác suất hoàn trả cao. Thông qua 10 biểu đồ phân tích sâu, chúng tôi đã chỉ ra những quy luật quan trọng giúp bộ phận vận hành đưa ra quyết định dựa trên dữ liệu.

## 📊 2. Phân tích Insights Chuyên sâu (Data-Driven Decisions)

### 📈 Quy mô & Phân bổ (Distribution Analysis)
| Tỷ trọng quy mô (Biểu đồ 1 & 5) | Đặc điểm đơn hàng (Biểu đồ 4 & 6) |
|---|---|
| ![Distribution](outputs/overview_distribution.png) | ![Characteristics](outputs/order_characteristics.png) |
- **Insight:** Tỷ lệ trả hàng chiếm **37.1%**. Đáng chú ý, các đơn hàng bị trả có giá trị trung bình **cao hơn 32%** và số lượng sản phẩm **nhiều hơn 27%** so với đơn thông thường.

### 💰 Quy luật Tài chính & Phân khúc (Strategic Grouping)
| Phân khúc giá (Biểu đồ 9) | Xu hướng tăng trưởng (Biểu đồ 8) |
|---|---|
| ![Price Group](outputs/trends_and_segments.png) | ![Trend](outputs/trends_and_segments.png) |
- **Insight:** Rủi ro tăng vọt theo cấp số nhân khi giá trị đơn hàng thuộc nhóm **"Rất cao"** và số lượng sản phẩm **trên 4 món**.

### 🌍 Phân tích Địa lý & Tương quan (Geographical & Scatter)
| Điểm nóng khu vực (Biểu đồ 7) | Tương quan Item/Payment (Biểu đồ 10) |
|---|---|
| ![States](outputs/top_return_states.png) | ![Scatter](outputs/item_vs_payment_scatter.png) |

## 🤖 3. Kết quả Mô hình Machine Learning
| Tầm ảnh hưởng biến số (Biểu đồ 2) | Ma trận đánh giá (Biểu đồ 3) |
|---|---|
| ![Feature](outputs/feature_importance.png) | ![CM](outputs/confusion_matrix.png) |
- **Kết luận:** Mô hình nhận diện chính xác các yếu tố tài chính là tiền đề then chốt để cảnh báo sớm rủi ro hoàn trả.

---
## 📂 4. Cấu trúc Dự án
Dự án được phân rã thành các bước chi tiết trong thư mục `notebooks/`:
- `01_eda.ipynb`: Khám phá toàn diện 8 biểu đồ hành vi.
- `04_modeling.ipynb`: Huấn luyện thuật toán Random Forest/XGBoost.
- `06_evaluation_report.ipynb`: Đánh giá kỹ thuật và Precision/Recall.

---
**Author:** [lkbdayyy](https://github.com/lkbdayyy)  
**Project Goal:** Bridging the gap between Data Analysis and Business Decisions.
