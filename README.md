# CIP_WeatherApp
Final CIP project

# Table of Contents

* [Installation](#Installation)
* [Project Motivation](#Project-Motivation)
* [File Descriptions and Analyses](#File-Descriptions-and-Analyses)
* [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)


## Installation <a name="Installation"></a>
The code should run with no issues using Python versions 3.12.4 using VS Code IDE.  Requests, json, and configparser libraries were used.  An Openweathermap.org account must be created and then the API token saved in a secrets.ini config file for security.

Libraries  must be installed as below

```python
pip install requests
pip install configparser
pip install json
```

## Project Motivation <a name="Project-Motivation"></a>
For this final Stanford Code In Place project, I wanted to make a useful project that addresses a daily information need applicable to almost everyone, so I built a Weather App that displayed the temperature in degrees Celcius (metric).  I was interestested in using the Internet (via APIs from openweathermap.org), Libraries and data structures.  I explored VS Code and GitHub.  I incorporated learnings from the various lessons in the codes.   I used json; and print, round, lower and captialise functions; emojis and f-strings.  I used while loops, and try and except blocks for city name validation.   The App asks for a city and gives the weather details until "exit" is typed to exit the App.  It has the functionality to process duplicate city names in different countries such as London, US and London, GB.


## File Descriptions and Analyses <a name="File-Descriptions-and-Analyses"></a>
gitignore stores the secret files list

secret.ini stores the config files and the API key

weather_app.py stores the Python code 

## Licensing, Authors, and Acknowledgements<a name="Licensing,-Authors,-and-Acknowledgements"></a>


[GeeksforGeeks.com](https://www.geeksforgeeks.org/building-a-weather-cli-using-python/), 
[Real Python.com](https://realpython.com/build-a-python-weather-app-cli/), 
[Openweathermap.org](https://home.openweathermap.org/), 
[Youtube](https://www.youtube.com/watch?v=Y84MGU_ZL18), 
[CodeInPlace](https://codeinplace.stanford.edu/cip4/studenthome), 
[chatgpt](https://chatgpt.com/c/ea4202f0-4591-4225-bd26-2decc41c70c9), 
[Github](https://github.com/), and  
[Dataquest.io](https://www.dataquest.io/blog/python-projects-for-beginners/)


