file = input('Name of the file: ')
suffix_list = ['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']
media_type = ['image/gif','image/jpg','image/jpeg','image/png','application/pdf','text/plain','application/zip']


start_index = file.find('.')


suffix = file[start_index:].lower() #.png
suffix_index = 0


if suffix in suffix_list:
    suffix_index = suffix_list.index(suffix)
    print(media_type[suffix_index])
else:
    print('application/octet-stream')


