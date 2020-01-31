# Energy_Data_Visualization
===============================================================================
## Introduction

This project is aimed at __providing a visualization tool for the data of energy consumption__ at Luther College.

By utilizing data from the water/electricity/heat monitoring devices throughout the campus, I have built a simple web application to display energy data from database using different types of graphs.

The programming languages and tools that I use include __Python, Django, Javascript, Chartjs, HTML, CSS__.

The work is supervised by Dr. Roman Yasinovskyy and Dr. Philip Iversen.

===============================================================================

## Step-by-step Set-up

### 1. Clone the repository and enter it
` git clone https://github.com/leth02/Energy_Data_Visualization.git `
`  cd Energy_Data_Visualization `

### 2. Install Python on your machine
` sudo apt-get update `
` sudo apt-get install python3.6 `

### 3. Create a virtual environment to install required packages
` python3 –m venv .venv `
` source .venv/bin/activate `

### 4. Install Django (it is recommended to use pip)
` python3 –m pip install Django `

### 5. Include Chartjs, Momentjs, jQuery and other bootstrap packages.
I have already included all the script tags needed in the proper order (do not change the order of these script tags).

There are several ways to install Chartjs. Since I do not use any front-end web framework, include the CDN is enough.

` <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script> `

` <script type="text/javascript" src="https://cdn.jsdelivr.net/momentjs/latest/moment.min.js"></script> `

` <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script> `

### 6. Run the local server on the desired port (8000 by default)
` python3 manage.py runserver 8000 `

### 7. Open your favorite browser and go to the link at http://127.0.0.1:8000/

===============================================================================

## How it works

With the data given by the professors, I import it into the database (SQLite) represented as Django Models. From these models, I send the data to the front-end under JSON format so that it can be manipulated by Javascript. The JSON object is extracted and filtered to provide appropriate data for the graphs using Chartjs. 


![Demo Picture](/images/data_graph_demo.png)
