import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity as ssim

def find_difference(image1, image2):
    if image1.shape != image2.shape:
        raise ValueError("Specify 2 images with the same shape.")
    
    gray_image1, gray_image2 = map(rgb2gray, (image1, image2))
    score, difference_image = ssim(gray_image1, gray_image2, full=True)
    print(f"Similarity of the images: {score:.4f}")
    
    normalized_difference_image = (difference_image - difference_image.min()) / (difference_image.max() - difference_image.min())
    return normalized_difference_image

def transfer_histogram(image1, image2):
    return match_histograms(image1, image2, multichannel=True)