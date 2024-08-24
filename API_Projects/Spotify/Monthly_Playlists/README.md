# Spotify Wrapped Playlists & Cover Generation

## Overview

This project automates the creation of monthly Spotify playlists based on your listening history and generates unique playlist covers for each month. The process is divided into two main parts: generating playlists and creating covers.

## Features

- **Automated Playlist Creation**: Automatically generates monthly Spotify playlists based on your streaming history.
- **Custom Cover Generation**: Creates unique, visually appealing covers for each playlist using radial gradient backgrounds with added noise texture.
- **Dynamic Font Selection**: Automatically selects between black or white text for maximum contrast and readability.
- **Color Uniqueness**: Ensures that no two playlist covers use similar colors, enhancing visual distinction.
- **Playlist Exclusion**: Optionally excludes songs from specific playlists in your Spotify library from the analysis.

## Prerequisites

Before running this project, ensure that you have the following:

- **Spotify Developer Account**: Needed to obtain your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`.
- **Python 3.7+**: The project is developed using Python and requires version 3.7 or later.
- **Spotify Data**: You need access to your Spotify streaming history files, typically named `StreamingHistory_music*.json`. After receiving and downloading your data, add the path to your `.env` file as `EXPORT_PATH`.
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
- **matplotlib**: For displaying images in Jupyter Notebooks.

## Assets Needed

### Notebooks

- **wrapped_months.ipynb**: Handles the extraction of Spotify listening history, the creation of monthly playlists, and querying additional track information from the Spotify API.
- **cover_generation.ipynb**: Generates unique covers for each playlist by creating radial gradient backgrounds with added noise texture.

### Fonts

The project includes several fonts stored in the `fonts` directory. The current implementation uses `paskowy.ttf`. Other fonts included are:

- `DRUNKFONTS-Regular.otf`
- `Kage Retro.otf`
- `Squealer Embossed.otf`
- `Break gothic.ttf`
- `Super Magic.ttf`

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

3. **Playlist Exclusion**:
   - Searches your library for specific playlists and collects the song IDs within.
   - Filters the final DataFrame to exclude these songs from the grouping.

4. **Playlist Creation**:
   - Groups your streaming history by month and year.
   - Creates a playlist for each month containing the top 20 tracks based on playtime.

5. **Data Storage**:
   - Saves the final dataframe as a pickle file for use in the cover_generation notebook.


### cover_generation Notebook

This notebook generates the playlist covers with the following steps:

1. **Unique Color Generation**:
   - Generates unique vibrant color pairs for each year, ensuring no two similar colors are used.

2. **Radial Gradient and Noise Application**:
   - Creates a radial gradient between two randomly generated colors for each cover.
   - Applies a noise texture to make each cover unique and visually appealing.

3. **Text Visibility Optimization**:
   - Automatically selects black or white text for each cover based on the background contrast, ensuring maximum readability.

4. **Saving Covers**:
   - Saves the generated covers in the `covers` directory.

## Known Issues

### Differences Between General Spotify Data Export and Extended Streaming History Export

When creating Spotify playlists based on your streaming history, the choice between using the general Spotify data export and the extended streaming history export has significant implications:

1. **Data Coverage and Track IDs**:
   - The **general Spotify data export** provides streaming data for only the past year and lacks Spotify track IDs within the streaming history files. Track IDs are crucial for accurately adding songs to playlists. Without these IDs, it becomes necessary to use the Spotify API's search endpoint, which relies on matching tracks based on a combination of track names and artist names.
   - The **extended streaming history export** offers a more comprehensive dataset, including several years of streaming history along with Spotify track IDs. This allows for the direct use of these IDs to generate playlists, avoiding the need for additional searches.

2. **Search Endpoint Limitations**:
   - When the search endpoint is used due to the absence of track IDs in the general export, there is a risk of retrieving incorrect tracks. The search function might return the wrong track, such as a remix, live version, or an entirely different song with a similar name, leading to inaccuracies in the generated playlists.
   - Additionally, frequent API queries to retrieve track IDs can lead to hitting Spotify's rate limits, which may temporarily block further requests and delay the playlist creation process.

3. **Track Relinking and ID Discrepancies**:
   - In the **extended streaming history export**, the track IDs might differ from those obtained through the search endpoint, particularly for older tracks. However, Spotify's track relinking feature helps mitigate issues related to regional availability. Track relinking allows Spotify to automatically link different instances of a track—each associated with different licenses or markets—so that when a user tries to play a track unavailable in their market, Spotify attempts to play another available instance of the same track. This ensures that using older track IDs from the extended export will still correctly add the appropriate, currently available track to your playlists.

Due to these reasons, the current script is set to work only with the **Extended Streaming History Dataset**. Using the general export dataset will not work because it lacks track IDs, and the search capability has been removed due to the aforementioned problems.

## Future Plans

- **Automate Cover Upload**:
  - The API does not support uploading the current generated covers. In the future, the goal is to integrate this feature once it becomes available or find alternative methods.

- **More Segmentation Options**:
  - Instead of automatically grouping tracks by month, users will be able to choose alternative options such as weekly segments or seasonal groupings like summer, winter, etc. This enhancement will allow for even more personalized and diverse playlist creation.

## Acknowledgements

- **ChatGPT**: Assisted in developing the cover generation notebook.

## Note

For any changes or customizations:

- You can modify the font used by changing the `font_path` variable in the `cover_generation.ipynb`.
- The script currently defaults to using `paskowy.ttf` for generating playlist covers.

## Running the Project

To get started:

1. Clone the repository to your local machine.
2. Install the required Python packages listed in the dependencies section.
3. Run the notebooks in the specified order.
