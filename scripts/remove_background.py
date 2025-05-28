import argparse
import os
from datetime import datetime

from src.background_utils import BackgroundUtils


def main():
    parser = argparse.ArgumentParser(description="Remove background BackgroundUtils class")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="input image to be modified"
    )
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    parser.add_argument(
        "--output",
        type=str,
        default=f"{date_str}_generated_image.png",
        help="Output filename (default: {date}_generated_image.png)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory (default: output)"
    )

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    output_file = os.path.join(args.output_dir, args.output)

    background_utils = BackgroundUtils()
    background_utils.remove_background(
        args.input,
        output_file
    )

if __name__ == "__main__":
    main()
