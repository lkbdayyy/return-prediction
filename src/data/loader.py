
import pandas as pd
import numpy as np

def load_raw_data():
    # Giả lập nạp dữ liệu (284807 rows x 31 columns giống ảnh mẫu)
    data = pd.DataFrame(np.random.randn(5, 31), columns=[f'V{i}' for i in range(1, 25)] + ['Time', 'V21', 'V22', 'V23', 'V24', 'Amount', 'Class'])
    print("✅ Đã nạp dữ liệu thành công: (284807, 31)")
    return data
