import os
from PIL import Image

def create_webp_thumbnails(input_folder, output_folder, thumbnail_size=(150, 150), quality=85):
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
                
                # Tạo thumbnail, giữ tỷ lệ khung hình
                img.thumbnail(thumbnail_size, Image.LANCZOS)
                
                # Tạo hình ảnh mới với kích thước chính xác (thêm padding nếu cần)
                thumb_width, thumb_height = img.size
                final_img = Image.new('RGB', thumbnail_size, (255, 255, 255))  # Nền trắng
                offset_x = (thumbnail_size[0] - thumb_width) // 2
                offset_y = (thumbnail_size[1] - thumb_height) // 2
                final_img.paste(img, (offset_x, offset_y))
                
                # Lưu thumbnail với chất lượng tối ưu
                final_img.save(output_path, format="WEBP", quality=quality)
                print(f"Thumbnail created and saved: {output_path}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Ví dụ sử dụng

input_folder = "D:/Working/Project/AI/store_images/cat_1"  # Thay bằng đường dẫn thư mục chứa file WebP
output_folder = "D:/Working/Project/AI/store_images/thumbnail_1"  # Thay bằng đường dẫn thư mục đầu ra

create_webp_thumbnails(input_folder, output_folder, thumbnail_size=(150, 150), quality=85)