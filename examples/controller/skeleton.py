"""
A skeleton Ryu component
"""
from ryu.base import app_manager
# The central management of Ryu applications.


class RyuSkeleton(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(RyuSkeleton, self).__init__(*args, **kwargs)
