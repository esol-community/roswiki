# To change the set of active distros:
# 1) Change which distro is opened by default in custom/js/rosversion.js
#
# 2) Restart the server

# Still TODO:
# - Display which distro is active under the buttons so people know default,
#   and know if their action took effect
# - Have better error-reporting somehow if rosversion sections have typos
#   (maybe show all distros that aren't listed as hidden, so that a mistyped
#   distro will always be visible?)
# - Automatically label the sections as "c-turtle only" so people see the
#   changes?

"""
Example:

    <<Version()>>

    {{{#!wiki version fuerte_and_older
    This is fuerte and older
    }}}

    {{{#!wiki version groovy
    This is groovy
    }}}

    {{{#!wiki version hydro_and_newer
    This is hydro and newer
    }}}

"""

from headers import distro_selector_html
from macroutils import distro_names, distro_names_buildfarm, distro_names_eol

Dependencies = []

def execute(macro, args):
    if args:
        version = str(args)
        if version.lower() == 'n-turtle':
            return ('<span style="background-color:#FFFF00; '
                    'font-weight:bold; padding: 3px;">'
                    'Expected in N-Turtle</span>')
        else:
            return ('<span style="background-color:#FFFF00; '
                    'font-weight:bold; padding: 3px;">'
                    'New in %s</span>' % version)

    html = distro_selector_html(
        distros_default_displayed=distro_names_buildfarm,
        distros_default_hidden=distro_names_eol,
        distros_to_support_macros_for=distro_names
    )
    return macro.formatter.rawHTML(html)
