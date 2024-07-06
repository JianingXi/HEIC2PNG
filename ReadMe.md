
# HEIC to PNG Converter

This script converts all HEIC images in a specified folder to PNG format using ImageMagick and then deletes the original HEIC files.

����ű�ʹ��ImageMagick��ָ���ļ����е�����HEICͼ��ת��ΪPNG��ʽ��Ȼ��ɾ��ԭʼ��HEIC�ļ���

## Requirements
- Python 3.x
- ImageMagick

## ��װ ImageMagick

1. Download and install ImageMagick from [ImageMagick Downloads](https://imagemagick.org/script/download.php#windows).
2. During installation, ensure you select the option "Install legacy utilities (e.g. convert)".

��[ImageMagick ����ҳ��](https://imagemagick.org/script/download.php#windows)���ز���װImageMagick���ڰ�װ�����У�ȷ��ѡ���ˡ�Install legacy utilities (e.g. convert)��ѡ�

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/heic-to-png-converter.git
cd heic-to-png-converter
```

��¡�ֿ⣺
```sh
git clone https://github.com/yourusername/heic-to-png-converter.git
cd heic-to-png-converter
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

��װ�����Python����
```sh
pip install -r requirements.txt
```

## Usage

1. Open the script `heic_to_png.py` and modify the `folder_path` variable to point to the directory containing your HEIC files.

�򿪽ű�`heic_to_png.py`���޸�`folder_path`������ʹ��ָ��������HEIC�ļ���Ŀ¼��

```python
folder_path = r'D:\path\to\your\folder'
```

2. Run the script:

```sh
python heic_to_png.py
```

���нű���
```sh
python heic_to_png.py
```

## Script Explanation

This script iterates over all HEIC files in the specified folder, converts them to PNG format using ImageMagick, and then deletes the original HEIC files.

����ű�����ָ���ļ����е�����HEIC�ļ���ʹ��ImageMagick������ת��ΪPNG��ʽ��Ȼ��ɾ��ԭʼ��HEIC�ļ���

## Code

```python
import os
import subprocess

def convert_heic_to_png(folder_path):
    # ImageMagick ������·��
    magick_path = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(folder_path, filename)
            png_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.png')

            # ���� ImageMagick ����ת��
            try:
                subprocess.run([magick_path, heic_file_path, png_file_path], check=True)
                print(f"Converted {filename} to {png_file_path}")

                # ɾ��ԭʼ�� HEIC �ļ�
                os.remove(heic_file_path)
                print(f"Deleted original HEIC file: {heic_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}: {e}")

# �������·���滻Ϊ����ļ���·��
folder_path = r'D:\path\to\your\folder'
convert_heic_to_png(folder_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ���֤

�����Ŀ�Ǹ���MIT���֤��Ȩ�� - ���[LICENSE](LICENSE)�ļ���
