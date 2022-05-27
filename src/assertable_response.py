from src.conditions_ import Conditions


class AssertableResponse:

    def __init__(self, response):
        self.response = response
        self.condition = Conditions(self.response.json())

    def should_have_status_code(self, status_code):
        # print(self.response.status_code, "|", status_code)
        assert self.response.status_code == status_code, f'{self.response.status_code} | {status_code}: \n ' \
                                                         f'{self.condition.show_response_body()}'

    def should_have_body_field(self, field_name, field_value=False):
        assert self.condition.have_field(field_name) is True

        if field_value:
            assert self.condition.field_have_value(field_name, field_value) is True

    '''def should_not_have_body_field(self, field_name, field_value=False):
        if field_value:
            assert self.condition.field_have_value(field_name, field_value) is False
        else:
            assert self.condition.have_field(field_name) is False'''

    '''def show_response_body(self):
        # print(self.condition.show_response_body())
        return self.condition.show_response_body()'''

    '''def get_value(self, key):
        return self.condition.get_params_request(key)'''

    def does_str_in_value(self, field_name, field_value):
        assert self.condition.does_str_in_value(field_name, field_value)