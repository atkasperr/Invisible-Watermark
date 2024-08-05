import os
from PIL import Image
import cv2
from imwatermark import WatermarkEncoder
import numpy as np

#input and output files 
input_dir = './Input_Photos'
output_dir = './Output_photos'  

watermark_key = 'hello'
'''
def get_encoded_byte_length(message):
   
    encoded_message = message.encode('utf-8')

    return len(encoded_message)
'''

# Ensuring Directory for debugging stuff  
os.makedirs(output_dir, exist_ok=True)

def apply_watermark(image_path, watermark_key, output_path):
    # Read the image, for each. 
    bgr_image = cv2.imread(image_path)
    
    # Initialize the watermark encoder. KEEP setup keywords! 
    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', watermark_key.encode('utf-8'))
    
    # Apply the watermark (dwtDct is the fastest and least secure) 
    bgr_encoded = encoder.encode(bgr_image, 'dwtDct')
   

    cv2.imwrite(output_path, bgr_encoded)
    print(f"Watermarked image saved to {output_path}")

def process_images(input_directory, output_directory, watermark_key):
    # Processes each image in Input_Photos directory. 
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            apply_watermark(image_path, watermark_key, output_path)

if __name__ == "__main__":
    process_images(input_dir, output_dir, watermark_key)
