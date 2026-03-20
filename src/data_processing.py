
import pandas as pd
def clean_data(df):
    # Thêm các bước xử lý dữ liệu của bạn vào đây
    df['is_return'] = df['order_status'].apply(lambda x: 1 if x == 'returned' else 0)
    return df
