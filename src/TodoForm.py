from wtforms import Form, StringField, BooleanField, validators, ValidationError


def filter_done(field):
    print '---------------{}--------------------'.format(field)
    if field == 'true':
        return True
    if field == 'false':
        return False
    return None


class UpdateTodoForm(Form):
    name = StringField('name', [validators.required()])
    done = StringField('done', filters=[filter_done])

    def validate_done(self, field):
        if field.data is None:
            raise ValidationError(
                '{} is incorrect for done'.format(field.data)
            )


class CreateTodoForm(Form):
    name = StringField('name', [validators.required()])
