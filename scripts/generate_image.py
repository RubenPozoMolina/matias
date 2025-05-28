import argparse
import os
import sys
from datetime import datetime

from src.image_utils import ImageUtils


def main():
    """
    Main function to generate images using ImageUtils class with command-line parameters
    """
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Generate images using ImageUtils class")
    parser.add_argument(
        "--model",
        type=str,
        default="stabilityai/stable-diffusion-2-1",
        help="Model name to use for image generation (default: stabilityai/stable-diffusion-2-1)"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Text prompt for image generation"
    )
    parser.add_argument(
        "--negative-prompt",
        type=str,
        default="blurry, low quality, distorted, deformed, disfigured, bad anatomy, bad proportions, extra limbs, cloned face, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, mutated hands, poorly drawn hands, poorly drawn face, mutation, ugly, bad art, beginner, amateur, distorted face",
        help="Negative prompt to avoid unwanted features (default: comprehensive quality/anatomy terms)"
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

    # Parse arguments
    args = parser.parse_args()

    # Check if CUDA is available
    import torch
    if not torch.cuda.is_available():
        print("Warning: CUDA is not available. This may run very slowly on CPU.")

    try:
        # Initialize ImageUtils with specified model
        print(f"Initializing ImageUtils with model: {args.model}")
        image_generator = ImageUtils(model=args.model)
        print("ImageUtils initialized successfully!")

        # Create output directory if it doesn't exist
        os.makedirs(args.output_dir, exist_ok=True)

        # Prepare output file path
        output_file = os.path.join(args.output_dir, args.output)

        print(f"\nGenerating image with prompt: '{args.prompt}'")
        print(f"Saving to: {output_file}")

        # Generate image
        image_generator.generate_image(
            args.prompt,
            args.negative_prompt,
            output_file
        )
        print(f"✓ Image generated successfully and saved to: {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure you have:")
        print("1. CUDA-compatible GPU with sufficient memory")
        print("2. Required packages installed (torch, diffusers)")
        print("3. Stable internet connection for model download")
        print("4. Valid model name")
        sys.exit(1)


if __name__ == "__main__":
    main()