from .article import controller as article_api
from .library import controller as library_api
from .list import controller as list_api
from .user import controller as user_api
from .group import controller as group_api
from .article import model as article_model
from .library import model as library_model
from .list import model as list_model
from .user import model as user_model
from .group import model as group_model

# APIDOC Inherit Doc


"""
@apiDefine UnauthorizedAccessError
@apiError UnauthorizedAccessError User's access token is not valid
@apiErrorExample Error 401
    {
        "msg": "Unauthorized access"
    }
"""

"""
@apiDefine ListDoesNotExist
apiError ListDoesNotExist The list does not exist
@apiErrorExample Error 400
    {
        "msg": "List does not exist"
    }
"""