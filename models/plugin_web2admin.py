auth.settings.auth_manager_role = 'w2a_root'

if auth.user and not db.auth_group(role='w2a_root'):
    auth.add_membership(auth.add_group('w2a_root'))

a0, a1 = request.args(0), request.args(1)

auth_tables = ('auth_user', 'auth_group', 'auth_membership')


def check_access(table, perm):
    return auth.is_logged_in() and (auth.has_membership(role='w2a_root') and table in auth_tables)


from gluon.tools import PluginManager

plugins = PluginManager('web2admin',
                        items_per_page=20,
                        fields={},
                        field_id={},
                        dbs=(db,),
                        headers={},
                        orderby={},
                        maxtextlength={},
                        maxtextlengths={},
                        showbuttontext=True,
                        )


def d(index=-1):
    return plugins.web2admin.dbs[index]
