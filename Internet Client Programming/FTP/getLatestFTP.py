import ftplib
import os
import socket

host = 'ftp.mozilla.org'
dirn = 'pub/mozilla.org/webtools'
file = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(host)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % host, e)
        return
    print('Connected to host "%s"' % host)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('Logged in as "anonymous"')

    try:
        f.cwd(dirn)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % dirn)
        f.quit()
        return
    print('Changed to "%s" folder' % dirn)

    try:
        f.retrbinary('RETR %s' % file, open(file, 'wb').write())
    except ftplib.error_perm:
        print('ERROR: Cannot read file "%s"' % file)
        os.unlink(file)
    else:
        print('Downloaded "%s" to CWD' % file )
    f.quit()


if __name__ == '__main__':
    main()
