Automated Kaggle Dataset Analysis Pipeline:

⚙️ Overview:
This is a python-based automation project that searches the datasets on Kaggle first, then downloads it, further processes it and then finally generates a report highlighting the features of the dataset using CLI command.

This project shows automation using API, data analysis and reporting in a modular way.

✨ Key Features:
•	Automated dataset search and download using Kaggle API
•	Automatic CSV file detection
•	Processing (Summary Statistics and missing values)
•	HTML report 
•	CLI based execution
•	Centralized logging for better debugging.

📌 Stack
•	Python
•	Kaggle API
•	pandas, numpy
•	matplotlib, seaborn
•	Jinja2
•	Argparse, logging

Project Strucutre
 

📦 Setup:
1.	Create virtual environment and install dependencies from requirements.txt using 🛠️
	pip install -r requirements.txt

2.	Configure Kaggle for API 🌐:
	Login to Kaggle
	Download Kaggle.json and configure by placing it on
	C:\Users\<username>\.kaggle\kaggle.json (For Windows)
3.	Finally run ▶️:
	Python main.py –query iris 	# or any dataset of interest
📈 Output
•	Downloaded dataset (CSV)
•	Visual images
•	Logs
•	Analysis Report
📊 Improvements
•	Email automation
•	Dockerization

Author
Sabin Shahi
🐙Github: https://github.com/sabinshahi-code
🧑‍💼LinkedIn: https://www.linkedin.com/in/sabin-shahi-5435a133b/
📧 Gmail: ss.sabin.shahi@gmail.com
