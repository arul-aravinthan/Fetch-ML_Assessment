# Fetch-ML-Assessment

## Two Options to run the code:

### Option 1: Docker

1. Run docker pull arularavinthan/fetch-ml_assessment:latest in command line.
2. Run docker run -p 7860:7860 arularavinthan/fetch-ml_assessment:latest

### Option 2: VirtualEnv

1. Clone the repository, and make sure you have python3 installed.
2. (Optional) Create a virtualenv using 'virtualenv venv', then do 'source ./venv/bin/activate'
3. Run 'python -m pip install -r requirements.txt' (or do 'python -m pip install torch pandas numpy gradio')
4. Run 'python model.py', and follow the link to see application. 
