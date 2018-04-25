from tracker.views.auth import __all__ as all_auth_views
from tracker.views.auth import *

from tracker.views.public import __all__ as all_public_views
from tracker.views.public import *

from tracker.views.api import __all__ as all_api_views
from tracker.views.api import *

from tracker.views.donateviews import __all__ as all_donate_views
from tracker.views.donateviews import *

from tracker.views.user import __all__ as all_user_views
from tracker.views.user import *

from tracker.views.commands import __all__ as all_command_views
from tracker.views.commands import *

from tracker.views.eventviews import __all__ as all_event_views
from tracker.views.eventviews import *


__all__ = all_auth_views + all_public_views + all_api_views + all_donate_views + all_user_views + all_command_views + all_event_views

