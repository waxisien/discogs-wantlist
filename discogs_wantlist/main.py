import os

import discogs_client


d = discogs_client.Client('discogs_wantlist/0.1', user_token=os.environ('DISCOGS_TOKEN'))


if __name__ == '__main__':
    me = d.identity()
    username = me.username
    # Only to load user and access data
    user = me.profile
    currency = me.data['curr_abbr']

    print('{0} wantlist:'.format(username))
    for want in me.wantlist:
        release = d.release(want.id)
        title = release.title
        lowest_price = release.data.get('lowest_price')
        if lowest_price:
            lowest_price = str(lowest_price) + currency
        artist = release.data['artists'][0]['name']
        format = '{0}x{1}'.format(release.data['formats'][0]['qty'], release.data['formats'][0]['name'])
        print('{0} - {1} ({2}): {3}'.format(artist, title, format, lowest_price or '-'))
