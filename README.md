## Project Repository
Author: Kyriakos Papadopoulos

### Introduction
This is my personal repository where I publish my Data Science related projects. The projects in this repository are meant to showcase my progress through my Data Science journey. For more information about me, feel free to look at my LinkedIn profile.

### Repository Structure
This repository is organized as follows:

- README.md
- .gitignore.txt
- `UTM Link Generator`: This project was initiated to address practical challenges faced by some of my less tech-savvy colleagues who were struggling to understand and create links with UTM parameters for our advertising campaigns.
- `Data_Science_Bootcamp`: Container for projects undertaken as part of Big Blue Data Academy's Data Science Bootcamp.
  - `Interactive Dashboard project`: Utilizing a dataset comprising patient data, including risk factors and lung cancer diagnoses, my team conducted an analysis to examine the relationship between these factors and lung cancer outcomes.
  - `Clustering Project`: Using a dataset containing audio features for the top 2,000 songs on Spotify, our team sought to identify patterns and group similar songs to inform marketing strategies, optimize playlist curation, and enhance audience engagement.
- `API_Projects`: Container for API related projects.
  - `Spotify`:
    - `Text_2_Playlist`: This program interacts with the Spotify Web API to create a playlist based on a sentence provided by the user. The program attempts to find songs whose titles match the words in the sentence. If a match is found, the song is added to a new Spotify playlist. If no match is found for a word, the program adds a placeholder track.
  - `Reddit`:
    - `Photography_Analysis`: WIP

### How to Navigate
- Each project is organized within its own folder.
- Inside each project's folder, you will find the project's documentation and data.

### Technologies Used
- **Jupyter Notebooks**: For interactive data analysis and visualization.
- **Python**: Core language for scripting and automation.
  - **Seaborn**: For statistical data visualization.
  - **Matplotlib**: For creating static, animated, and interactive visualizations in Python.
  - **Pandas**: For data manipulation and analysis.
  - **NumPy**: For numerical computations.
  - **Plotly Express**: For creating interactive visualizations.
  - **Dash**: For building web applications and dashboards.
    - **Dash Core Components (dcc)**: Provides interactive components like dropdowns, graphs, and sliders.
    - **Dash HTML Components (html)**: Allows the use of HTML elements within Dash applications.
    - **Dash Dependencies**: Manages interactivity and callbacks within Dash applications.
  - **WordCloud**: For generating word cloud visualizations from text data.
  - **Scikit-learn**: A machine learning library in Python.
    - **StandardScaler**: For standardizing features by removing the mean and scaling to unit variance.
    - **PCA (Principal Component Analysis)**: For dimensionality reduction by transforming features.   
    - **KMeans**: For clustering data into a predefined number of groups.
    - **Feature Extraction (text)**: For converting text data into numerical data suitable for machine learning.
  - **Threading**: For managing concurrent execution of tasks.
  - **Webbrowser**: For opening web browsers and automating tasks involving web content.
  - **Spotipy**: For interacting with the Spotify Web API to search for tracks, manage playlists, and more.
  - **python-dotenv**: For loading environment variables from a `.env` file to securely manage API credentials.
  - **Re (Regular Expressions)**: For text processing and manipulating strings by pattern matching.
  - **Praw**: For accessing and interacting with Reddit’s API to collect and analyze data.
  - **Requests**: For sending HTTP requests and interacting with web services and APIs.
  - **Pillow (PIL)**: For opening, manipulating, and saving image files in various formats.
  - **BytesIO**: For handling binary data and working with in-memory streams.
  - **Datetime**: For manipulating dates and times in Python.
  - **OS**: For interacting with the operating system, including file and directory manipulation.
  - **Hashlib**: For creating secure hash values (e.g., MD5, SHA-1) from data.
  - **Time**: For time-related functions, such as pausing the execution of code or getting the current time.
- **SQL**: For data acquisition.
