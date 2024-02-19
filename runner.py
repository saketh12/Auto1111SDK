import os

os.environ['COMMANDLINE_ARGS'] = "--skip-torch-cuda-test --upcast-sampling --no-half-vae --use-cpu interrogate"

from auto1111sdk import civit_download, download_realesrgan, RealEsrganPipeline, StableDiffusionPipeline, EsrganPipeline, ControlNetModel
from PIL import Image

# civit_download("https://civitai.com/models/4201/realistic-vision-v60-b1", "model.safetensors")

# pipe = StableDiffusionPipeline("model.safetensors")
# prompt = "closeup portrait photo of beautiful muslim woman, 8k uhd, high quality, cinematic"
# negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
# output = pipe.generate_txt2img(num_images = 2, prompt = prompt, height = 1024, width = 1024, negative_prompt = negative_prompt, steps = 10)
# output[0].save("huh.png")

model = ControlNetModel()

pipe = StableDiffusionPipeline("model.safetensors", controlnet=model)
prompt = "closeup portrait photo of beautiful muslim woman, 8k uhd, high quality, cinematic"
negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
output = pipe.generate_txt2img(num_images = 1, prompt = prompt, height = 512, width = 512, negative_prompt = negative_prompt, steps = 10)
output[0].save("huh.png")

