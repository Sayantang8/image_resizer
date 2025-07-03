# Image Resizer

This project provides a simple Python script to resize images. It is useful for batch processing images to a specific size for web, presentations, or other uses.

## Features

- Resize images to desired dimensions
- Supports common image formats (e.g., JPG, PNG)
- Easy to use and modify

## Getting Started

### Prerequisites

- Python 3.11
- Pillow library (for image processing)

Install Pillow using pip:

```powershell
pip install pillow
```

### Usage

1. Place the images you want to resize in the `image_files` directory.
2. Run the script:

```powershell
python image_resizer.py
```

3. The resized images will be saved in the same directory with `_resized` appended to the filename.

## File Structure

- `image_resizer.py` — Main script for resizing images
- `image_files/` — Directory containing original and resized images
- `README.md` — Project documentation

## Example

Original: `AGRASEN.jpg`
Resized: `AGRASEN_resized.jpg`

## License

This project is under the MIT License.
