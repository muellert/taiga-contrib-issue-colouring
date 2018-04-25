# from taiga.projects.issues.models import Issue
# from taiga.projects.issues.models import Issue
from taiga_contrib_issue_colouring.models import Issue


def test_having_the_colour_field(settings):
    issue = Issue()
    assert issue.colour is not None
