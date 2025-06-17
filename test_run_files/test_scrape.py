import requests
import json

headers = {
    "Cookie" : "_fbp=fb.2.1725442849273.983826324874610183; _ga_YRLBGM14X9=GS1.1.1733062194.1.1.1733062262.60.0.0; _gcl_au=1.1.1253197537.1749055557; _ga_QHXRKWW9HH=GS2.3.s1749741838$o53$g0$t1749741838$j60$l0$h0; _ga=GA1.1.506358031.1725442804; _ga_08NPRH5L4M=GS2.1.s1749741872$o422$g1$t1749742536$j60$l0$h0; _ga_5HTJMW67XK=GS2.1.s1749741873$o179$g1$t1749742536$j60$l0$h0; _bypass_cache=true; _t=sX9YOT23gIjFXZYyJs0hiAnIY7HnZLm9JLlaRCl9YRK3yF8TNoMU2qj4nqwTZpHyN7V8g6A7PzVuRGqGpGVCKaKJzHCcJeJK1So0o20BDQiqbKw3cozP0mg1SvJ8PncvilbzqLT%2F0Hpt3f0%2B%2BUee77T1H8UvlLfxMXKwyJlOs%2BWHjqkx7bOpqLTicxSWILHGxFasNUUi7mqutnhQdI1EBHPO%2BqwEkprxYqlLQfVLcg%2FzkFVDVjvAlTXwmeWnAUxi8BY%2BiwUqdqbB8n8DccmtHyeyJxp%2BPnMLveemFDE9U9cdd6Dii9j%2Bk9%2B3uKtGJMX4fHSh4nT0VzQ%3D--uXLtK09SJ%2FYdEt2J--iS9e0JvDD%2Bjh%2BGnv7N%2B1xQ%3D%3D; _forum_session=PL6OAeVKLKexVN6MzG79S4ETDBqdEuge%2FZLHbGlAzZNQBGwdCAtmODdOSWq4AMxXqYVxbhuKofweTQBFlx0S3YetkjvfWDuMmDneoPBp39%2FLm4s6YyYP7jX0WjMvPMjUZ2gknJgk0cbYQpOY95uGkvIQHkdt2wRGq3TzZQ14sJYFn2hQLa9%2FDdo3uVLNjbPPFXzJekC1Sp62lUCZIXw21GLMqKXi7i6iR2ehllzdX8%2BVKxQesomPfYmsOnLXEJGIgfHBwxJHT09o%2F9oA4QqDfKd%2BOpjBc9I3YPAKmUT7p0vkBRP6p0Bd2z58iNRe1AtyU73%2FaemBvHfMCxOhS99bVNblGZwlKudrrD2aD%2B4PHp%2FwP8gvWXX7DFi1sIzd%2FA%3D%3D--gGg3K%2Foam%2FepwkK%2F--pmP%2F1hXdpV7OpFui4YVgzQ%3D%3D"
}

thread_count = 1
rangee=1
data = []
for i in range(rangee//20+1):
    response = requests.get(f"https://discourse.onlinedegree.iitm.ac.in/t/tds-project-1-doubt/179103/{thread_count}.json",headers=headers)
    data += response.json()["post_stream"]["posts"]
    thread_count+=20
    print(response.cookies.get_dict()["_forum_session"])

with open("test_scraped_data4.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=2,ensure_ascii=False)
