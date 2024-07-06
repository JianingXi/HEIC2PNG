
# HEIC to PNG Converter

This script converts all HEIC images in a specified folder to PNG format using ImageMagick and then deletes the original HEIC files.

这个脚本使用ImageMagick将指定文件夹中的所有HEIC图像转换为PNG格式，然后删除原始的HEIC文件。

## Requirements
- Python 3.x
- ImageMagick

## 安装 ImageMagick

1. Download and install ImageMagick from [ImageMagick Downloads](https://imagemagick.org/script/download.php#windows).
2. During installation, ensure you select the option "Install legacy utilities (e.g. convert)".

从[ImageMagick 下载页面](https://imagemagick.org/script/download.php#windows)下载并安装ImageMagick。在安装过程中，确保选择了“Install legacy utilities (e.g. convert)”选项。

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/heic-to-png-converter.git
cd heic-to-png-converter
```

克隆仓库：
```sh
git clone https://github.com/yourusername/heic-to-png-converter.git
cd heic-to-png-converter
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

安装所需的Python包：
```sh
pip install -r requirements.txt
```

## Usage

1. Open the script `heic_to_png.py` and modify the `folder_path` variable to point to the directory containing your HEIC files.

打开脚本`heic_to_png.py`并修改`folder_path`变量，使其指向包含你的HEIC文件的目录。

```python
folder_path = r'D:\path\to\your\folder'
```

2. Run the script:

```sh
python heic_to_png.py
```

运行脚本：
```sh
python heic_to_png.py
```

## Script Explanation

This script iterates over all HEIC files in the specified folder, converts them to PNG format using ImageMagick, and then deletes the original HEIC files.

这个脚本遍历指定文件夹中的所有HEIC文件，使用ImageMagick将它们转换为PNG格式，然后删除原始的HEIC文件。

## Code

```python
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
folder_path = r'D:\path\to\your\folder'
convert_heic_to_png(folder_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 许可证

这个项目是根据MIT许可证授权的 - 详见[LICENSE](LICENSE)文件。
