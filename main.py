#!/usr/bin/python


from server import *
import sys, getopt

def main(argv):
    host = 0;
    port = 0;
    
    try:
        opts, args = getopt.getopt\
        (argv, "hs:p:", ["server=", "port="])
    except getopt.GetoptError:
        print __file__, '-s <host> -b <port>'

    for opt, arg in opts:
        if opt == '-h':
            print __file__, '-s <host> -p <port>'
            sys.exit()

        elif opt in ("-s", "--server"):
            host = arg

        elif opt in ("-p", "--port"):
            port = int(arg)

    if not host:
        print 'expected -s <host>'
        exit(1)

    if not port:
        print 'expected -p <port>'
        exit(1)

    dir(server)
    server.start_server(host, port)
    
    
if __name__ == "__main__":
    main(sys.argv[1:]);
