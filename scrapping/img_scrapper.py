def save_img(html, timestamp, site):
    img_tags = html.find_all('img',{"src":True})
    img_urls = [img['src'] for img in img_tags]
    for url in img_urls:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = make_http_req(url)
        if not response: return None
        filename = re.search(r'/([\w_-]+)[.](jpg|gif|png)$', url)
        md5_hash = hashlib.md5(response.content).hexdigest()
        if not filename:
             continue
        img_full_name = f"saffar.me\\{filename.group(1)}_{md5_hash}.{filename.group(2)}".strip()
        if os.path.exists(img_full_name):
            continue
        with open(img_full_name, 'wb') as f:
            f.write(response.content)
            setctime(img_full_name, timestamp)