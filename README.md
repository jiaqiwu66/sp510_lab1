# TECHIN 510 Lab 1
## Overview

This is a profile page for Jiaqi, a UXUI designer. This website showcases my educational background, work experience, hobbies, and some interesting projects I've undertaken. See a demo here: https://sp510lab1-bjjtncbtbthqqu5tebahpf.streamlit.app/.


## How to Run
1. Clone the repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate
```
4. Activate the virtual environment
```
source venv/bin/activate
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Run the Streamlit app by executing:
```
Streamlit run app.py
```


## What's Included
- ```app.py```: The main Flask application.
- Image folder: all images used in the website.
- ```.gitignore```:tells Git which files or directories to ignore in a project.
- ```README.md```: repo overview.
- ```requreiments.txt```: include all the dependencies needed.
- ```.gitignore```:include files or directories need to ignore.

## Lessons Learned
__How to use Streamlit to create a simple website__
- Use the terminal to create a virtual environment, multi-platform collaboration, visualize images and text by coding or use existing library.

__How to use requirements.txt to manage Python dependencies__
- List all dependencies in the 'requirements.txt' file, install them by running 'pip install -r requirements.txt' in the terminal, and regular updating the file to maintain.

__How to use GitHub Actions to deploy a website to Azure App Service__
- Create a new resource group in region, a new App service, connected with GitHub repo, configuration and startup.

__Other__
- Use ```streamlit run app.py```to test for the real time interface
- Remember to stop the test using "control + C"
- Some basical terminal commend
```
git status  
git add .  
git status  
git commit -m "comments of the upadates"
git log
git pull 
git push
```
- Include these in ```.gitignore```
```
.venv
*.pyc
.DS_Store
```

## Question
- How to do centering without column？
- What if I want to make the profile picture round?
- How to add effects when sliding？
- How can I change font and size? As I only found 1 default font in the website sample. And sometimes even ```subheader``` is too large.
- How can I change the line spacing?

