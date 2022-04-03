from django.urls import converters


class UsernameConverter:
    regex = '[a-zA-Z0-9_-]{5,20}'

    # to_python的作用是返回值格式的转变，有时是原来格式，有时是int(value)
    def to_python(self, value):
        return value
