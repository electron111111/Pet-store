from src.conditions_ import Conditions


class AssertableResponse:

    def __init__(self, response):
        self.response = response
        self.condition = Conditions

    def should_have_status_code(self, status_code):
        assert self.response.status_code == status_code, f'{self.response.status_code} | {status_code}'

    def should_have_body_field(self, field_name, field_value=False):
        assert self.condition(self.response.json()).have_field(field_name) is True

        if field_value:
            assert self.condition(self.response.json()).field_have_value(field_name, field_value) is True

    def does_str_in_value(self, field_name, field_value):
        assert self.condition(self.response.json()).does_str_in_value(field_name, field_value)

    def get_value(self, key):
        return self.condition(self.response.json()).get_params_request(key)
