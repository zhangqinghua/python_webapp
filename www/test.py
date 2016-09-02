import hashlib

sha1_passwd = '%s:%s' % ('1001', '123')
print('f')
hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
