from rembg import remove
from PIL import Image
import io


class BackgroundUtils:

    background_path = ""

    def __init__(self, background_path=""):
        self.background_path = background_path

    @staticmethod
    def remove_background(input_path, output_path=None):
        try:
            # Open the input image
            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()

            # Remove background
            output_data = remove(input_data)

            # Convert to PIL Image
            output_image = Image.open(io.BytesIO(output_data))

            if output_path:
                # Save to file
                output_image.save(output_path)
                print(f"Background removed and saved to: {output_path}")
                return None
            else:
                return output_image

        except Exception as e:
            print(f"Error removing background: {str(e)}")
            return None
