# -*- coding: utf-8 -*-
from libnmap.diff import NmapDiff
from libnmap.objects.os import CPE


class NmapHostname(object):
    """
        NmapHostname represents a hostname seen by nmap. The 
        of the protocol and the port.

        Depending on the scanning options, some additional details might be
        available or not. Like banner or extra datas from NSE (nmap scripts).
    """
    def __init__(self, name, hostname_type):
        """
            Constructor

            :param name: the hostname
            :type name: string
            :param hostname_type: how the hostname was recorded by nmap
            :type hostname_type: string
        """

        self._name = name
        self._type = hostname_type

    def __str__(self):
        return self._name

    @property
    def name(self):
        """
            Accessor for the hostname's name

            :return: string if available
        """
        return self._name

    @property
    def type(self):
        """
            Accessor for the hostname's type

            :return: string if available
        """
        return self._type
