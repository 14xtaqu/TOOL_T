import requests
import instaloader
import time
import os
from info import *


Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

def fetch_instagram_info(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return profile
    except Exception as e:
        return {"error": str(e)}

def search_social_media(username):
    websites = {
        "FaceBook": f"https://www.facebook.com/public/{username}/",
        "Instagram": f"https://instagram.com/{username}/",
        "YouTube": f"https://www.youtube.com/@{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}/",
        "SnapChat": f"https://www.snapchat.com/add/{username}/",
        "Telegram": f"https://t.me/{username}/",
        "Spotify": f"https://open.spotify.com/user/{username}/",
        "X": f"https://twitter.com/{username}/",
        "Pinterest": f"https://in.pinterest.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}/",
        "Tumblr": f"https://tumblr.com/{username}/",
        "Google+": f"https://plus.google.com/s/{username}/top/",
        "Weibo": f"https://weibo.com/u/{username}/",
        "Badoo": f"https://www.badoo.com/en/{username}/",
        "Behance": f"https://www.behance.net/{username}/",
        "Dribbble": f"https://dribbble.com/{username}/",
        "Kuaishou": f"https://www.kuaishou.com/profile/{username}/",
        "YY": f"https://www.yy.com/u/{username}/",
        "Quora": f"https://www.quora.com/profile/{username}/",
        "Tieba Baidu": f"https://tieba.baidu.com/f?kw={username}/",
        "Imgur": f"https://imgur.com/user/{username}/",
        "PayPal": f"https://www.paypal.com/paypalme/{username}/",
        "Vimeo": f"https://vimeo.com/{username}/",
        "Discord": f"https://discord.gg/{username}/",
        "Likee": f"https://l.likee.video/p/{username}/",
        "PicsArt": f"https://picsart.com/{username}/",
        "Twitch": f"https://www.twitch.tv/{username}/",
        "Linkedin": f"https://www.linkedin.com/in/{username}/",
        "Threads": f"https://www.threads.net/@{username}/",
        "Medium": f"https://medium.com/@{username}/",
        "Stack Exchange": f"https://academia.stackexchange.com/users/{username}/",
        "Wattpad": f"https://www.wattpad.com/user/{username}/",
        "SoundCloud": f"https://soundcloud.com/{username}/",
        "Deviantart": f"https://www.deviantart.com/{username}/",
        "YuboLive": f"https://www.deviantart.com/{username}/",
        "Tinder": f"https://tinder.com/app/profile/{username}/",
        "Wordpress": f"https://wordpress.com/{username}/",
        "NextDoor": f"https://nextdoor.com/profile/{username}/",
        "Triller": f"https://triller.co/@{username}/",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "Foursquare": f"https://foursquare.com/user/{username}/",
        "Steam": f"https://steamcommunity.com/id/{username}/",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}/",
        "Fotolog": f"https://fotolog.com/{username}/",
        "Gaiaonline": f"https://www.gaiaonline.com/profiles/{username}/",
        "Myspace": f"https://myspace.com/{username}/",
        "Replit": f"https://replit.com/@{username}/",
        "Tagged": f"https://www.tagged.com/{username}/",
        "Mixi": f"https://mixi.jp/view_community.pl?id={username}/",
        "Crunchyroll": f"https://www.crunchyroll.com/{username}/",
        "Meetup": f"https://www.meetup.com/{username}/",
        "Tellonym": f"https://tellonym.me/{username}/",
        "Pastebin": f"https://pastebin.com/u/{username}/",
        "Github": f"https://github.com/{username}/",
        "Gitlab": f"https://gitlab.com/{username}/",
        "Wikipedia": f"https://www.wikipedia.org/wiki/User:{username}/",
        "Udemy": f"https://www.udemy.com/user/{username}/",
        "Canva": f"https://www.canva.com/{username}/",
        "Payhip": f"https://payhip.com/{username}",
        "Portswigger": f"https://portswigger.net/users/{username}",
        "DokanTip": f"https://tip.dokan.sa/{username}/",
        "Harmash": f"https://harmash.com/users/{username}/",
        "EXPO ReactNative": f"https://expo.dev/accounts/{username}"
    }
    
   
    account_status = {}
    for site, url in websites.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                account_status[site] = "Found"
            else:
                account_status[site] = "Not Found"
        except requests.RequestException as e:
            account_status[site] = f"Error: {e}"
        
        # Sleep to avoid being blocked
        time.sleep(1)
    
    return account_status

def format_output(instagram_info, social_media_status):
    output = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Info                     ┃ Acc                                                                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ID                       │ {instagram_info.userid}                                                       │
│ Is business acc?         │ {"Yes" if instagram_info.is_business_account else "No"}                       │
│ Business category name   │ {instagram_info.business_category_name}                                       │
│ Is verified acc?         │ {"Yes" if instagram_info.is_verified else "No"}                               │
│ Is private acc?          │ {"Yes" if instagram_info.is_private else "No"}                                │
│ Username                 │ @{instagram_info.username}                                                    │
│ Nickname                 │ {instagram_info.full_name}                                                    │
│ Avatar                   │ {instagram_info.profile_pic_url}                                              │
│ Followers                │ {instagram_info.followers}                                                    │
│ Following                │ {instagram_info.followees}                                                    │
│ Followed by viewer       │ {instagram_info.followed_by_viewer}                                           │
│ Follows viewer           │ {instagram_info.follows_viewer}                                               │
│ Has blocked viewer       │ {instagram_info.has_blocked_viewer}                                           │
│ Posts                    │ {instagram_info.mediacount}                                                   │
│ IGTV videos              │ {instagram_info.igtvcount}                                                    │
│ Has public stories?      │ {instagram_info.has_public_story}                                             │
│ Has viewable stories?    │ {instagram_info.has_viewable_story}                                           │
│ Has highlight?           │ {instagram_info.has_highlight_reels}                                          │
│ Bio                      │ {instagram_info.biography}                                                    │
│ Bio link                 │ {instagram_info.external_url}                                                 │
│ Has requested viewer?    │ {instagram_info.has_requested_viewer}                                         │
│ Requested by viewer?     │ {instagram_info.requested_by_viewer}                                          │
└──────────────────────────┴──────────────────────────────────────────────────────────────────────────────┘
"""
    # Add social media status to the output
    output += "\nSocial Media Accounts:\n"
    for site, status in social_media_status.items():
        output += f"{site}: {status}\n"
    
    return output
    def save_to_file(data, filename='social_media_info.txt'):
        with open(filename, 'w') as file:
            file.write(data)

def chosa1():
    username = input(f"[+]Enter the username:@{Green}")
    
    # Fetch Instagram info
    instagram_info = fetch_instagram_info(username)
    
    # Check if there's an error with Instagram info
    if isinstance(instagram_info, dict) and "error" in instagram_info:
        print(f"{DarkRed}Error fetching Instagram info: {instagram_info['error']}")
        return
    
    # Fetch social media links
    social_media_status = search_social_media(username)
    
    # Format the output
    formatted_output = format_output(instagram_info, social_media_status)
    
    # Ask user if they want to save the info
    save_option = input(f"{Green}you want to save the information to a file? (y/n):")
    if save_option.lower() == 'y':
        save_to_file(formatted_output)
        print(f"[{Red}+{Red}]{White}Information saved to file.")
    else:
        print(f"[{Red}+{Red}]{White}Oky please wait...")
        time.sleep(1)
        os.system('clear' if os.name != 'nt' else 'cls')
        time.sleep(1)
        print(formatted_output)

