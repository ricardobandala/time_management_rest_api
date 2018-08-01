from .assoc_user_role import table as assoc_user_role_table
from .assoc_stint_stint_category import table as assoc_stint_stint_category_table
from .credential import CredentialModel
from .identity import IdentityModel
from .role import RoleModel
from .stint import StintModel
from .stint_category import StintCategoryModel
from .stint_note import StintNoteModel
from .user import UserModel
from .workday import WorkdayModel
from .workday_note import WorkdayNoteModel
__slots__ = [
    assoc_stint_stint_category_table,
    assoc_user_role_table,
    CredentialModel,
    IdentityModel,
    RoleModel,
    StintCategoryModel,
    StintModel,
    StintNoteModel,
    UserModel,
    WorkdayModel,
    WorkdayNoteModel
]

