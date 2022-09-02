class Readable:
    """
    Extendable to make object readable, i.e., you can use ``read`` on it.

    :param prefix: To be used internally.
    :param content: The text to be displayed when ``read`` is used.
    """
    def __init__(self, prefix="", content=None):
        self._content = content

    def set_content(self, content):
        self._content = content

    def content(self):
        return self._content


class Surface:
    """
    Extendable to make ``put [direct object] on [indirect object]`` work. Use this on the **indirect** object.
    """
    def __init__(self):
        pass
