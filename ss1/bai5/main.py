# Phần 2 - Mã nguồn Python mô phỏng

def process_rikkeimart_order(item_status, customer_response):
    try:
        if item_status == "available":
            return "Sản phẩm còn hàng. Tài xế mua hàng và tiếp tục giao."
        if item_status == "out_of_stock":
            if customer_response == "accept":
                return "Khách hàng đồng ý đổi sản phẩm."
            if customer_response == "reject":
                return "Khách hàng từ chối sản phẩm thay thế."
            if customer_response == "timeout":
                return "Không nhận được phản hồi trong 3 phút."
            raise ValueError("customer_response không hợp lệ.")
        raise ValueError("item_status không hợp lệ.")
    except ValueError as e:
        return f"Lỗi dữ liệu đầu vào: {e}"
    
print(process_rikkeimart_order("available", None))
print(process_rikkeimart_order("out_of_stock","accept"))
print(process_rikkeimart_order("out_of_stock","reject"))
print(process_rikkeimart_order("out_of_stock","timeout"))

# | Tình huống             | Kết quả                                                     |
# | ---------------------- | ----------------------------------------------------------- |
# | available              | Tiếp tục mua và giao hàng                                   |
# | out_of_stock + accept  | Đổi sang sản phẩm tương đương                               |
# | out_of_stock + reject  | Hủy mặt hàng/đơn hàng                                       |
# | out_of_stock + timeout | Kích hoạt Auto-substitute hoặc Auto-cancel sau 3 phút       |
# | Dữ liệu sai            | Bắt ngoại lệ và trả thông báo lỗi, chương trình không crash |

# Kết luận
# Use Case Diagram giúp xác định các chức năng và tác nhân tham gia.
# Activity Diagram giúp mô tả rõ luồng xử lý hết hàng và bẫy Timeout 3 phút.
# Class Diagram giúp thiết kế cấu trúc dữ liệu của hệ thống.
# Chương trình Python trên xử lý đầy đủ các trường hợp còn hàng, hết hàng, đổi món, từ chối và Timeout mà không làm ứng dụng bị crash.
