from ddtrace import patch_all
patch_all()
print('making a file')
with open('test.txt', 'w') as o:
    o.write('hello world')