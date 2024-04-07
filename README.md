# Vulnerability Analysis in Code 🕵️
Welcome to our Code Analysis and Vulnerability Prediction Tool! This web application is designed to assist developers in analyzing their code for potential vulnerabilities and predicting security issues using machine learning techniques.

## Overview 🔭
In today's software development landscape, ensuring the security of code is paramount. However, identifying vulnerabilities manually can be time-consuming and prone to oversight. Our tool aims to streamline this process by automating code analysis and providing predictive insights into potential security risks.

## Features⭐️
**1. Comprehensive Vulnerability Detection🔍**

Our tool leverages a database of 22 MITRE vulnerabilities, covering a wide range of common security issues. By analyzing code against these vulnerabilities, we provide developers with a comprehensive assessment of potential risks.

**2. Transformer Model Integration🤗**

To enhance the accuracy of vulnerability detection, we've integrated a Transformer model trained on labeled vulnerability data. This model predicts vulnerability percentages for each identified issue, helping prioritize and address high-risk areas.

**3. Power Virtual Agent (PVA) Bot for Education🤖**

Our tool includes a Power Virtual Agent (PVA) bot, trained on MITRE Att&ck website, OWASP code review guide, and Writing Secured code book by Microsoft. This bot serves as an educational resource for developers, providing insights into safe coding practices, frameworks, vulnerability details, and mitigation strategies for identified vulnerabilities.

**4. User-Friendly Interface😀**

Our web application features an intuitive and user-friendly interface, built using Python Django for the backend and HTML/CSS for the frontend. This makes it easy for developers to upload their code, initiate analysis, and interpret results. Visualizations and highlighting of vulnerable code segments aid in understanding and addressing security issues.

## Getting Started 🚀
To use our tool, follow these steps:

**Upload Code**: Navigate to our web application and upload your codebase.

**Initiate Analysis**: Start the code analysis process to identify vulnerabilities and predict security risks.

**Review Results**: Explore the analysis results, including highlighted vulnerable code segments and predicted vulnerability percentages.

**Interact with PVA Bot**: Our tool includes a Power Virtual Agent (PVA) bot, trained on MITRE Att&ck website, OWASP code review guide, and Writing Secured code book by Microsoft. This bot serves as an educational resource for developers, providing insights into safe coding practices, frameworks, vulnerability details, and mitigation strategies for identified vulnerabilities.

## Installation 🔨🔧
Our tool is accessible through a web interface, hosted on Azure App Services. No local installation is required. Simply visit [your application URL] to get started.

## Requirements 🔧
Web browser with JavaScript enabled
Stable internet connection for accessing the web application

## Technologies Used 💻

**Backend**: Python Django

**Frontend**: HTML, CSS

**Machine Learning Model**: Hugging face mrm8488/codebert-base-finetuned-detect-insecure-code from Azure Machine Learning Studio

**Database**: PostgreSQL

**Chatbot**: Power Virtual Agents

**Hosting**: Azure App Services

## Screenshots

![Screenshot 2024-04-05 141031](https://github.com/Sreya-E-P/Vulnerability-Analysis-in-Code/assets/117088162/e5e801c1-3ae6-453f-b4ab-123319d05604)
![Screenshot 2024-04-05 141215](https://github.com/Sreya-E-P/Vulnerability-Analysis-in-Code/assets/117088162/50426dd9-d30a-4fef-a673-3dd1241af04e)
![Screenshot 2024-04-05 141238](https://github.com/Sreya-E-P/Vulnerability-Analysis-in-Code/assets/117088162/dea72782-448f-440e-bd68-a527e09be1b6)
![Screenshot 2024-04-05 141428](https://github.com/Sreya-E-P/Vulnerability-Analysis-in-Code/assets/117088162/d7a96893-16af-4d3e-9aff-78c70cc5ab0b)
