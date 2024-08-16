# Spotify Wrapped Playlists & Cover Generation

## Overview

This project creates custom monthly Spotify playlists based on your listening history and generates unique playlist covers for each month. The process is divided into two main parts: generating playlists and creating covers. Below is an overview of the necessary assets, workflow, features, prerequisites, and future plans.

## Features

- **Automated Playlist Creation**: Automatically generates monthly Spotify playlists based on your streaming history.
- **Custom Cover Generation**: Creates unique, visually appealing covers for each playlist using gradient noise backgrounds.
- **Dynamic Font Selection**: Automatically selects between black or white text for maximum contrast and readability.
- **Color Uniqueness**: Ensures that no two playlist covers use similar colors, enhancing visual distinction.
- **Data Persistence**: Intermediate data (like track information and streaming history) is saved to pickle files for easy re-use and modification.

## Prerequisites

Before running this project, ensure that you have the following:

- **Spotify Developer Account**: Needed to obtain your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`.
- **Python 3.7+**: The project is developed using Python and requires version 3.7 or later.
- **Spotify Data**: You need access to your Spotify streaming history files, typically named `StreamingHistory_music*.json`.
- **Spotipy Library**: For interacting with the Spotify API.

## Dependencies

Make sure to install the following Python packages before running the notebooks:

- **spotipy**: For interacting with the Spotify API.
- **pandas**: For data manipulation.
- **numpy**: For numerical operations, particularly in image processing.
- **Pillow**: For image creation and manipulation.
- **dotenv**: For environment variable management.
- **tqdm**: For progress bars in loops.
- **requests**: For making HTTP requests.

## Assets Needed

### Notebooks
- **wrapped_months.ipynb**: Handles the extraction of Spotify listening history, the creation of monthly playlists, and querying additional track information from the Spotify API.
- **cover_generation.ipynb**: Generates unique covers for each playlist by creating gradient noise backgrounds and applying appropriate font styles.

### Fonts
The project includes several fonts stored in the `fonts` directory. The current implementation uses `paskowy.ttf`. Other fonts included are:
- DRUNKFONTS-Regular.otf
- Kage Retro.otf
- Squealer Embossed.otf
- Break gothic.ttf
- Super Magic.ttf

You can switch to any of these fonts by adjusting the `font_path` in the script.

## Workflow

1. **Run the `wrapped_months` Notebook**:
   - This notebook will automatically create Spotify playlists for each month based on your streaming history.
   
2. **Run the `cover_generation` Notebook**:
   - This will generate unique covers for each playlist. The covers are saved locally and need to be manually added to the playlists on Spotify.

## Detailed Description of the Process

### wrapped_months Notebook

The notebook performs the following steps:
1. **Streaming Data Loading**:
   - Loads your Spotify streaming history from specified JSON files.
   - Merges data from multiple files and creates a DataFrame for easy manipulation.

2. **Spotify API Integration**:
   - Connects to Spotify using `spotipy` and OAuth for querying track information.
   - Retrieves track duration and Spotify IDs for each track in your history.

3. **Playlist Creation**:
   - Groups your streaming history by month and year.
   - Creates a playlist for each month containing the top 20 tracks based on playtime.

4. **Data Storage**:
   - Saves various stages of data processing to pickle files for later use.

### cover_generation Notebook

This notebook generates the playlist covers with the following steps:
1. **Unique Color Generation**:
   - Randomly generates unique colors for each year, ensuring no two similar colors are used.

2. **Gradient and Noise Application**:
   - Creates a gradient between two randomly selected colors for each cover.
   - Applies a noise texture to make each cover unique and visually appealing.

3. **Text Visibility Optimization**:
   - Automatically selects black or white text for each cover based on the background contrast, ensuring maximum readability.

4. **Saving Covers**:
   - Saves the generated covers in the `covers` directory.

## Future Plans

- **Automate Cover Upload**:
   - The current API functionality does not support automatic cover uploads. In the future, the goal is to integrate this feature once it becomes available or find alternative methods.

## Acknowledgements

- **ChatGPT**: Assisted in developing the cover generation notebook and creating this README file.

## Note

For any changes or customizations:
- You can modify the font used by changing the `font_path` variable in the `cover_generation.ipynb`.
- The script currently defaults to using `paskowy.ttf` for generating playlist covers.

## Running the Project

To get started:
1. Clone the repository to your local machine.
2. Install the required Python packages listed in the dependencies section.
3. Run the notebooks in the specified order.
