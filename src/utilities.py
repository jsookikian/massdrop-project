def getValidatedUrl(url):
    if 'http://' not in url:
        return 'http://' + url
    elif 'https://' not in url:
        return url.replace("https://", "http://")
    else:
        return url