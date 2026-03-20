# 📦 E-commerce Return Prediction Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Machine Learning](https://img.shields.io/badge/Random--Forest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📖 Tổng quan
Dự án phân tích hành vi trả hàng trong thương mại điện tử. Mục tiêu là dự đoán khả năng một đơn hàng bị hủy/trả dựa trên giá trị, số lượng và vị trí địa lý.

## 🛠 Cấu trúc dự án (6 Notebooks)
1. **01_eda**: Khám phá dữ liệu qua 10 biểu đồ trực quan.
2. **02_preprocess**: Làm sạch và chuẩn hóa dữ liệu.
3. **03_mining**: Tìm kiếm các luật kết hợp sản phẩm.
4. **04_modeling**: Huấn luyện Random Forest Classifier.
5. **05_forecasting**: Dự báo xu hướng tương lai.
6. **06_evaluation**: Đánh giá chi tiết hiệu suất mô hình.

## 📊 Hình ảnh kết quả tiêu biểu
| Tỷ lệ trả hàng | Yếu tố quan trọng | Ma trận nhầm lẫn |
|:---:|:---:|:---:|
| ![Pie](outputs/return_ratio_pie.png) | ![Importance](outputs/feature_importance.png) | ![CM](outputs/confusion_matrix.png) |

## 🚀 Cách sử dụng
Cài đặt thư viện: `pip install pandas matplotlib scikit-learn seaborn`

---
**Author:** lkbdayyy | **Status:** Completed ✅
