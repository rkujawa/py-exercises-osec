#!/usr/bin/env python3

from gi.repository import GLib
from pydbus import SessionBus
from dish import *
from order import *

loop = GLib.MainLoop()

class LunchService(object):
    """
        <node>
            <interface name='net.c0ff33.LunchService'>
                <method name='add'>
                    <arg type='s' name='name' direction='in'/>
                    <arg type='s' name='owner' direction='in'/>
                    <arg type='s' name='comment' direction='in'/>
                </method>
                <method name='dump'>
                </method>
            </interface>
        </node>
    """

    def __init__(self):
        self.o = Order()

    def add(self, name, owner, comment):
        self.o.dish_add(Dish(name, owner, comment))

    def dump(self):
        self.o.printit()

bus = SessionBus()
bus.publish("net.c0ff33.LunchService", LunchService())
loop.run()

