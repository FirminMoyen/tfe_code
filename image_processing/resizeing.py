import os, sys
from PIL import Image

def resize_image(input_image_path, output_image_path):
    try:
        # Check if output directory exists, if not create it
        output_dir = os.path.dirname(output_image_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with Image.open(input_image_path) as image:
            # Resize image, maintaining aspect ratio
            image.thumbnail((512, 512))

            # Create a new square background image
            new_image = Image.new("RGBA", (512, 512,))

            # Paste the resized image into the center of the square background image
            new_image.paste(image, ((512 - image.size[0]) // 2, (512 - image.size[1]) // 2))

            new_image.save(output_image_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_path = "TFE/tfe_code/image_processing/unet_segmentation/dataset/og_images/a15.jpg"
output_path = "TFE/tfe_code/image_processing/unet_segmentation/dataset/resized_images/a15_RS.jpg"
resize_image(input_path, output_path)
print("Image resized and saved successfully!")