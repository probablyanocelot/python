
import os
import json
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('.env')

APP_ID = os.getenv('APP_ID')
SECRET_KEY = os.getenv('SECRET_KEY')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

print(APP_ID, SECRET_KEY, REDDIT_USERNAME, REDDIT_PASSWORD)


def get_auth(app_id, secret, username, password):
    '''
        **AFTER FIRST USE, PASS AS HEADERS TO ALL REQUESTS**
    '''

    # authenticate API
    client_auth = requests.auth.HTTPBasicAuth(
        app_id, secret)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }
    headers = {'User-Agent': 'Test-Script: v0.01 (by /u/' + username}

    # send authentication request for OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=client_auth, data=data, headers=headers)
    print(res.json())
    # extract token from response and format correctly
    token = f"bearer {res.json()['access_token']}"
    # update API headers with authorization (bearer token)
    headers = {**headers, **{'Authorization': token}}
    return headers


def get_data(headers, passes, test=False):
    # initialize dataframe and parameters for pulling data in loop
    data = pd.DataFrame()
    # of posts to collect per pass
    params = {'limit': 100}

    # loop through x times
    # returns (passes * params['limit']) many posts
    for i in range(passes):
        # make request
        res = requests.get("https://oauth.reddit.com/r/edm/new",
                           headers=headers,
                           params=params)

        # get dataframe from response
        new_df = df_from_response(res, test)
        # take the final row (oldest entry)
        row = new_df.iloc[len(new_df)-1]
        # create fullname
        fullname = row['kind'] + '_' + row['id']
        # add/update fullname in params
        params['after'] = fullname

        # append new_df to data
        data = data.append(new_df, ignore_index=True)
    print(data)
    return data


# we use this function to convert responses to dataframes
def df_from_response(res, test=False):
    # initialize temp dataframe for batch of data in response
    df = pd.DataFrame()

    posts = res.json()['data']['children']
    # loop through each post pulled from res and append to df
    for post in posts:
        # if post['oembed']['type'] == 'video':
        df = df.append({
            'title': post['data']['title'],
            'url': post['data']['url'],
            'domain': post['data']['domain'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score'],
            'subreddit': post['data']['subreddit'],
            'created_utc': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'link_flair_css_class': post['data']['link_flair_css_class'],
            'id': post['data']['id'],
            'kind': post['kind'],
        }, ignore_index=True)
    if test:
        get_full_json(res, posts)
    return df


def get_full_json(res, posts):
    '''
    writes post data to json file, starting at 2nd highest level
        - triggered in df_from_response() by optional argument 'test'
    '''
    data = res.json()['data']
    with open('full_data.json', 'w') as f:
        json.dump(data, f, indent=4)


def main():
    app_info = get_auth(APP_ID, SECRET_KEY, REDDIT_USERNAME, REDDIT_PASSWORD)
    data = get_data(app_info, 1)
    data = data.to_json(orient='table')
    data = json.loads(data)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


app_info = get_auth(APP_ID, SECRET_KEY, REDDIT_USERNAME, REDDIT_PASSWORD)


if __name__ == '__main__':
    # for some reason, simply 'main()' doesn't work here
    # app_info = get_auth(APP_ID, SECRET_KEY, REDDIT_USERNAME, REDDIT_PASSWORD)
    data = get_data(app_info, 1)
    data = data.to_json(orient='table')
    data = json.loads(data)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
