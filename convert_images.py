from PIL import Image
import os

# Define input and output folders
input_folder = r'C:\Users\bkind\iCloudDrive\Data_Projects_and_Tools\pngs logos icons\png files for keeping'  # Replace with your actual input folder path
output_folder = r'C:\Users\bkind\iCloudDrive\Data_Projects_and_Tools\pngs logos icons\png files for keeping'  # Replace with your desired output folder path

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.webp')):
        try:
            # Open the image and save it as PNG
            with Image.open(os.path.join(input_folder, file_name)) as img:
                output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.png")
                img.save(output_file)
                print(f"Converted: {file_name} -> {output_file}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print(f"\nConversion complete! {files_converted} file(s) converted.")

