# Quiz-app-in-Python
Quiz App in Python with Tkinter


This is a simple quiz application built in Python using Tkinter, a standard GUI library, and B612 Mono font for a clean and stylish look. The app reads questions, their correct answers, and alternative answers from a CSV file named questions.csv.

## How to Run the App
Make sure you have Python installed on your system.
Clone this repository to your local machine or download the source code as a ZIP file and extract it.
Install Tkinter (if not already installed):
For Windows users, Tkinter is usually included with Python by default.
For Linux users, you can install Tkinter using the package manager:

```sudo apt-get install python3-tk```

## Install required font (B612 Mono)
Download the B612 Mono font from the Google Fonts website.
Install the font on your operating system by double-clicking the downloaded font file and clicking "Install."
Place the questions.csv file in the project folder, following the format specified below.
Navigate to the project folder where the quiz.py file is located using the command line or terminal.
Run the app with the following command:

```python quiz.py```

## questions.csv Format

The questions.csv file contains the questions, correct answers, and alternative answers in the following format:

question,correct_answer,alternatives
Which one of the following is not a greenhouse gas?,N2,"CO2, N2O, CH4"
What is the largest source of marine pollution?,Plastic waste,"Oil spills, Chemical runoff, Sewage discharge"
Which renewable energy source harnesses the power of tides?,Tidal power,"Solar power, Wind power, Geothermal power"
What is the primary cause of soil erosion?,Water and wind,"Deforestation, Agricultural practices, Urbanization"
Which gas is responsible for the depletion of the ozone layer?,Chlorofluorocarbons (CFCs),"Carbon dioxide (CO2), Methane (CH4), Nitrous oxide (N2O)"
What is the process of converting sunlight into electricity called?,Photovoltaics,"Thermal power, Geothermal power, Hydropower"
Each question is represented as a row in the CSV file.
The first column represents the question.
The second column represents the correct answer.
The third column represents the alternative answers, separated by commas and enclosed in double quotes.

## Features

The app reads questions and answers from the questions.csv file, making it easy to modify and update quiz content.
Randomizes the order of options in each question to keep the quiz dynamic and engaging.
Displays the final score at the end of the quiz.

## Contribution

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
