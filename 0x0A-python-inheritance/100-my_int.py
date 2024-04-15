#!/usr/bin/python3
"""Defines MyInt class that inherits from int"""


class MyInt(int):

    def __eq__(self, others):
        """Custom inverted equallity"""

        if isinstance(others, int):
            return super().__ne__(others)
        else:
            return True

        def __ne__(self, others):
            """Custom inverted not equal"""

            if isinstance(others, int):
                return super().__eq__(others)
            else:
                return False
