import os
from PIL import Image

def resize_webp_folder(input_folder, output_folder, target_size=(750, 750), quality=85):
    # Tạo thư mục đầu ra nếu chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lặp qua tất cả các file trong thư mục đầu vào
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}")
            
            try:
                # Mở hình ảnh
                img = Image.open(input_path)
                
                # Chuyển sang chế độ RGB nếu cần (đảm bảo tương thích)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Tính toán tỷ lệ khung hình
                original_width, original_height = img.size
                target_width, target_height = target_size
                
                # Resize giữ tỷ lệ khung hình
                ratio = min(target_width / original_width, target_height / original_height)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
                
                # Resize hình ảnh
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                
                # Tạo hình ảnh mới với kích thước 750x750, thêm padding nếu cần
                final_img = Image.new('RGB', target_size, (255, 255, 255))  # Nền trắng
                offset_x = (target_width - new_width) // 2
                offset_y = (target_height - new_height) // 2
                final_img.paste(resized_img, (offset_x, offset_y))
                
                # Lưu hình ảnh với chất lượng nén tối ưu
                final_img.save(output_path, format="WEBP", quality=quality)
                print(f"Resized and saved: {output_path}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Ví dụ sử dụng
input_folder = "D:/Working/Project/AI/store_images/cat_1"  # Thay bằng đường dẫn thư mục chứa file WebP
output_folder = "D:/Working/Project/AI/store_images/out"  # Thay bằng đường dẫn thư mục đầu ra
resize_webp_folder(input_folder, output_folder, target_size=(750, 750), quality=85)