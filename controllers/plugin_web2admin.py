@auth.requires_login()
def index():
    tables = [table for table in d().tables if check_access(table, 'w2a_root')]
    return locals()


@auth.requires(check_access(a0, 'w2a_root'))
def view_table():
    table = a0 or redirect(URL('error'))
    if table not in d().tables():
        redirect(URL('error'))
    form = None
    grid = SQLFORM.grid(d()[table],
                        args=request.args[:1],
                        fields=plugins.web2admin.fields.get(table),
                        field_id=plugins.web2admin.field_id.get(table),
                        details=False,
                        create=check_access(table, 'w2a_root'),
                        searchable=False,
                        editable=check_access(table, 'w2a_root'),
                        deletable=check_access(table, 'w2a_root'),
                        csv=False,
                        paginate=plugins.web2admin.items_per_page,
                        selectable=None,
                        headers=plugins.web2admin.headers,
                        orderby=plugins.web2admin.orderby.get(table),
                        maxtextlength=plugins.web2admin.maxtextlength.get(table) or 20,
                        maxtextlengths=plugins.web2admin.maxtextlengths,
                        showbuttontext=plugins.web2admin.showbuttontext,
                        # formstyle='divs',
                        # formstyle=formstyle_materialdesignlight,
                        ui=dict(widget='',
                                header='',
                                content='',
                                default='',
                                cornerall='',
                                cornertop='',
                                cornerbottom='',
                                button='button btn btn-default',
                                buttontext='buttontext button',
                                buttonadd='',
                                buttonback='',
                                buttonexport='',
                                buttondelete='',
                                buttonedit='',
                                buttontable='',
                                buttonview='',
                                )
                        )
    return locals()


@auth.requires(auth.has_membership('w2a_root'))
def fields():
    table = a0
    if table not in d().tables():
        redirect(URL('error'))
    table = d()[table]
    return locals()


def error():
    # TODO: change this with a nice page
    raise HTTP(404)
