#!/usr/bin/env python
# coding: utf-8

# In[12]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import time
import os
from dotenv import load_dotenv
load_dotenv()


# In[13]:


def remove_special_characters(word):
    # Remove all non-alphanumeric characters except spaces
    return re.sub(r'[^A-Za-z0-9 ]+', '', word)


# In[14]:


def get_spotify_instance():
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope='playlist-modify-public'
    )
    
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        token_info = sp_oauth.get_access_token()
    
    return spotipy.Spotify(auth=token_info['access_token'])


# In[15]:


def safe_spotify_search(sp, query, retries=3, delay=1, max_results=200):
    results = []
    limit = 50
    offset = 0

    while offset < max_results:
        for attempt in range(retries):
            try:
                response = sp.search(q=f'track:{query}', type='track', limit=limit, offset=offset)
                tracks = response['tracks']['items']
                if not tracks:
                    print(f"No more tracks found after {len(results)} results.")
                    return results
                results.extend(tracks)
                offset += limit
                break  # Exit retry loop if successful
            except spotipy.SpotifyException as e:
                print(f"Spotify API error: {e}")
                if '401' in str(e):
                    print("Token might be invalid or expired. Refreshing token.")
                    sp = get_spotify_instance()
                time.sleep(delay * (2 ** attempt))  # Exponential backoff
        else:
            print("Failed to get a valid response from Spotify after multiple attempts.")
            return results  # Return what was gathered so far
    
    return results


# In[16]:


def create_playlist_from_sentence():
    # Prompt the user for input
    sentence = input("Please enter the sentence to create a playlist from: ")
    playlist_name = input("Please enter the playlist name: ")

    sp = get_spotify_instance()
    words = [remove_special_characters(word) for word in sentence.split()]
    track_ids = []
    i = 0
    while i < len(words):
        found_match = False
        for j in range(4, 0, -1):
            if i + j <= len(words):
                combined_word = ' '.join(words[i:i + j])
                print(f"Searching for: {combined_word}")
                results = safe_spotify_search(sp, combined_word, max_results=400)  # Set max_results to 400
                if results:
                    for track in results:
                        track_name_cleaned = track['name'].strip().lower()
                        combined_word_cleaned = combined_word.lower()
                        if track_name_cleaned == combined_word_cleaned:
                            track_ids.append(track['id'])
                            found_match = True
                            i += j - 1
                            break
                    if found_match:
                        break
                time.sleep(0.5)
        if not found_match:
            print(f"No exact match found for words: {' '.join(words[i:i + j])}")
            track_ids.append('69toZvLG490IrN6YtmN4wH')  # Placeholder track ID
        i += 1

    try:
        user_id = sp.current_user()['id']
        playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
        if track_ids:
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)
            print(f"Playlist '{playlist_name}' created successfully!")
        else:
            print("No tracks were added to the playlist.")
    except spotipy.SpotifyException as e:
        print(f"Error creating playlist: {e}")


# In[17]:


create_playlist_from_sentence()


# In[10]:





# In[ ]:




