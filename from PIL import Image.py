from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    encrypted_pixels = (pixels + key) % 256  # Basic encryption by shifting pixel values
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    decrypted_pixels = (pixels - key) % 256  # Reverse the operation
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Example Usage
if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().lower()
    image_path = input("Enter the image file path: ")
    key = int(input("Enter encryption key (integer): "))
    output_path = input("Enter output file path: ")
    
    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    elif choice == 'd':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
