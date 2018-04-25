from django.db import models
from django.utils.translation import ugettext_lazy as _
from taiga.projects.issues.models import Issue as OldIssue

from taiga_contrib_issue_colouring import colours


class Issue(OldIssue):
    colour = models.SmallIntegerField(null=False, default=colours.UNSET,
                                      verbose_name=_("issue_state_colour"))
