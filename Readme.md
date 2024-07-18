# Resynthesizer as masked content

This extenstion for [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) adds new value of "Masked content" field in img2img -> inpaint tab. It uses Resynthesizer - a very old (2000 year) open-source equivalent to Adobe Photoshop's "Content-Aware Fill" feature

If you install [lama cleaner](https://github.com/light-and-ray/sd-webui-lama-cleaner-masked-content), "Resynthesizer" will appear as model in extras tab

Generally it's worse and slower then lama, but in a few scenarios if lama has some concepts which it can't remove, resynthesizer can help. Also it can on hard for surfaces e.g. grid, sand

### Example of concept which lama cannot remove:

![](/images/mask.png)

*mask*

![](/images/lama.png)

*lama*

![](/images/resynthesizer.png)

*resynthesizer*

### Links:
- python lib: https://github.com/light-and-ray/resynthesizer-python-lib
- c implementation: https://github.com/61315/resynthesizer
- original project: https://github.com/bootchk/resynthesizer

If you have problems with windows build, I would be thankful if you can fix it and make PR in [resynthesizer-python-lib](https://github.com/light-and-ray/resynthesizer-python-lib), because:
> For .dll I've used x86_64-w64-mingw32-gcc from sudo apt-get install gcc-mingw-w64 instead of gcc. It shows strange worse result on my virtual machine, I don't know why. They are the same if I build in VM using clang, or if I build it on Linux
