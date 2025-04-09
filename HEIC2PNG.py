import os
import subprocess

def convert_heic_to_png(folder_path):
    # ImageMagick 的完整路径
    magick_path = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(folder_path, filename)
            png_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.png')

            # 调用 ImageMagick 进行转换
            try:
                subprocess.run([magick_path, heic_file_path, png_file_path], check=True)
                print(f"Converted {filename} to {png_file_path}")

                # 删除原始的 HEIC 文件
                os.remove(heic_file_path)
                print(f"Deleted original HEIC file: {heic_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}: {e}")

# 将下面的路径替换为你的文件夹路径
folder_path = r'C:\Users\xijia\Desktop\D20240906_ISAIE2024_教育人工智能_陕西西安'
convert_heic_to_png(folder_path)

