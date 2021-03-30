from random import choice, choices

from urlextract import URLExtract


# print('='*50)
# print('ЗАДАЧІ на интервью')
# print('='*50)
# print('Из двух списков получить словарь')
# list1 = [1, 3, 4, 56, 7, 8, 25]
# list2 = ['q', 's', 'd', 'f', 'g', 'h', 'j']
# new_dict = dict(zip(list1, list2))
# print('new_dict: ', new_dict)

# print('='*50)
# print('Превратить список в строку')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# new_str = ' '.join(i for i in fruits)
# print('new_str: ', type(new_str))
# print('new_str: ', new_str)

# print('='*50)
# print('Расскрытие списка любой вложености')
# l = [1, [2], [[[3, 4]]]]
# def flatten(lst):
#     while lst:
#         sublist = lst.pop(0)
#         if isinstance(sublist, list):
#             lst = sublist + lst
#         else:
#             yield sublist
# print('Pасскрытый список: ', list(flatten(l)))


def get_pages_urls(sitemap):
    extractor = URLExtract()
    pages = sitemap.split('\n')
    page = '<loc>https://www.qwerty.com/blog22.xml.gz</loc> <loc>https://www.qwerty.com/blog22.xml.gz</loc>'
    url = extractor.find_urls(page)
    # print('url: ', url)
    urls = [extractor.find_urls(k)[0] for k in pages if k.endswith('</loc>')]
    # print('urls: ', urls)
    return urls


if __name__ == "__main__":
    with open('./sitemap.txt', 'r') as site_map:
        sitemap = site_map.read()
    pages = get_pages_urls(sitemap)
    print('pages: ', pages)
    # print('pages: ', pages)
    sampling = choices(pages, k=4)
    print('sampling: ', sampling)
