import os
from glob import glob

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm


# filter images by size
def filter_images_by_size(images, min_size):
    output = []

    for image in tqdm(images, total=len(images)):
        img = cv2.imread(image, cv2.IMREAD_COLOR)
        h, w, c = img.shape

        if h >= min_size and w >= min_size:
            output.append(image)

    return output


def resize_image(images, height, width):

    resized_images = []
    for img in tqdm(images, total=len(images)):
        img = Image.open(img)

        # Resize image, maintaining aspect ratio
        img.thumbnail((height, width))

        # Create a new square background image
        new_image = Image.new(
            "RGBA",
            (
                height,
                width,
            ),
        )

        # Paste the resized image into the center of the square background image
        new_image.paste(img, ((height - img.size[0]) // 2, (width - img.size[1]) // 2))

        resized_images.append(new_image)

    return resized_images


def save_images(images, save_dir):

    print(f"saving images to {save_dir}")
    idx = 1

    for img in tqdm(images, total=len(images)):
        rgb_img = img.convert("RGB")
        rgb_img.save(f"{save_dir}/{idx}.jpeg")
        idx += 1


def prep_images_for_network(input_dir, output_dir, size):
    all_images = glob(f"{input_dir}/*.jpg") + glob(f"{input_dir}/*.JPG")
    print(f"Number of raw images: {len(all_images)}")
    print(" ")

    print(f"Filtering images by size: {size}")
    filtered_output = filter_images_by_size(all_images, size)
    print(f"Number of images after filtering: {len(filtered_output)}")
    print(" ")

    print(f"Resizing images to {size}x{size}")
    resized_output = resize_image(filtered_output, size, size)
    print(f"Number of images after resizing: {len(resized_output)}")
    print(" ")

    print(f"Saving images to {output_dir}")
    save_images(resized_output, output_dir)
    print("Done!")


prep_images_for_network(
    "../../images_dataset/raw_images", "../../images_dataset/images_for_network", 512
)
