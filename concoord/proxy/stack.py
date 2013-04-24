"""
@author: Deniz Altinbuken, Emin Gun Sirer
@note: Stack proxy
@copyright: See LICENSE
"""
from concoord.clientproxy import ClientProxy
class Stack:
    def __init__(self, bootstrap):
        self.proxy = ClientProxy(bootstrap)

    def __concoordinit__(self):
        return self.proxy.invoke_command('__concoordinit__')

    def append(self, item):
        return self.proxy.invoke_command('append', item)

    def pop(self):
        return self.proxy.invoke_command('pop')

    def get_size(self):
        return self.proxy.invoke_command('get_size')

    def get_stack(self):
        return self.proxy.invoke_command('get_stack')

    def __str__(self):
        return self.proxy.invoke_command('__str__')


