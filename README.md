## Flask OpenAI Text Completion Application
This is a Flask application that uses the Azure OpenAI API to generate text completions based on user input. The application is designed to take a series of prompts from the user and generate a story based on these prompts.

## Getting Started
To get started with this application, you need to clone the repository to your local machine and install the necessary dependencies.

## Prerequisites
You need to have Python installed on your machine. You also need to install the necessary Python packages. You can do this by running the following command in your terminal:

`pip install -r requirements.txt`
`source env/bin/activate`

## Setting Up
Before running the application, you need to set up the necessary environment variables. You need to set the OPENAI_API_KEY environment variable with your OpenAI API key. You can do this in your terminal as follows:

`export OPENAI_API_KEY=your_api_key`

Replace `your_api_key` with your actual OpenAI API key.

## Running the Application
To run the application, navigate to the directory containing the app.py file in your terminal and run the following command:

`python app.py`

The application will start running on http://localhost:8000.

## Usage
Navigate to `http://localhost:8000` in your web browser. If you make a POST request to this URL with a form containing fields for "title", "name", "tone", "creature", and "environment", the application will generate a story based on these prompts and display it on the page

## Contributing
Contributions are welcome. Please feel free to submit a pull request or open an issue.
