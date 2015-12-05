from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import View
from builder.models import Website, Page


class EditView(View):
    def is_ok_page_id(self, website_id, page_id):
        try:
            page = Page.objects.get(pk=page_id)
        except Page.DoesNotExist:
            return False
        print page.website.id == website_id
        return page.website.id == website_id

    def is_ok_website_id(self, website_id, user):
        try:
            site = Website.objects.get(pk=website_id)
        except Website.DoesNotExist:
            return False
        return site.owner == user

    def build_pages_data(self, website_id, page_id):
        # Put the requested page (if exists) first
        pages = Page.objects \
                .filter(website__id__exact=website_id) \
                .order_by('priority')
        data = []
        for page in pages:
            if page.id == page_id:
                data = [{'id': page.id, 'name': page.name}] + data
            else:
                data.append({'id': page.id, 'name': page.name})
        return data

    def build_html_data(self, page_id):
        page = Page.objects.get(pk=page_id)
        return page.html

    def build_css_data(self, page_id):
        page = Page.objects.get(pk=page_id)
        css = []
        for style in page.css.all():
            css.append(
                {
                    'select': style.select,
                    'attr': style.attr,
                    'val': style.val,
                }
            )

        return css

    def get(self, request, website_id, page_id=None, *args, **kwargs):
        website_id = int(website_id)
        if page_id is not None:
            page_id = int(page_id)
        else:
            # Get the default page id
            pages = Page.objects \
                    .filter(website__id__exact=website_id) \
                    .order_by('priority')
            page_id = pages[0].id

        if not self.is_ok_website_id(website_id, request.user):
            return redirect('error', 102)

        if page_id is not None and not self.is_ok_page_id(website_id, page_id):
            return redirect('error', 101)

        pages_data = self.build_pages_data(website_id, page_id)
        html = self.build_html_data(page_id)
        css = self.build_css_data(page_id)

        data = {
            'website_id': website_id,
            'pages_data': pages_data,
            'html': html,
            'css': css,
        }

        return render(request, 'edit/edit.html', data)
