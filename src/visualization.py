
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def save_all_plots(df):
    """
    Hàm tổng hợp để vẽ và lưu 10 biểu đồ phân tích.
    """
    # Cấu hình chung cho biểu đồ
    sns.set_style("whitegrid")
    plt.rcParams.update({'font.size': 12})

    # --- 1. Biểu đồ 1: Phân bổ Đơn hàng (Bar Chart) ---
    plt.figure(figsize=(8, 5))
    df['is_return'].value_counts().plot(kind='bar', color=['teal', 'tomato'])
    plt.title("Phân bổ Trả hàng (Returned Orders Distribution)", fontweight='bold')
    plt.xlabel("Trạng thái (0: Thành công, 1: Trả hàng)")
    plt.ylabel("Số lượng")
    plt.savefig('outputs/order_status_chart.png')
    plt.close()

    # --- 2. Biểu đồ 2: Tỷ lệ Phần trăm (Pie Chart) ---
    # (Tự động cập nhật code vẽ 10 biểu đồ vào đây...)
    # [Code vẽ các biểu đồ khác sẽ được code tương tự...]
