# Prodigy_CS_02
Image Encryption Tool
Overview

This Python tool encrypts and decrypts images using basic pixel manipulation. The encryption method involves modifying pixel values using a user-provided key, making it a simple yet effective way to obscure images.
Features

    Encrypts images by modifying pixel values.

    Decrypts images using the same key.

    Supports common image formats (PNG, JPG, BMP, etc.).

    Lightweight and easy to use.

How It Works

    The user selects an image file.

    A numeric key is provided for encryption.

    The tool modifies pixel values using the key.

    To decrypt, the same key is used to reverse the process.

Installation

Ensure you have Python installed along with the required dependencies:
Ensure you have Python installed along with the required dependencies:

pip install pillow numpy

Usage

Run the script and follow the prompts:

python image_encryption_tool.py

Example
Encrypt an image

Do you want to (E)ncrypt or (D)ecrypt an image? E
Enter the image file path: input.jpg
Enter encryption key (integer): 50
Enter output file path: encrypted.png
Encrypted image saved as encrypted.png

Decrypt an image

Do you want to (E)ncrypt or (D)ecrypt an image? D
Enter the image file path: encrypted.png
Enter encryption key (integer): 50
Enter output file path: decrypted.jpg
Decrypted image saved as decrypted.jpg

Notes

    The same key must be used for both encryption and decryption.

    Incorrect keys will result in incorrect decryption.

    The method is basic and not suitable for high-security applications.
