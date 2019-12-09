from rest_framework import permissions


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):

    def __init__(self):
        self.perms_map['POST'] = ['webapp.add_project']