
import pandas as pd
import numpy as np

def clean_data(df):
    """
    Hàm xử lý và làm sạch dữ liệu đơn hàng.
    Thêm cột phân loại 'is_return' từ trạng thái đơn hàng.
    """
    # Tạo biến mục tiêu (Target variable)
    df['is_return'] = df['order_status'].apply(lambda x: 1 if x == 'returned' else 0)
    
    # Chia nhóm giá bằng pd.qcut
    df['price_group'] = pd.qcut(df['payment_value'], 4, labels=["Thấp", "Trung bình", "Cao", "Rất cao"])
    
    return df
