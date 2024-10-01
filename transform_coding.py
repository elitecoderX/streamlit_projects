import numpy as np
from PIL import Image
from scipy.fftpack import dct, idct
from numpy.fft import fft2, ifft2
import io

def input_img(file):
    image = Image.open(file)
    gray_image = image.convert('L')
    gray_image = np.array(gray_image, dtype='float32')
    return gray_image

def add_padding(image, patch_size):
    pad_h = (patch_size - image.shape[0] % patch_size) % patch_size
    pad_w = (patch_size - image.shape[1] % patch_size) % patch_size
    padded_image = np.pad(image, ((0, pad_h), (0, pad_w)), mode='edge')
    return padded_image

def remove_padding(padded_image, original_height, original_width):
    return padded_image[:original_height, :original_width]

def create_patches(image, patch_size):
    image_height, image_width= image.shape
    patches = []
    for i in range(0, image_height, patch_size):
        for j in range(0, image_width, patch_size):
            patch = image[i:i + patch_size, j:j + patch_size]
            patches.append(patch)
    return patches

def merge_patches(patches, image_shape, patch_size):
    image_height, image_width = image_shape
    reconstructed_image = np.zeros((image_height, image_width), dtype=patches[0].dtype)
    patch_idx = 0
    for i in range(0, image_height, patch_size):
        for j in range(0, image_width, patch_size):
            reconstructed_image[i:i + patch_size, j:j + patch_size] = patches[patch_idx]
            patch_idx += 1
    return reconstructed_image

def transform(block, mode):
    if mode=='DCT':
        return dct(dct(block.T, norm='ortho').T, norm='ortho')
    elif mode=='FFT':
        return fft2(block)
    
def inverse_transform(block, mode):
    if mode=='DCT':
        return idct(idct(block.T, norm='ortho').T, norm='ortho')
    elif mode=='FFT':
        return np.real(ifft2(block))
    
def quantize(block,percentage):
    flat_arr = block.ravel()
    k = int((1 - percentage / 100) * flat_arr.size)
    threshold_value = np.partition(flat_arr, k)[k]
    block[np.abs(block) < threshold_value] = 0
    return block

def MSE(original_image, compressed_image):
    mse = np.mean((original_image - compressed_image) ** 2)
    return mse

def get_image_size(image):
    with io.BytesIO() as output:
        image.save(output, format="JPEG")
        size_kb = len(output.getvalue()) / 1024
    return size_kb

def compress_img(path, patch_size, t_mode, q_level):
    image = input_img(path)
    padded_image = add_padding(image, patch_size)
    patches = create_patches(padded_image, patch_size)
    trans_patches = [transform(patch, t_mode) for patch in patches]
    quantized_patches = [quantize(patch, q_level) for patch in trans_patches]
    inv_trans_patches = [inverse_transform(patch, t_mode) for patch in quantized_patches]
    compressed_image = merge_patches(inv_trans_patches, padded_image.shape, patch_size)
    compressed_image = np.round(remove_padding(compressed_image, image.shape[0], image.shape[1]), decimals=0)
    return image, compressed_image