"""Update feeds of instructors and workshops."""

import json
import urllib.request

URL_WORKSHOP = 'https://feeds.carpentries.org/all_workshops.json'
URL_INSTRUCTORS = 'https://feeds.carpentries.org/all_badged_people.json'


def get(url):
    response = urllib.request.urlopen(url)
    return json.load(response)


if __name__ == '__main__':
    workshops_all = get('https://feeds.carpentries.org/all_workshops.json')
    workshops = [workshop
                 for workshop in workshops_all
                 if workshop['url'].find('https://carpentries-uconn') != -1]
    with open('_data/all_workshops.json', 'w') as handle:
        json.dump(workshops, handle, indent=2)
