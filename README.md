# ASCII Art Video Player

This project is a command-line tool that converts a video file into ASCII art and plays it in the terminal.

## Prerequisites

*   Python 3.x
*   OpenCV for Python

## Installation

1.  Clone this repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd <repository-directory>
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To play a video file, run the `index.py` script with the following command-line arguments:

```bash
python index.py -f <path-to-video-file> -w <width-of-ascii-art>
```

### Arguments

*   `-f`, `--file`: Path to the video file (e.g., `vid.mp4`).
*   `-w`, `--width`: Width of the ASCII art in characters (e.g., `100`).

### Example

```bash
python index.py -f vid.mp4 -w 100
```

Press `Ctrl+C` to stop the playback.
