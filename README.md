# Energy_Data_Visualization
===================================
## Introduction

This project is aimed at __providing a visualization tool for the data of energy consumption__ at Luther College.

By utilizing data from the water/electricity/heat monitoring devices throughout the campus, I have built a simple web application to display energy data from database using different types of graphs.

The programming languages and tools that I use include __Python, Django, Javascript, Chartjs, HTML, CSS__.

The work is supervised by Dr. Roman Yasinovskyy and Dr. Philip Iversen.

===================================
## Installation Requirements

### 1. Install Django using pip (recommended):

` python -m pip install Django `

### 2. Install Chartjs
There are several ways to install Chartjs. Since I do not use any front-end web framework, include the CDN is enough. Include this in your HTML file

` <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script> `

===================================
## How it works

With the data given by the professors, I import it into the database (SQLite) represented as Django Models. From these models, I send the data to the front-end under JSON format so that it can be manipulated by Javascript. The JSON object is extracted and filtered to provide appropriate data for the graphs using Chartjs. 
