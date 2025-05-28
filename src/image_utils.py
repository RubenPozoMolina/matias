import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler


class ImageUtils:

    model = None
    pipeline = None

    def __init__(self, model="stabilityai/stable-diffusion-2-1"):
        self.model = model
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            self.model,
            torch_dtype=torch.float16
        )
        self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
            self.pipeline.scheduler.config,
            use_karras_sigmas=True,
            algorithm_type="dpmsolver++"
        )
        self.pipeline = self.pipeline.to("cuda")

    def generate_image(self, prompt, negative_prompt, output_file):
        image = self.pipeline(
            prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=50,
            guidance_scale=7.5
        ).images[0]
        image.save(output_file)

