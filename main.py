import requests
from bs4 import BeautifulSoup as bs


github_user_name = input('Enter the GitHub user\'s name\n')

url = f'https://github.com/{github_user_name}'
r = requests.get(url)

bsoup = bs(r.content, 'html.parser')

if r.status_code == requests.codes.ok:
    avatar_src = bsoup.find('img', {'class': 'avatar-user', 'class': 'width-full'})['src']
    print(avatar_src)
else:
    print('That user does not exists!')


