import json
from django.views.generic.base import View
from django.shortcuts import render


class ErrorView(View):

    ERRORS = {
        1: 'Please follow the appropriate steps.',
        100: 'The website you are trying to edit does not belong to you',
    }

    def get(self, request, error_id, *args, **kwargs):
        error_msg = self.ERRORS.get(int(error_id))
        return render(
            request, 'error/error.html', {'msg': error_msg}
        )
