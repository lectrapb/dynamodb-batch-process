import os


class StatusUpdate:
    current_page = ''
    current_data = ''

    def __int__(self):
        pass


class StatusUpdateService:
    data = {
        'current_page': '',
        'current_data': ''
    }

    def __init__(self):
        self.file = None
        self.file_dir = os.path.dirname(os.path.realpath('__file__'))

    def current_status(self):
        #Open local
        # file_name = os.path.join(self.file_dir, '../../../status.properties')
        file_name = os.path.join(self.file_dir, '../status.properties')
        file_name = os.path.abspath(os.path.realpath(file_name))
        try:
            self.file = open(file_name, 'r')
            for l in self.file:
                states = l.split(":")
                self.data[states[0]] = states[1].rstrip()
        except IOError:
            print("Unable read file!")
        finally:
            self.file.close()
        state = StatusUpdate()
        state.current_data = self.data['current_data']
        state.current_page = self.data['current_page']
        return state

    def update_status_page(self, key, value):
        # file_name = os.path.join(self.file_dir, '../../../status.properties')
        file_name = os.path.join(self.file_dir, '../status.properties')
        file_name = os.path.abspath(os.path.realpath(file_name))
        try:
            self.file = open(file_name, 'r')
            for l in self.file:
                states = l.split(":")
                self.data[states[0]] = states[1].rstrip()
        except IOError:
            print("Unable read file!")
        finally:
            self.file.close()
        self.data[key] = value
        result_keys = list(self.data.keys())
        result_values = list(self.data.values())
        list_status = []
        for i in range(len(result_keys)):
            list_status.insert(i, result_keys[i] + ":" + str(result_values[i]))
        try:
            self.file = open(file_name, 'w')
            for data in list_status:
                self.file.writelines(data + '\n')
        except IOError:
            print("Unable read file status!")
        finally:
            self.file.close()



