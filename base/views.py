from urllib import request
from django.shortcuts import render

# Base Views:
#   base

def home(request):
    # TODO Get Cabal accounts
    context = {
        'guildmaster_name':      None,
        'guildmaster_year':      None,
        'guildmaster_subject':   None,
        'guildmaster_college':   None,
        'guildmaster_pseudonym': None,

        'treasurer_name':        None,
        'treasurer_year':        None,
        'treasurer_subject':     None,
        'treasurer_college':     None,
        'treasurer_pseudonym':   None,

        'archivist_name':        None,
        'archivist_year':        None,
        'archivist_subject':     None,
        'archivist_college':     None,
        'archivist_pseudonym':   None,

        'secretary_name':        None,
        'secretary_year':        None,
        'secretary_subject':     None,
        'secretary_college':     None,
        'secretary_pseudonym':   None,

        'webmaster_name':        None,
        'webmaster_year':        None,
        'webmaster_subject':     None,
        'webmaster_college':     None,
        'webmaster_pseudonym':   None,

        'minister_name':         None,
        'minister_year':         None,
        'minister_subject':      None,
        'minister_college':      None,
        'minister_pseudonym':    None,
    }
    return render(request, 'base/base.html', context)