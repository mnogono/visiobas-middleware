#!/usr/bin/python

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

import tools

def __get_backnet(host, port, device):
    """Run external application collect data from BACnet device
    and return json object with all end point devices"""
    print '__get_backnet'
    return tools.bacnet.device_list(host, port, device)

@Request.application
def __application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b
    dispatcher["export.BACnet"] = __get_backnet

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

def start_server(host, port):
    run_simple(host, port, __application)

if __name__ == '__main__':
    run_simple('192.168.1.36', 4000, __application)
