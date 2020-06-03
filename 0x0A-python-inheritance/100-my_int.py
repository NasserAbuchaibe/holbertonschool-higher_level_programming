#!/usr/bin/python3


"""Rebel Class module"""


class MyInt(int):
    """[summary]

    Args:
        int ([type]): [description]
    """

    def __init__(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.__value = value

    def __eq__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.__value != other

    def __ne__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.__value == other

    def __str__(self):
        """Print out the string format"""
        return "{}".format(self.__value)
