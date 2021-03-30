import re

if __name__ == "__main__": 
    
    with open('/home/lasoft/hillel_python_base/ReExp/sitemap.txt', 'r') as site_map:
        sitemap = site_map.read()

    # Нахождение URL-ов
    url_pattern = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
    urls = re.findall(url_pattern, sitemap)
    print('URLS======', urls)
    # Нахождение Доменов
    # domains_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    # domains = re.findall(domains_pattern, sitemap)
    # print('DOMAINS===', domains)
    # # Нахождение Email
    # email_pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    # email = re.findall(email_pattern, 'Мой email pahamihali4@gmail.com или меня можно найти здесь pavlom@oneplanetops.com')
    # print('EMAIL===', email)


    # ПОДМЕНА ТЕКСТА
    SHORT_TRACEBACK = {
        "Given the url (.+)": 'Could not load url {arg}',
        "Then see if we switched to a new tab": 'Could not load the new tab',
        "Then see if we switched to a new window": 'Could not load the new window',
        'Then check if the path (.+) exist': 'Could not load the new page {arg}',
        'Then check if you see (.+)': 'Could not find element {arg}',
        'Then click on the element (.+)': 'Could not find element {arg}'
    }
    # last_step = "Then check if you see #ZipCode_245"
    # last_step = "Then see if we switched to a new tab"
    last_step = "Then check if the path step3 exist"

    for key, value in SHORT_TRACEBACK.items():
        result = re.search(key, last_step)
        if result is not None:
            new_explanation = value
            if result.groups():
                new_explanation = re.sub(r'{arg}', result.group(1), value)
            print(new_explanation)

