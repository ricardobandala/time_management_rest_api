# from db import Database
# from model import *
#
# session = Database().Session()
#
#
# def initial_add_users():
#     roles = session.add_all([
#         RoleModel(title='admin'),
#         RoleModel(title='reporter'),
#         RoleModel(title='observer')
#     ])
#
#     roles = session.query(RoleModel).all()
#     role_admin = list(filter(lambda r: r.title.name == 'admin', roles))[0]
#     role_reporter = list(filter(lambda r: r.title.name == 'reporter', roles))[0]
#     role_observer = list(filter(lambda r: r.title.name == 'observer', roles))[0]
#
#     user1 = UserModel()
#     user1.identity = IdentityModel(first_name='Leigh', last_name='Richman',email='leighrichman@pagefolio.com')
#     user1.credential = CredentialModel(username='leighrichman', password='987654321', is_active=True)
#     user1.role.append(role_admin)
#     user1.role.append(role_reporter)
#
#     user2 = UserModel()
#     user2.identity = IdentityModel(first_name='ricardo', last_name='bandala',email='ricardobandala@pagefolio.com')
#     user2.credential = CredentialModel( username='ricardobandala', password='123456789', is_active=True)
#     user2.role.append(role_reporter)
#
#     user3 = UserModel()
#     user3.identity = IdentityModel(first_name='Arin', last_name='Blue',email='arinblue@pagefolio.com')
#     user3.credential = CredentialModel(username='yorboyblue', password='123456789',is_active=True)
#
#     user4 = UserModel()
#     user4.identity = IdentityModel(first_name='Sherry', last_name='Richman',email='sherryrichman@pagefolio.com')
#     user4.credential = CredentialModel(username='sherryrichman', password='987654321', is_active=True)
#     user4.role.append(role_observer)
#
#     session.add_all([
#         user1,
#         user2,
#         user3,
#         user4
#     ])


def firstDuplicate(a):
    repeated_on_index = -1
    a_len = len(a)
    for i, x in enumerate(a):
        if (x in a[i:] and i+1 < a_len):
            repeated_on_index = x
    return repeated_on_index


print(firstDuplicate([2, 4, 3, 5, 1]))
print(firstDuplicate([2, 1, 3, 5, 3, 2]))