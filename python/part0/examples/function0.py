
def print_metadata(metadata):
    print 'Title: ' + metadata['title']
    print 'Id: ' + str(metadata['id'])
    print 'Comment: ' + metadata['comment']

my_meta = {'title': 'C1s', 'id': 47, 'comment': 'This is the one'}

print_metadata(my_meta)
