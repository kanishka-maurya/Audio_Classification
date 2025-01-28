import setuptools

# reading README.md file
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

# metadata of package
REPO_NAME = "AUDIO_VISION"
NAME = "audioClassification"
__VERSION__ = "0.0.0"
AUTHOR_NAME = "kanishka-maurya"
AUTHOR_EMAIL_ID = "kanishkamauryaofficial@gmail.com"

setuptools.setup(
    name = NAME,
    version = __VERSION__,
    description = "Audio classification by leveraging image data obtained from audio data.",
    long_description = long_description,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL_ID,
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
