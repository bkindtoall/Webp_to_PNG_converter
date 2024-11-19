# Image Conversion Script

This project contains a Python script that automates the process of converting image files from various formats (e.g., JPG, GIF, WebP) to PNG. The script is lightweight, easy to use, and ideal for batch processing.

---

## Features

- Converts images from formats like **JPG**, **JPEG**, **GIF**, and **WebP** to **PNG**.
- Supports batch processing of files in a specified input folder.
- Automatically creates an output folder if it doesn't exist.
- Logs converted files and any errors encountered.

---

## Requirements

- Python 3.7 or later
- [Pillow](https://pillow.readthedocs.io/) library for image processing

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Install Dependencies**:
   Install the required Python library:
   ```bash
   pip install pillow
   ```

---

## Usage

1. **Prepare Your Files**:
   - Place the images you want to convert in the `input` folder (or modify the script to point to your desired directory).

2. **Run the Script**:
   ```bash
   python convert_images.py
   ```

3. **View the Results**:
   - Converted images will appear in the `output` folder.

---

## Script Customization

- **Input Folder**: Update the `input_folder` variable in the script to point to your images directory.
- **Output Folder**: Update the `output_folder` variable for the desired destination directory.
- **Supported Formats**: The script currently supports JPG, JPEG, GIF, and WebP. Modify the `endswith` check to add more formats if needed.

---

## Example

```python
input_folder = r"C:\Users\Your Name\iCloudDrive\My Images"
output_folder = r"C:\Users\Your Name\iCloudDrive\Converted Images"
```

Run the script to convert all eligible files in the `input_folder` to PNG and save them in the `output_folder`.

---

## Troubleshooting

- **Error: "No module named PIL"**: Install Pillow with:
  ```bash
  pip install pillow
  ```
- **File Format Not Supported**: Ensure the format is listed in the `endswith` check within the script.
- **Path Issues**: Use raw strings (`r"..."`) for paths containing backslashes or spaces.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
