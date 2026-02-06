import cv2
import os
import time
import sys
import argparse

# The set of ASCII characters used to represent shades of gray
ASCII_CHARS = " .:-=+*#%@"

def convert_frame_to_ascii(frame, width):
    """Converts a single video frame to ASCII art."""
    # Calculate the new height based on the original aspect ratio
    # and a 0.5 factor to account for terminal character height
    height = int(frame.shape[0] * width / frame.shape[1] * 0.5)
    resized_frame = cv2.resize(frame, (width, height))
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    # Map grayscale values (0-255) to the ASCII_CHARS index (0-9)
    # This is a faster, vectorized approach than using nested loops
    buckets = (gray_frame // 26).astype(int)
    
    # Create the ASCII art string
    ascii_rows = ["".join([ASCII_CHARS[pixel] for pixel in row]) for row in buckets]
    
    return "\n".join(ascii_rows)

def play_video(video_path, width):
    """Plays a video file as ASCII art in the terminal."""
    if not os.path.exists(video_path):
        print(f"Error: File not found at {video_path}")
        sys.exit(1)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        sys.exit(1)

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_delay = 1.0 / fps

    try:
        # Clear the screen once at the start
        os.system('cls' if os.name == 'nt' else 'clear')
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            ascii_art = convert_frame_to_ascii(frame, width)
            
            # Use sys.stdout.write for faster printing and to prevent flickering
            # \033[H resets the cursor to the top-left corner
            sys.stdout.write("\033[H" + ascii_art)
            sys.stdout.flush()
            
            time.sleep(frame_delay)
            
    except KeyboardInterrupt:
        print("\nPlayback stopped by user.")
    finally:
        cap.release()

def main():
    """Parses command-line arguments and starts the video playback."""
    parser = argparse.ArgumentParser(description="Plays a video file as ASCII art in the terminal.")
    parser.add_argument("-f", "--file", dest="video_path", required=True,
                        help="Path to the video file.")
    parser.add_argument("-w", "--width", dest="width", type=int, default=100,
                        help="Width of the ASCII art in characters (default: 100).")
    
    args = parser.parse_args()
    
    play_video(args.video_path, args.width)

if __name__ == "__main__":
    main()