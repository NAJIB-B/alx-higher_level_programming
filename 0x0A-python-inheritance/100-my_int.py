#!/usr/bin/python3
"""Defines MyInt class that inherits from int"""


class MyInt(int):

    def __eq__(self, others):
        """Custom inverted equallity

        Args:
            others (int): value to be compared with our instance
        """

        if isinstance(others, int):
            return super().__ne__(others)
        else:
            return True

        def __ne__(self, others):
            """Custom inverted equallity
 
            Args:
                others (int): value to be compared with our instance
            """

            if isinstance(others, int):
                return super().__eq__(others)
            else:
                return False
