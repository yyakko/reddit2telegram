#encoding:utf-8

from utils import get_url, download_file


subreddit = 'pics'
t_channel = '@r_pics_redux'


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}'.format(title, link)

    if what not in ('img'):
        return False
    # elif what == 'album':
    #     just_send_an_album(t_channel, url, bot)
    #     return True

    return r2t.send_img(url, ext, text)
