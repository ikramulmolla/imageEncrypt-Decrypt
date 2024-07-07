import os
from PIL import Image
import random


def create_output_folder(folder_name="output_images"):
    """Create the output folder if it does not exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def shuffle_pixels(image, key):
    """Shuffle the pixels of the image based on the provided key."""
    width, height = image.size
    pixels = list(image.getdata())

    random.seed(key)
    shuffled_pixels = pixels[:]
    random.shuffle(shuffled_pixels)

    return shuffled_pixels


def unshuffle_pixels(image, key):
    """Unshuffle the pixels of the image based on the provided key."""
    width, height = image.size
    pixels = list(image.getdata())

    random.seed(key)
    order = list(range(len(pixels)))
    random.shuffle(order)

    unshuffled_pixels = [None] * len(pixels)
    for i, index in enumerate(order):
        unshuffled_pixels[index] = pixels[i]

    return unshuffled_pixels


def save_image(image, pixels, output_path):
    """Save the image with the given pixels."""
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    new_image.save(output_path)


def process_image(image_path, key, output_folder="output_images", mode="encrypt"):
    """Encrypt or decrypt the image by shuffling or unshuffling pixels based on the key."""
    with Image.open(image_path) as img:
        if mode == "encrypt":
            processed_pixels = shuffle_pixels(img, key)
            output_path = os.path.join(output_folder, f"encrypted_{os.path.basename(image_path)}")
        else:
            processed_pixels = unshuffle_pixels(img, key)
            output_path = os.path.join(output_folder, f"decrypted_{os.path.basename(image_path)}")

        save_image(img, processed_pixels, output_path)
        print(f"Image {mode}ed and saved to {output_path}")


def main():
    print("Welcome to the ImageEncryptionTool")
    print("This tool was created by Ikramul Molla.")
    print("Ikramul Molla is a Cyber Security Enthusiast, Penetration Testing Specialist, and Ethical Hacker.")
    print("He holds a B.Tech degree in Cyber Security and a Diploma in Computer Science and Technology.")
    print(
        "Ikramul is proficient in PHP, JavaScript, Python, C, and skilled with Kali Linux, Burpsuite, Metasploit, Nmap, Wireshark.")
    print()

    create_output_folder()

    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? (Enter Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice in ['E', 'D']:
            image_path = input("Enter the path of the image: ")
            key = int(input("Enter the encryption key (integer): "))
            if choice == 'E':
                process_image(image_path, key, mode="encrypt")
            else:
                process_image(image_path, key, mode="decrypt")
        else:
            print("Invalid choice. Please choose (E) or (D) or Q to quit.")


if __name__ == "__main__":
    main()
