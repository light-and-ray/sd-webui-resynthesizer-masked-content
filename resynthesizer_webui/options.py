from modules import shared
from modules.processing import StableDiffusionProcessingImg2Img
import gradio as gr


def getResynthesizerUpscaler(p: StableDiffusionProcessingImg2Img = None):
    if hasattr(p, 'override_settings'):
        overriden = p.override_settings.get("resynthesizer_upscaling", None)
        if overriden:
            return overriden
    res = shared.opts.data.get("resynthesizer_upscaling", "ESRGAN_4x")
    return res


def getResolution(p: StableDiffusionProcessingImg2Img = None):
    if hasattr(p, 'override_settings'):
        overriden = p.override_settings.get("resynthesizer_resolution", None)
        if overriden:
            return overriden
    res = shared.opts.data.get("resynthesizer_resolution", 512)
    return res



resynthesizer_settings = {
    'resynthesizer_upscaling': shared.OptionInfo(
            "ESRGAN_4x",
            "Upscaler for resynthesizer masked content",
            gr.Dropdown,
            lambda: {"choices": [x.name for x in shared.sd_upscalers]},
        ).info("I recommend to use Waifu2x upscaler from extension, because it's very fast and good enough for this purpose"),

    'resynthesizer_resolution': shared.OptionInfo(
            512,
            "Resolution for resynthesizer masked content",
            gr.Slider,
            {
                "minimum": 256,
                "maximum": 2048,
                "step": 8,
            },
        ).info("Despite resynthesizer is not a NN algorithm, it's too slow on big resolutions"),
}

shared.options_templates.update(shared.options_section(('extras_inpaint', 'Extras Inpaint'), resynthesizer_settings))

