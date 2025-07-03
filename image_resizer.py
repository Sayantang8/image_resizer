import os
from PIL import Image

def resize_images(folder_path, width, height):
    """Resize all images in a folder to specified dimensions."""
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found!")
        return
    
    # Get all image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    image_files = []
    
    for file in os.listdir(folder_path):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(file)
    
    if not image_files:
        print("No image files found in the folder!")
        return
    
    print(f"Found {len(image_files)} images to resize...")
    
    # Resize each image
    for filename in image_files:
        try:
            # Open image
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            # Resize image
            resized_img = img.resize((width, height))
            
            # Save resized image
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_resized{ext}"
            new_path = os.path.join(folder_path, new_filename)
            resized_img.save(new_path)
            
            print(f"✓ Resized: {filename}")
            
        except Exception as e:
            print(f"✗ Error with {filename}: {e}")
    
    print("Done!")

# Usage
if __name__ == "__main__":
    folder_path = "./image_files" 
    new_width = 800
    new_height = 600
    
    resize_images(folder_path, new_width, new_height)
