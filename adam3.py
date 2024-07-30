import os
import asyncio
import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth


auth = SpotifyOAuth(client_id='6a3e8ace6fcb458fa723085e6a2f1766',
                        client_secret='312e2ae6504c4d44a0f0c622b5e7b4ca',
                        redirect_uri='http://localhost:8888/callback?code=AQBo82M-dWuhAYAjhJjbIaxXRsfSOBtCAX4GesBa_t4MLW87KzziIUOc0LlkZt0QzB8Pr1C-hIPBhIn1qtPsAg9dvXUOyJTDBjTYxPTDnzKGFPmCYEIOrIMpSxffarZI0MPeoMnygKT69mt1xf-XkdAF54mj7yy2aaR10G5m6ZxEtA')
sp = spotipy.Spotify(auth_manager=auth)

sp.current_user_follow_playlist("38IryVuUHgLSgOfwpJwXVe")