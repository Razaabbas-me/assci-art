import cv2
import os
import time
import sys

# CONFIGURATION - No more prompts
VIDEO_PATH = r"C:\Users\DELL\Desktop\js_repo\python\vid.mp4"
WIDTH = 100  # Adjusted for better detail
ASCII_CHARS = " .:-=+*#%@"

def convert_frame_to_ascii(frame, width):
    # Calculate height based on aspect ratio (0.5 accounts for terminal character height)
    height = int(frame.shape[0] * width / frame.shape[1] * 0.5)
    resized_frame = cv2.resize(frame, (width, height))
    
    # Convert to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    # Vectorized mapping: much faster than nested loops
    # Map 0-255 to 0-9 (index of ASCII_CHARS)
    buckets = (gray_frame // 26).astype(int)
    
    ascii_rows = []
    for row in buckets:
        ascii_rows.append("".join([ASCII_CHARS[pixel] for pixel in row]))
    
    return "\n".join(ascii_rows)

def play_video():
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: File not found at {VIDEO_PATH}")
        return

    cap = cv2.VideoCapture(VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_delay = 1.0 / fps

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            ascii_art = convert_frame_to_ascii(frame, WIDTH)
            
            # Using sys.stdout.write is faster than print()
            # \033[H resets cursor to top-left without clearing the screen (prevents flicker)
            sys.stdout.write("\033[H" + ascii_art)
            sys.stdout.flush()
            
            time.sleep(frame_delay)
            
    except KeyboardInterrupt:
        print("\nPlayback stopped.")
    finally:
        cap.release()

if __name__ == "__main__":
    # Clear screen once at start
    os.system('cls' if os.name == 'nt' else 'clear')
    play_video()