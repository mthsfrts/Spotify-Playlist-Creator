# Code Libraries

from searchs import SpotifyClient
from dataframes import SpotifyDataFrame

# Style Libraries

import time
import random
from colorama import Fore

# Instances

sp = SpotifyClient()
df = SpotifyDataFrame()

# -------------------------------------------------------------------

# Load Users Data

user = sp.me()
username = user['username']
user_id = user['id']
user_ct = user['country']
user_followers = user['followers']

# Greeting the User

print('Hey ' + f'{Fore.LIGHTBLUE_EX + username}' + Fore.RESET + '!!')
print(Fore.RESET + 'Welcome to the ' + Fore.RED + 'BEST' + Fore.RESET + Fore.GREEN + ' Spotify Tool'
      + Fore.RESET + ' that you will find online!')
print('Here is some of your stats on Spotify:')
print('Here is your ID: ' + f'{Fore.LIGHTBLUE_EX}{user_id}')
print(Fore.RESET + 'Your number of followers: ' + f'{Fore.LIGHTBLUE_EX}{user_followers}')
print(Fore.RESET + 'Your country: ' + Fore.LIGHTBLUE_EX + user_ct)
time.sleep(1)
print()
print(Fore.RESET + 'Now let me tell you how you can access some neat features that Spotify wont show to you.')
print()

while True:

    # Starting the Code

    print(Fore.RESET + 'Just choose a number from the list below, and I will do my magic!')
    print()
    print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Want just a quick search?')
    print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - Want to know everything?')
    print(Fore.LIGHTBLUE_EX + '3' + Fore.RESET + ' - Want some recommendations?')
    print(Fore.LIGHTBLUE_EX + '4' + Fore.RESET + ' - Want to know some new releases?')
    print(Fore.LIGHTBLUE_EX + '5' + Fore.RESET + ' - If you are a musician or a dj, hit me ')
    print(Fore.LIGHTBLUE_EX + 'x' + Fore.RESET + ' - Want to exit?')
    print()
    print()
    choice = input('Now your turn, ' + f'{Fore.LIGHTBLUE_EX + username}'
                   + Fore.RESET + ', what can I do for you today? ')

    # Choices

    if choice == '1':
        print()
        print('Cool, just a quickie. But first I need to know their name!')
        time.sleep(1)
        artist_input = input(Fore.LIGHTRED_EX + 'Enter the Name of the Artist : ')
        time.sleep(1)
        print()

        # Response

        print(
            Fore.RESET + 'Niiiiiice, ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + Fore.RESET +
            ' it is. Let me do my thing ! I will be right back with the results!')
        print()
        print()
        time.sleep(2)
        print('Here just some light result about ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + Fore.RESET +
              ', for you!')
        print()

        # Setting Up Variables with DataFrame Attributes

        artist = sp.artist(artist_input)

        artist_id = artist['id']

        # Setting Up DataFrame

        artist_df = artist['artist_df']

        #

        print()
        time.sleep(1)
        print(Fore.LIGHTYELLOW_EX + f'{artist_df.to_string(index=False)}')
        print()
        print()
        print(Fore.RESET + 'Now, here are some of ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + '`s' +
              Fore.RESET + ', ' + 'Top Tracks')
        time.sleep(1)
        print()

        # Setting Up New Variables for insert into the query

        top_track_input = ''.join(artist_id)

        # Query

        top_track = sp.top_tracks(f'{top_track_input}')

        # DataFrame

        top_df = top_track['top_df']

        #

        print((Fore.LIGHTYELLOW_EX + f'{top_df.to_string(index=False)}'))
        print()
        time.sleep(2)
        print(Fore.RESET + 'Wow that was quick! Did I found what you were looking for?')
        time.sleep(1)
        print()
        print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
        print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
        print()
        response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')

        if response == '1':
            print(Fore.RESET + 'Cool, glad that I helped! Do you want some recommendations?')
            time.sleep(1)
            print()
            print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
            print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
            print()
            response_1_1 = input(Fore.LIGHTRED_EX + 'Enter your answer: ')

            if response_1_1 == '1':
                print(Fore.RESET + 'Here some tracks that you might want to look into.')
                print()
                time.sleep(1)

                # Setting Up New Variables for insert into the query

                seed_artist = ','.join(artist_id)

                top_track_id = top_track['id']
                randomization_track = random.sample(top_track_id, 1)
                seed_track = ','.join(randomization_track)

                seed_genre = ','.join(artist['genres'])

                # Query

                recommendations = sp.recommendations(f'{seed_artist}',
                                                     f'{seed_track}',
                                                     f'{seed_genre}',
                                                     10, 40, 0.5)

                # DataFrame

                recommendations_df = recommendations['recommendations_df']

                print((Fore.LIGHTYELLOW_EX + f'{recommendations_df.to_string(index=False)}'))
                time.sleep(1)
                print()
                print()
                print(Fore.RESET + 'Want me to create a playlist for you with my recommendations?')
                print()
                print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
                print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
                print()
                response_1_1_2 = input(Fore.LIGHTRED_EX + 'Enter your answer: ')
                if response_1_1_2 == '1':
                    print('NOIIIIIIICEEEEE!!!! Just gimme a sec, I`ll get some inputs from you')
                    time.sleep(1)
                    print()
                    print('Lets start')
                    print()
                    pl_name = input(Fore.LIGHTRED_EX + 'Could you name your playlist? ')
                    time.sleep(1)
                    print()
                    pl_disc = input(Fore.LIGHTRED_EX + 'Now, could you put some description? ')
                    time.sleep(1)
                    print()
                    print(Fore.RESET + 'Be right back')

                    # Setting Up Play list

                    playlist = sp.create_list(f'{user_id}', f'{pl_name}', f'{pl_disc}')

                    playlist_id = playlist['id']
                    playlist_url = playlist['url']

                    # Adding Tracks

                    recommendations_ids = recommendations['id']

                    add_songs = sp.add_songs(playlist_id, recommendations_ids)
                    print()
                    print('Yooo, just finished, here is your playlist info')
                    print()
                    print(Fore.LIGHTYELLOW_EX + pl_name, playlist_id, playlist_url)
                    print()
                    print(Fore.RESET + 'Now, that we got everything here, I will bring back the main menu')
                    print()
                if response_1_1_2 == '2':
                    print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
                    time.sleep(2)
                    print('Now, that we got everything here, I will bring back the main menu')
                    print()
            if response_1_1 == '2':
                print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
                time.sleep(2)
                print('Now, that we got everything here, I will bring back the main menu')
                print()
        if response == '2':
            print(Fore.RESET + 'Sorry, ' + Fore.LIGHTBLUE_EX + ', please look it up if the name of the band is spelled '
                                                               'right and run me again!')
            time.sleep(1)
            print('I will bring back the main menu')
            time.sleep(1)
    if choice == '2':
        print()
        print('I`m on it, I will bring back everything that I will find. But first I need to know their name!')
        time.sleep(1)
        artist_input = input(Fore.LIGHTRED_EX + 'Enter the Name of the Artist : ')
        time.sleep(1)

        # Response

        print(
            Fore.RESET + 'Niiiiiice, ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + Fore.RESET +
            ' it is. Let me do my thing ! I will be right back with the results!')
        print()
        print()
        time.sleep(2)
        print('Here everything that I found about ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + Fore.RESET +
              ' !')
        print()

        # Setting Up Variables with DataFrame Attributes

        artist = sp.artist(artist_input)
        artist_df = artist['artist_df']
        artist_id = artist['id']

        #

        print()
        time.sleep(1)
        print(Fore.LIGHTYELLOW_EX + f'{artist_df.to_string(index=False)}')
        print()
        print()
        print(Fore.RESET + 'Now, here are some of ' + Fore.LIGHTYELLOW_EX + str.title(artist_input) + '`s' +
              Fore.RESET + ', ' + 'Top Tracks')
        time.sleep(1)
        print()

        # Setting Up New Variables for insert into the query

        top_track_input = ''.join(artist_id)

        # Query

        top_track = sp.top_tracks(f'{top_track_input}')

        # DataFrame

        top_df = top_track['top_df']

        print((Fore.LIGHTYELLOW_EX + f'{top_df.to_string(index=False)}'))
        print()
        time.sleep(1)
        print(Fore.RESET +
              'I pretty sure that you might know some of these, but here are the ' +
              Fore.LIGHTYELLOW_EX + str.title(artist_input) + '`s' + Fore.RESET + ' discography.')
        print()
        album = sp.album(f'{artist_input}')
        #
        print(Fore.LIGHTYELLOW_EX +
              f"{album.query(f'ID == {artist_id} and Tracks > 1').drop('ID', axis=1).to_string(index=False)}")
        time.sleep(2)
        print()
        print(Fore.RESET + 'Wow that was a lot of info! Did I found what you were looking for?')
        time.sleep(1)
        print()
        print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
        print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
        print()
        response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')
        if response == '1':
            print(Fore.RESET + 'Cool, glad that I helped! Do you want some recommendations?')
            time.sleep(1)
            print()
            print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
            print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
            print()
            response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')

            if response == '1':
                print(Fore.RESET + 'Here some tracks that you might want to look into.')
                print()
                time.sleep(1)

                # Setting Up New Variables for insert into the query

                seed_artist = ','.join(artist_id)

                top_track_id = top_track['id']
                randomization_track = random.sample(top_track_id, 1)
                seed_track = ','.join(randomization_track)

                seed_genre = ','.join(artist['genres'])

                # Query

                recommendations = sp.recommendations(f'{seed_artist}',
                                                     f'{seed_track}',
                                                     f'{seed_genre}',
                                                     40, 90, 0.5)

                # DataFrame

                recommendations_df = recommendations['recommendations_df']

                print((Fore.LIGHTYELLOW_EX + f'{recommendations_df.to_string(index=False)}'))
                time.sleep(1)
                print()
                print()
                print(Fore.RESET + 'Want me to create a playlist for you with my recommendations?')
                print()
                print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
                print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
                print()
                response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')
                if response == '1':
                    print(Fore.RESET + 'NOIIIIIIICEEEEE!!!! Just gimme a sec, I`ll get some inputs from you')
                    time.sleep(1)
                    print()
                    print(Fore.RESET + 'Lets start')
                    print()
                    pl_name = input(Fore.LIGHTRED_EX + 'Could you name your playlist? ')
                    time.sleep(1)
                    print()
                    pl_disc = input(Fore.LIGHTRED_EX + 'Now, could you put some description? ')
                    time.sleep(1)
                    print()
                    print(Fore.RESET + 'Be right back')

                    # Setting Up Play list

                    playlist = sp.create_list(f'{user_id}', f'{pl_name}', f'{pl_disc}')

                    playlist_id = playlist['id']
                    playlist_url = playlist['url']

                    # Adding Tracks

                    recommendations_ids = recommendations['id']

                    add_songs = sp.add_songs(playlist_id, recommendations_ids)
                    print()
                    print('Yooo, just finished, here is your playlist info')
                    print()
                    print(Fore.LIGHTYELLOW_EX + 'name :' + pl_name, playlist_url)
                    print()
                    print(Fore.RESET + 'Now, that we got everything here, I will bring back the main menu')
                    print()
                if response == '2':
                    print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
                    time.sleep(2)
                    print('Now, that we got everything here, I will bring back the main menu')
                    print()
            if response == '2':
                print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
                time.sleep(2)
                print('Now, that we got everything here, I will bring back the main menu')
                print()
        if response == '2':
            print(Fore.RESET + 'Sorry, ' + Fore.LIGHTBLUE_EX + ', please look it up if the name of the band is spelled '
                                                               'right and run me again!')
            time.sleep(1)
            print('I will bring back the main menu')
    if choice == '3':
        print()
        print(Fore.RESET + 'Sure, I will get you just the best!!!')
        print('But before I show you, could you do me a favor?')
        time.sleep(1)
        print('I need a band, for me to get to know more about your taste, could you tell me')
        print()
        artist_input = input(Fore.LIGHTRED_EX + 'Enter the Name of the Artist : ')
        print()
        print(Fore.RESET + 'Cool, I know them! I`m on it, by the way - nice taste ' + f'{Fore.LIGHTBLUE_EX + username}'
              + Fore.RESET + '!')
        time.sleep(1)
        print()
        print('Just more couple of things!')
        print('For me to get more accurate results, could you set the min and max popularity and the target energy '
              'value?')
        time.sleep(1)
        print()
        print('Just enter a number from 0 to 100')
        print('Take in consideration that the lower the number in the popularity parameters, more likely to get a '
              'list of upcoming bands!')
        print()
        print('And the target energy will set the mood of the tracks, the parameter is using values from 0 to 1,'
              'For example, you might request target_energy=0.6. All target values will be weighed equally in ranking '
              'results.')
        time.sleep(1)
        print()
        print('If you`re feeling adventurous, take a shot, I will not disappoint!')
        print()
        minimum_popularity = input(Fore.LIGHTRED_EX + 'Enter the minimum value: ')
        time.sleep(1)
        print()
        maximum_popularity = input(Fore.LIGHTRED_EX + 'Enter the maximum value: ')
        print()
        target_energy = input(Fore.LIGHTRED_EX + 'Enter the energy value: ')
        print()
        print(Fore.RESET + 'All right, now that I have all that the info, be right back with some kick ass '
                           'recommendations for you!!')
        print()
        # Setting Up Variables with DataFrame Attributes

        artist = sp.artist(artist_input)

        artist_df = artist['artist_df']
        artist_id = artist['id']
        top_track_input = ''.join(artist_id)

        # Query

        top_track = sp.top_tracks(f'{top_track_input}')

        # DataFrame

        top_df = top_track['top_df']

        seed_artist = ','.join(artist_id)

        top_track_id = top_track['id']
        randomization_track = random.sample(top_track_id, 1)
        seed_track = ','.join(randomization_track)

        seed_genre = ','.join(artist['genres'])

        recommendations = sp.recommendations(f'{seed_artist}',
                                             f'{seed_track}',
                                             f'{seed_genre}',
                                             f'{minimum_popularity}',
                                             f'{maximum_popularity}',
                                             f'{target_energy}')

        # DataFrame

        recommendations_df = recommendations['recommendations_df']

        print((Fore.LIGHTYELLOW_EX + f'{recommendations_df.to_string(index=False)}'))
        time.sleep(1)
        print()
        print()
        print(Fore.RESET + 'Want me to create a playlist for you with my recommendations?')
        print()
        print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
        print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
        print()
        response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')
        if response == '1':
            print(Fore.RESET + 'NOIIIIIIICEEEEE!!!! Just gimme a sec, I`ll get some inputs from you')
            time.sleep(1)
            print()
            print(Fore.RESET + 'Lets start')
            print()
            pl_name = input(Fore.LIGHTRED_EX + 'Could you name your playlist? ')
            time.sleep(1)
            print()
            pl_disc = input(Fore.LIGHTRED_EX + 'Now, could you put some description? ')
            time.sleep(1)
            print()
            print(Fore.RESET + 'Be right back')

            # Setting Up Play list

            playlist = sp.create_list(f'{user_id}', f'{pl_name}', f'{pl_disc}')

            playlist_id = playlist['id']
            playlist_url = playlist['url']

            # Adding Tracks

            recommendations_ids = recommendations['id']

            add_songs = sp.add_songs(playlist_id, recommendations_ids)
            print()
            print('Yooo, just finished, here is your playlist info')
            print()
            print(Fore.LIGHTYELLOW_EX + 'Name: ' + pl_name, playlist_url)
            print()
            print(Fore.RESET + 'Now, that we got everything here, I will bring back the main menu')
            print()
        if response == '2':
            print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
            time.sleep(2)
            print('Now, that we got everything here, I will bring back the main menu')
            print()
    if choice == '4':
        print('Right on, it is always nice to get to know new stuff!')
        time.sleep(1)
        print()
        print('This search wont be towards your musical taste, but I will take as a parameter your country')
        print(
            'So, the result might bring a lot of different flavors for you! '
            'So just relax and try to expand your horizons!')
        time.sleep(1)
        print()
        print('I just need to know do you want to get new stuff from your country or another one?')
        time.sleep(1)
        print()
        print('Beware that your country is the one that your billing info is set on')
        time.sleep(1)
        print()
        print('I will get all the singles within 2 months period!')
        print()
        print('Hope you like it!')
        print()
        print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - My Country')
        print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - Another Country')
        print()
        response = input(Fore.LIGHTRED_EX + 'Give it a try, you wont regret : ')
        if response == '1':
            print(Fore.RESET + 'Cool your country has a lot to offer, just gimme a sec')
            # Setting Up Query
            new_releases = sp.new_releases(user_ct)

            # Filtering
            new_releases_df = new_releases['new_releases_df']
            new_releases_loc = new_releases_df.loc[new_releases_df["Type"] == "single"]

            print()
            print(Fore.LIGHTYELLOW_EX +
                  f'{new_releases_loc.to_string(index=False)}')

            # Setting Up the Playlist

            print()
            print(Fore.RESET + 'Want me to create a playlist for you with the new releases singles?')
            print()
            print(Fore.LIGHTBLUE_EX + '1' + Fore.RESET + ' - Yes')
            print(Fore.LIGHTBLUE_EX + '2' + Fore.RESET + ' - No')
            print()
            response = input(Fore.LIGHTRED_EX + 'Enter your answer: ')
            if response == '1':
                print(Fore.RESET + 'NOIIIIIIICEEEEE!!!! Just gimme a sec, I`ll get some inputs from you')
                time.sleep(1)
                print()
                print(Fore.RESET + 'Lets start')
                print()
                pl_name = input(Fore.LIGHTRED_EX + 'Could you name your playlist? ')
                time.sleep(1)
                print()
                pl_disc = input(Fore.LIGHTRED_EX + 'Now, could you put some description? ')
                time.sleep(1)
                print()
                print(Fore.RESET + 'Be right back, I will add the best 10 singles on it!')

                # Getting Songs` ID
                track_name = ','.join(new_releases['url'])
                track_artist = ','.join(new_releases['artist'])

                track = sp.track(track_name)

                print(track)

            if response == '2':
                print("No worries, I really enjoy to looked all this for you, hope you enjoy as well")
                time.sleep(2)
                print('Now, that we got everything here, I will bring back the main menu')
                print()
        if response == '2':
            print()
            print(Fore.RESET + 'Sure, I`m glad that you are so adventurous to know some new stuff')
            print()
            print('But first, just a couple of things!')
            print()
            print('Which country you want me to look?')
            print()
            print(
                'Remember, to use just the country code, for example: "US" for United States,'
                ' "BR" for Brazil, and so on!')
            print()
            country = input(Fore.LIGHTRED_EX + 'Now just shoot the country, and I will be right over! ')
            print()

            # Setting Up Query
            new_releases = sp.new_releases(f'{country}')

            # Filtering
            new_releases_df = new_releases['new_releases_df']
            new_releases_loc = new_releases_df.loc[new_releases_df["Type"] == "single"]

            print(Fore.LIGHTYELLOW_EX +
                  f'{new_releases_loc.to_string(index=False)}')
    if choice == '5':
        print('Wow, now I got why you are such a music expert!!! Cool')
        print()
        print('For this I just need you to tell me, what song you might want to look into and what artist!')
        print()
        print('After I will, all most certain, your mind away')
        print()
        song_name = input(Fore.LIGHTRED_EX + 'Write the name of the song: ')
        print()
        singer_name = input(Fore.LIGHTRED_EX + 'Write the artist: ')
        print()
        print(Fore.RESET + 'I`m on it, just give me a sec!!')

        analysis = sp.analysis(f'{song_name}', f'{singer_name}')

        print(Fore.LIGHTYELLOW_EX + f'{analysis.to_string(index=False)}')

        print()
        print(Fore.RESET + 'Hope you enjoy these info about the track!')
        print()
        time.sleep(1)
        print('I will bring back the main menu')
        print()
        time.sleep(3)
    if choice == 'x':
        print('All right, next time will do a lot more! Take care ' + f'{Fore.LIGHTBLUE_EX + username}' + Fore.RESET)

        break
