from django.dispatch import Signal


notify = Signal(providing_args=['target_object', 'verb'])
