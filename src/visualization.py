
import matplotlib.pyplot as plt
import seaborn as sns

def save_all_plots(df):
    # Ví dụ biểu đồ 1
    plt.figure(figsize=(8,5))
    df['is_return'].value_counts().plot(kind='bar')
    plt.title("Phân bổ trả hàng")
    plt.savefig('outputs/order_status_chart.png')
    plt.close()
    # Các biểu đồ khác sẽ được code tương tự vào đây...
