import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README2.md").read_text()

setuptools.setup(
  name="charnstr",
  version="0.0.4",
  author="Sparisoma Viridi",
  url='https://github.com/dudung/charnstr',
  description="Analyze a string for its characters information",
  long_description=long_description,
  long_description_content_type='text/markdown',
  packages=["charnstr"]
)
