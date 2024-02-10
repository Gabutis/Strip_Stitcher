import numpy as np
from PIL import Image
import logging
import os
import json

config_path = './config.json'
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
num_horizontal_stripes = config.get('num_horizontal_stripes')
num_vertical_stripes = config.get('num_vertical_stripes')

logs_dir = "./logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(logs_dir, "errors.log")),
                        logging.StreamHandler()
                    ])


def create_striped_image(image, num_stripes, direction='vertical'):
    logging.info(
        f"Creating {'vertical' if direction == 'vertical' else 'horizontal'} striped image with {num_stripes} stripes.")
    if direction == 'vertical':
        total_length = image.shape[1]
    else:
        total_length = image.shape[0]

    base_stripe_size = total_length // num_stripes
    extra_pixels = total_length % num_stripes
    stripe_sizes = [base_stripe_size + 1 if i < extra_pixels else base_stripe_size for i in range(num_stripes)]

    stripes = []
    current_pos = 0
    for size in stripe_sizes:
        if direction == 'vertical':
            stripe = image[:, current_pos:current_pos + size, :]
        else:
            stripe = image[current_pos:current_pos + size, :, :]
        stripes.append(stripe)
        current_pos += size

    striped_images = [np.zeros((image.shape[0], 0, 3), dtype=image.dtype) if direction == 'vertical' else np.zeros(
        (0, image.shape[1], 3), dtype=image.dtype) for _ in range(2)]
    for i, stripe in enumerate(stripes):
        if i % 2 == 0:
            if direction == 'vertical':
                striped_images[0] = np.concatenate((striped_images[0], stripe), axis=1)
            else:
                striped_images[0] = np.concatenate((striped_images[0], stripe), axis=0)
        else:
            if direction == 'vertical':
                striped_images[1] = np.concatenate((striped_images[1], stripe), axis=1)
            else:
                striped_images[1] = np.concatenate((striped_images[1], stripe), axis=0)

    striped_image = np.concatenate(striped_images, axis=1 if direction == 'vertical' else 0)
    return striped_image


def stack_images_vertically(images):
    logging.info("Stacking images vertically.")
    total_height = sum(image.shape[0] for image in images)
    width = images[0].shape[1]
    stacked_image = np.zeros((total_height, width, 3), dtype=np.uint8)

    current_y = 0
    for image in images:
        end_y = current_y + image.shape[0]
        stacked_image[current_y:end_y, :, :] = image
        current_y = end_y

    return stacked_image


def main():
    image_path = './data/image.jpg'
    logging.info(f"Loading image from {image_path}.")

    try:
        original_image = Image.open(image_path)
        original_image_arr = np.array(original_image)
    except FileNotFoundError:
        logging.error(f"File not found: {image_path}", exc_info=True)
        return

    logging.info("Applying vertical striping.")
    vertical_striped_image = create_striped_image(original_image_arr, num_vertical_stripes, 'vertical')

    logging.info("Applying horizontal striping.")
    final_striped_image = create_striped_image(vertical_striped_image, num_horizontal_stripes, 'horizontal')

    logging.info("Stacking all images into a final image.")
    images_to_stack = [original_image_arr, vertical_striped_image, final_striped_image]
    stacked_image_arr = stack_images_vertically(images_to_stack)

    stacked_image_path = './data/shredded_and_reassembled_image.jpg'
    logging.info(f"Saving the final stacked image to {stacked_image_path}.")
    stacked_image = Image.fromarray(stacked_image_arr)
    stacked_image.save(stacked_image_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("An unhandled exception occurred", exc_info=True)
