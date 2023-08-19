import requests


# Replace 'VIDEO_URL' with the actual URL of the video you want to fetch
def retorna_thumb(video_url):
    url = f"https://www.youtube.com/oembed?format=json&url={video_url}"
    headers = {
        "authority": "www.youtube.com",
        "accept": "*/*",
        "accept-language": "pt-BR,pt;q=0.8",
        "cookie": "PREF=tz=America.Sao_Paulo&f6=400&f5=20000&f7=100; LOGIN_INFO=AFmmF2swRQIgBpu43HCFIb6_okOyzvgssIZ6cNTuBpITtL1BZxuI67YCIQDU1Bvmm6XIndncxft3bA7fMrrAoaOuA9jlM90R9fYVpg:QUQ3MjNmenl3a0VDTG9FLWU1RkcxUmRjMnZsUmoxa0hvdWdfcVRZdlpVR2pXRWRfYkRPV1RVM3dTVXMyT1ZkbWVTb195U2VYSmVXWm1iU2F6TGRWNVo2bkZGTk5mRVpSWWRNUF96akdGQ01IdXVZdGpmekV0Ykg2VVVFWjFqQ0trdU5wT0szb0d0UnNsdnRnZ1lGenpqbW1IeFBrWDVoZm93; VISITOR_INFO1_LIVE=q2ztYJ1_f_0; HSID=AXc6PLyGWTMeU0sIl; SSID=AZJb7qjH7st82KEv4; APISID=NqGfS2dQIel9c3ji/AkqDyZNfCnrPqk7MC; SAPISID=YxIL8k7ZcbxKLWXq/A9I88Ne9lTCyuoEIu; __Secure-1PAPISID=YxIL8k7ZcbxKLWXq/A9I88Ne9lTCyuoEIu; __Secure-3PAPISID=YxIL8k7ZcbxKLWXq/A9I88Ne9lTCyuoEIu; SID=Zwg5_ozTiUkic4TZtzBb_RPGHV8TPxjc9mrlyo2Nc5N2LsgadHlL4LsNoCHVHBXyfGiN2g.; __Secure-1PSID=Zwg5_ozTiUkic4TZtzBb_RPGHV8TPxjc9mrlyo2Nc5N2LsgarymTzcKWRLtXMw3p5qwj8w.; __Secure-3PSID=Zwg5_ozTiUkic4TZtzBb_RPGHV8TPxjc9mrlyo2Nc5N2LsgaWk3ELkTHCCBTZX7oKk7Lwg.; YSC=RBtj_AXe2hU; wide=0; __Secure-1PSIDTS=sidts-CjIBSAxbGZ0uGveF5yV-wYqGkqVHGnkqCv37RRtCttO8lmKZ93kTvOV3ctQinbilQMPnRRAA; __Secure-3PSIDTS=sidts-CjIBSAxbGZ0uGveF5yV-wYqGkqVHGnkqCv37RRtCttO8lmKZ93kTvOV3ctQinbilQMPnRRAA; SIDCC=APoG2W8B0-rtTJlD6Zfjka2vk2A0BeVYfUPhABPrkNk0jsa1Yb56wt5JhcEJ71idZEiMITBvDA; __Secure-1PSIDCC=APoG2W_yxE8VW4rWzr9A-kqAfITgDewkO9-F_eDvNeVltPWcEXb1iOgXhWzsj2ntslBT870o6q8; __Secure-3PSIDCC=APoG2W9WhIAcBEdU0HtMHxpSrdTBkxrfdumrNB3BOolZlnOAmGnKMZAgUGPBFLUqvI1ZLxXX4A",
        "referer": "https://www.youtube.com/watch?v=fjdrbqN5e-0&t=88s",
        "sec-ch-ua": 'Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '"',
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-platform-version": "10.0.0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    return requests.get(url, headers=headers).json()["thumbnail_url"]

