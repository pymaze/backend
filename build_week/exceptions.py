from rest_framework.views import exception_handler


def build_week_exception_handler(exc, context):
    # If exception is thrown that we don't explicitly handle here,
    # it should be delegated to the default e_handler in DRF. If we do
    # handle this exception type, still want to access the response generated
    # by the DRF

    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_generic_error
    }

    # Identify the type of the current exception
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        # If this exception is one we can handle, handle it.
        # Otherwise return the response generated earlier by
        # the default exception handler
        return handlers[exception_class](exec, context, response)
    return response


def _handle_generic_error(exc, context, response):
    response.data = {
        'errors': response.data
    }
    return response
