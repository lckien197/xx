Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import streamlit as st
... 
... # Giao diện nhập dữ liệu lịch sử
... st.title('Công cụ tính xác suất lô đề')
... historical_input = st.text_area('Nhập dữ liệu lịch sử lô (các số cách nhau bằng dấu phẩy)', '25, 17, 89, 64, 3, 25, 89, 3, 25, 17, 89, 64, 25, 3')
... 
... # Chuyển đổi dữ liệu thành danh sách số
... if historical_input:
...     try:
...         historical_data = [int(num.strip()) for num in historical_input.split(',')]
...     except ValueError:
...         st.error('Vui lòng nhập dữ liệu hợp lệ!')
... 
...     def calculate_frequency(data):
...         frequency = {}
...         for number in data:
...             if number in frequency:
...                 frequency[number] += 1
...             else:
...                 frequency[number] = 1
...         return frequency
... 
...     def predict_next_number(frequency):
...         numbers = list(frequency.keys())
...         weights = list(frequency.values())
...         predicted_number = random.choices(numbers, weights=weights, k=1)[0]
...         return predicted_number
... 
...     # Tính tần suất
...     frequency = calculate_frequency(historical_data)
... 
...     # Hiển thị tần suất
...     st.write("Tần suất xuất hiện các số lô:")
...     st.write(frequency)
... 
...     # Dự đoán số có khả năng ra tiếp theo
    predicted_number = predict_next_number(frequency)
    st.write(f"Số dự đoán có khả năng ra tiếp theo: {predicted_number}")
