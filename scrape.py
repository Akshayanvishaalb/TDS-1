import requests
import json

headers = {
    "Cookie" : "_fbp=fb.2.1725442849273.983826324874610183; _ga_YRLBGM14X9=GS1.1.1733062194.1.1.1733062262.60.0.0; _ga_QHXRKWW9HH=GS1.3.1744633349.52.1.1744633353.0.0.0; _ga=GA1.1.506358031.1725442804; _gcl_au=1.1.1253197537.1749055557; _ga_5HTJMW67XK=GS2.1.s1749537911$o178$g1$t1749537923$j48$l0$h0; _ga_08NPRH5L4M=GS2.1.s1749537911$o421$g1$t1749538113$j41$l0$h0; _t=Slhgq9Mq4CE5e44LrQKp2rhuG0u0Zyw9OwsfQJHVkJ9%2F51iyC6GRPhUS0QUlCVo9FdV7ygGtY6DYMukFdHcBudbhOukGNMm9O48JnHZCXZMuLQ3PWMFuNatnKgzq5p%2B7nuyz46fW3n3yvtKHsqb1OQRxzcJKcUKVvo6K42vj5fgl9aEsp7ewm%2FkK0xBLm5siJca26ES3HunDFAglBM0MPeqqQQvXIgswP59DLiE3UcK46mD17PBvBHAlFFe68VTek8gVFvBDWg4wiIW%2BH44uZFaGIammgIxu0%2F9dAWCtbPvC1CvoAVh82n6h45Js2SnloYXFj9A%2BHvc%3D--RIhduZgfEJ1xZ7jL--oAeJc3hjxNJOm6%2By%2FAQl7g%3D%3D; _forum_session=kGq1GTLp6jjJt%2BxVkiN6n3NKk6nxVMp4o5CsMmeuzrGtpDVsxGWmSIQu0F5x06suMaCTNtPDRS%2B7buEUkybYvfzsrsrkqifkQRlyp1Vsergw4zp37VVXwbwj%2FgHw9BHhndUoEq%2FT0D91uFrw2%2BRH49TJNMFeicwEu9fZwAgLuF3vNpoiBIvcBNAiqNsHQ3oFO0KG0IGITvEh%2BsvtzAo1%2BSqYP8dlJSq7K%2B1M8CbT1Qasr1szOboP7RF5zd4RGlGRSA6uWA4JCPUoZ5v%2FPiZ0gDx8JWobiaCpieqPZMy4PPMUfWiGW%2FK2%2FZQpp7KKMCgznXjueBbzn6TS5V%2Bcml15bYzC6vj%2FaTv70eOCBGXePmiUitC3b%2BYB5KzDWycru40rq%2FVW0WzY6B%2F8i0Xppjl0JOdb23XXW%2BQYpKgrbIEbTWWaALD%2B48qQYMcPsrk%2FwlkmYWKy63Lj3d8AJ2QiYbeJS419Fp4pPQdvUhr%2FC1YllSIhoqBAi7dQQVhzH6tl0QYt0KvQz7RjkxVw6yC3Kg%2BH9cJADRX4uPWzTbUJ3ASPWGYWMHUsx2xUdAvWHH7P%2Bg%3D%3D--W2UT0eyruitmB11V--EGKokFHY%2BT6l232LkLg7%2Fw%3D%3D"
}

for i in range(1,7):
    response = requests.get(f"https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json?page={i}",headers=headers)
    data = response.json()
    a = data["topic_list"]["topics"]
    with open(f"scraped_data{i}.json","w",encoding="utf-8") as f:
        json.dump(a,f,indent=2,ensure_ascii=False)
