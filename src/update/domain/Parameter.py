import os


class Parameter:
    data = {
        'table': '',
        'field_update1': ''
    }

    def __init__(self):
        pass

    def set_param(self, key, value):
        self.data[key] = value


class ParameterService:

    def __init__(self):
        self.file = None
        self.data = Parameter()
        self.file_dir = os.path.dirname(os.path.realpath('__file__'))

    def read_file(self):
        #Open local
        # file_name = os.path.join(self.file_dir, '../../../parameter.properties')
        file_name = os.path.join(self.file_dir, '../parameter.properties')
        file_name = os.path.abspath(os.path.realpath(file_name))

        try:
            self.file = open(file_name, 'r')
            for l in self.file:
                params = l.split(':')
                self.data.set_param(params[0],params[1].rstrip())
        except IOError:
            print("Unable read file parameter!")
        finally:
            self.file.close()

        return self.data
