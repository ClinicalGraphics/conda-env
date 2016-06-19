from .. import env
from ..exceptions import EnvironmentFileNotFound


class YamlFileSpec(object):
    _environment = None

    def __init__(self, filename=None, selectors=None, **kwargs):
        self.filename = filename
        self.selectors = selectors
        self.msg = None

    def can_handle(self):
        try:
            self._environment = env.from_file(self.filename, selectors=self.selectors)
            return True
        except EnvironmentFileNotFound as e:
            self.msg = str(e)
            return False
        except TypeError:
            self.msg = "{} is not a valid yaml file.".format(self.filename)
            return False

    @property
    def environment(self):
        if not self._environment:
            self.can_handle()
        return self._environment
