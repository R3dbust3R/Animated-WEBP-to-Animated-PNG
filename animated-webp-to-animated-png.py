from PIL import Image
import imageio

def convert_webp_to_apng(webp_path, apng_path, size=(500, 500)):
    # Read frames from the animated WebP file
    frames = imageio.mimread(webp_path, format="webp")
    png_frames = []

    # Convert each frame to PNG, resize, and set to RGBA mode for 32-bit depth
    for frame in frames:
        png_frame = Image.fromarray(frame).convert("RGBA")  # Convert to RGBA for 32-bit depth
        png_frame = png_frame.resize(size)
        png_frames.append(png_frame)

    # Save frames as animated PNG
    png_frames[0].save(
        apng_path,
        save_all=True,
        append_images=png_frames[:],
        duration=75,  # Adjust frame duration if needed
        loop=0  # Infinite loop
    )


def main():
    webp_path = input("Path to your animated WEBP file: ")
    apng_path = webp_path.replace('.webp', '.png')
    apng_output_size = int(input('Enter your PNG output dimensions: '))
    convert_webp_to_apng(webp_path, apng_path, apng_output_size)


if __name__ == '__main__':
    main()