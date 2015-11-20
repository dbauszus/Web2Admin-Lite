# Web2Admin-Lite

The Web2Admin-Lite plugin is cut version of the brilliant Web2Admin plugin.

https://github.com/rif/web2admin

Web2Admin was the reason why I started to use web2py. I previously worked with Django but was not satisfied with the user management tools and the integration of the Google Datastore.

Web2Admin adds a user management layer to the application which is seperate from the root administration of the web2py application itself.

The idea for this plugin was to offer the core user admin functionality only, with a minimal interface.

I prefer to show the admin interface on its own and not within the web2py frame. I don't record the admin history and only want to see auth_user, auth_group and auth_membership. The web2admin link at the top returns to this view.

![Imgur](http://i.imgur.com/r7T2RIj.png)

I use the bootstrap paper theme to show tables and forms. I only have one management role w2a_root and forms will always be opened for editing. In my use case there isn't a need to just view user accounts. I don't need to swap tables from this view and I don't require to export data from here.

![Imgur](http://i.imgur.com/8MnAUX1.png)

The editing form is styled with the bootstrap paper theme.

![Imgur](http://i.imgur.com/4xvyYps.png)

The plugin can be downloaded here.
[Web2Admin-Lite plugin](https://drive.google.com/uc?export=download&id=0B8HfmNU61LnARW0waV9hc1ZadUE)


