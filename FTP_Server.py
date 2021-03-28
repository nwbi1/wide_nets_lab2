import os
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class MyHandler(FTPHandler):

    def on_connect(self):
        print ("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        print ("%s:%s disconnected" % (self.remote_ip, self.remote_port))

    def on_login(self, username):
        print ("%s:%s login" % (self.remote_ip, self.remote_port))

    def on_logout(self, username):
        print ("%s:%s logout" % (self.remote_ip, self.remote_port))

    def on_file_sent(self, file):
        print ("%s:%s file sent" % (self.remote_ip, self.remote_port))

    def on_file_received(self, file):
        print ("%s:%s file received" % (self.remote_ip, self.remote_port))

    def on_incomplete_file_sent(self, file):
        print ("%s:%s file incomplete file sent" % (self.remote_ip, self.remote_port))

    def on_incomplete_file_received(self, file):
        print("%s:%s incomplete file received" % (self.remote_ip, self.remote_port))
        os.remove(file)

def main():

    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    #authorizer.add_user('user1', '12345', 'users/user1', perm='elradfmwMT')
    #authorizer.add_user('user2', '67890', 'users/user2', perm='elradfmwMT')
    #authorizer.add_anonymous(homedir='users/anon', perm='elradfwMT')
    #authorizer.add_user('admin', 'qqqqq', 'users', perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = 'FTP server ready'

    handler.passive_ports = range(60000, 65535)

    handler.active_dtp
    handler.timeout = 700

    # DEBUG logging
    logging.basicConfig(level=logging.INFO)
    handler.log_prefix = '[%(username)s]@%(remote_ip)s'

    address = ('127.0.0.1', 7777)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()
