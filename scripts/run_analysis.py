
from src.data_processing import clean_data
from src.visualization import save_all_plots
import pandas as pd
import os

def main():
    """
    File thực thi chính: Đọc dữ liệu, xử lý, vẽ biểu đồ.
    """
    print("🚀 Bắt đầu quá trình phân tích...")
    # df = pd.read_csv('data/raw/data.csv') # Ví dụ đường dẫn dữ liệu thật
    # df = clean_data(df)
    # save_all_plots(df)
    print("✅ Hoàn thành!")

if __name__ == "__main__":
    main()
