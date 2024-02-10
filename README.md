
# Strip Stitcher

Welcome to Strip Stitcher, a creative Python tool born from the viral concept of 'dog breeder by picture shredding.' Inspired by a popular internet meme, this project was developed during "Artificial Intelligence - Beginner Studies" and offers a playful twist on image processing. It transforms any photo into a piece of striped art by simulating a shredding effect and then reassembling it to create a unique patterned image.

## Motivation

The Strip Stitcher is designed to merge the worlds of art and programing, demonstrating how an image can be algorithmically shredded into strips and then reconstructed. The project showcases the power of image manipulation techniques and their potential to create new forms of visual art.

## Features

- Transforms images into vertically and horizontally striped versions.
- Configurable stripe patterns through an easy-to-edit `config.json` file.
- The project pays homage to the 'dog breeder by picture shredding' meme, adding a touch of humor and contemporary culture to the AI studies.

## Setup

To get Strip Stitcher up and running on your machine, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/[Your_GitHub_Username]/Strip_Stitcher.git
   cd Strip_Stitcher
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS or Linux
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Adjust the number of stripes in the `config.json` file:
```json
{
    "num_horizontal_stripes": 50,
    "num_vertical_stripes": 50
}
```

### Usage

1. Place the image you want to process in the `data` folder and rename it to `image.jpg`. The default image provided is for demonstration purposes; replace it with any image you wish to stripe.
2. Execute the script:
   ```bash
   python main.py
   ```
3. The processed image will be saved as `shredded_and_reassembled_image.jpg` in the `data` folder, demonstrating the program's capability.

## Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspiration from the 'dog breeder by picture shredding' meme.
- Anyone whose code was used as a reference.
- The AIUA community for their support in artificial intelligence studies.
