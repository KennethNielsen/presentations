
def make_metadata_string(metadata):
    result = 'Title: "' + metadata['title']
    result += '" Id: ' + str(metadata['id'])
    result += ' Comment: "' + metadata['comment'] + '"'
    return result

my_meta = {'title': 'C1s', 'id': 47, 'comment': 'This is the one'}

metadata_string = make_metadata_string(my_meta)
print metadata_string
