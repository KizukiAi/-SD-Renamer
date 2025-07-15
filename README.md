A Python utility to rename Stable Diffusion output files to match their original filenames, using different sorting criteria for each directory.

Features
- Matches filenames between source and target directories

- Source files sorted alphabetically (A-Z)

- Target files sorted by modification date (oldest first)

- Preserves original file extensions

-  Built-in safety checks:

Verifies directory existence

- Checks file count matching

- Handles naming conflicts

- Detailed console output


Use Case
Perfect for when Stable Diffusion's upscaler/img2img batch suddenly changes your filenames and you need to:

- Match hi-res outputs with their original low-res versions

- Maintain consistent naming throughout the process

- Organize for before/after comparisons


Installation
Clone the repository:

bash
git clone https://github.com/yourusername/StableDiffusion-Renamer.git
cd StableDiffusion-Renamer
Ensure Python 3.7+ is installed


Usage
Edit SD-Renamer.py and set your paths:

python
source_dir = r"ENTER_TARGET_PATH_HERE"  # Directory with original filenames
target_dir = r"ENTER_TARGET_PATH_HERE"  # Directory with files to be renamed
Run the script:

bash
python SD-Renamer.py


Example
Before:

/lowres/
   image1.png
   image2.png
   image3.png

/hires/ (sorted by date)
   oldest.png
   middle.png
   newest.png
   
After running:

/hires/
   image1.png
   image2.png
   image3.png

   
Safety Notes
Always backup your files before running
The script includes safety checks but cannot recover files after renaming.

License
MIT License - see LICENSE file for details
