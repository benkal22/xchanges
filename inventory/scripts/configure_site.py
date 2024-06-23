from django.contrib.sites.models import Site

def configure_site():
    site, created = Site.objects.get_or_create(id=1)
    site.domain = 'localhost:8000'  # ou tout autre domaine que vous utilisez localement
    site.name = 'xchanges drc app'
    site.save()

configure_site()
