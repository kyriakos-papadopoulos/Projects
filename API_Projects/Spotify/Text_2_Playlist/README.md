# Spotify Playlist Creator from Sentence

This Python program interacts with the Spotify Web API to create a playlist based on a sentence provided by the user. The program attempts to find songs whose titles match the words in the sentence. If a match is found, the song is added to a new Spotify playlist. If no match is found for a word, the program adds a placeholder track.

## Features

- **API Interaction**: Utilizes the Spotify Web API to search for tracks and create playlists.
- **Sentence to Playlist**: Converts a sentence into a playlist by searching for songs that match the words in the sentence.
- **Contextual Search**: Attempts to find matches for up to six consecutive words in the sentence to increase the likelihood of finding relevant tracks.
- **Dynamic Configuration**: Tries different configurations of word combinations to maximize the number of matched tracks.
- **Optimal Matching**: Selects the configuration with the fewest unmatched words to create the most accurate playlist.
- **Placeholder Track**: Adds a placeholder track when no exact match is found for a word or combination of words.
- **Token Management**: Handles Spotify OAuth token retrieval and caching.

## Prerequisites

- Python 3.x (Developed with Python 3.7.6)
- `spotipy` library
- Spotify Developer account with a registered application

## Installation

1. **Install Dependencies**:
    ```bash
    pip install spotipy python-dotenv
    ```

2. **Set Up Spotify API Credentials Using a `.env` File**:
    - Create a `Spotify` developer application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    - Obtain your `client_id`, `client_secret`, and set the `redirect_uri` to match the one used in your code.
    - In the root directory of your project (where your Jupyter Notebook or script is located), create a `.env` file with the following content:
      ```plaintext
      SPOTIPY_CLIENT_ID=your_client_id
      SPOTIPY_CLIENT_SECRET=your_client_secret
      SPOTIPY_REDIRECT_URI=your_redirect_url
      ```
    - Replace `your_client_id`, `your_client_secret`, and `your_redirect_url` with your actual Spotify credentials.

## Usage

1. **Run the Program**:
    ```bash
    python psycho_playlists.py
    ```

2. **Input Sentence and Playlist Name**:
    - The program will prompt you to enter a sentence. This sentence will be used to create the playlist.
    - You will also be asked to provide a name for the new playlist.

3. **Program Workflow**:
    - The program will clean the sentence, removing any special characters.
    - The program will attempt to find songs for each word or combination of words in the sentence, trying different configurations of up to six consecutive words.
    - It will evaluate each configuration by counting the number of unmatched words, aiming to minimize unmatched words in the final playlist.
    - If no exact match is found for a word or combination of words, a placeholder track is added to the playlist.
    - The configuration with the fewest unmatched words is selected, and the playlist is created based on that configuration.

4. **View Your Playlist**:
    - Once the program completes, you can view the playlist in your Spotify account.

## Example

Here is an example of the program in action:

1. **Input**:
    - Sentence: "Hello, this is a test playlist!"
    - Playlist Name: "Hello World"

2. **Output**:
    - A Spotify playlist named "Hello World" is created, containing the tracks: "Hello", "This Is A Test", and "PLAYLIST"

## Code Overview

### Functions

- **`remove_special_characters(word)`**: Removes non-alphanumeric characters except spaces from the input word.
- **`get_spotify_instance()`**: Handles Spotify API authentication and token management.
- **`safe_spotify_search(sp, query, retries=3, delay=1, max_results=200)`**: Searches Spotify for tracks matching the query, with error handling and retry logic.
- **`create_playlist_from_sentence()`**: Main function that prompts the user for input, processes the sentence, searches for matching tracks, and creates a playlist.

## Known Issues

- Small or common words might not return the correct results due to the limitations of the Spotify API.
- The search method might miss tracks that are not among the top results returned by the API.
- Unpredictable behavior may occur depending on the maximum number of words the algorithm is allowed to join when searching for tracks. In some cases, this may lead to the program either missing relevant tracks or incorrectly matching tracks, especially when the combined word sequence results in unexpected search results.

## Future Enhancements

- Implement a more sophisticated search mechanism to handle common and small words better.
- Improve error handling and user feedback when no matching tracks are found.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Spotipy Library](https://spotipy.readthedocs.io/)
