"""Post a notification issue to the EZO 'Client Admin' Linear project.

Reuses the shared API toolkit's Linear client (LINEAR_API_KEY lives in
~/Development/api-toolkit/.env). The toolkit is added to sys.path; no key is
copied into this repo.
"""
import sys

from .config import API_TOOLKIT_ROOT, LINEAR_ASSIGNEE, LINEAR_PROJECT, LINEAR_TEAM


def _api():
    sys.path.insert(0, str(API_TOOLKIT_ROOT))
    from services.linear.api import LinearAPI  # noqa: E402
    return LinearAPI()


def post_issue(title: str, description: str):
    api = _api()
    return api.create_issue(
        team=LINEAR_TEAM,
        title=title,
        description=description,
        project=LINEAR_PROJECT,
        assignee=LINEAR_ASSIGNEE,
        priority=2,
    )
