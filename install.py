import launch

if not launch.is_installed('resynthesizer'):
    launch.run_pip('install resynthesizer -U')
