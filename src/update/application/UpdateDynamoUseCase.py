from src.update.domain.Parameter import ParameterService
from src.update.domain.StatusUpdate import StatusUpdateService


class UpdateDynamoUseCase:

    def __init__(self):
        self.parameter_service = ParameterService()
        self.status_service = StatusUpdateService()
        self.param = self.parameter_service.read_file()
        self.table_name = self.param.data['table']
        self.field_update = self.param.data['field_to_update1']

    def update_dynamo(self):
        print(f'1. Tabla  a actualizar          =>: {self.table_name}')
        print(f'2. Campo  a añadir              =>: {self.field_update}')
        status = self.status_service.current_status()
        print(f'3. Ultima paginacion registrada =>: {status.current_page}')
        print(f'4. Ultimo registro enviado      =>: {status.current_data}')
        self.status_service.update_status_page("current_page", 10)


