from django.dispatch import Signal


notify = Signal(providing_args=['target_object', 'verb', 'text'
								, 'target_article', 'target_topic'])
