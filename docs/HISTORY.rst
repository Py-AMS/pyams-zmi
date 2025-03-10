Changelog
=========

2.6.0
-----
 - added table marker interface and custom viewlet manager to hide toolbar on specific views or tables
 - updated Gitlab-CI for Python 3.12

2.5.0
-----
 - added interface to handle tables columns with custom sorting values

2.4.2
-----
 - small updates in forms templates

2.4.1
-----
 - packaging issue

2.4.0
-----
 - added JSON table row delete callback helper

2.3.5
-----
 - force table width to 100%
 - added support for non exportable columns in MyAMS.js
 - added support for Python 3.12

2.3.4
-----
 - updated form group switcher widgets values checker
 - updated table refresh callback

2.3.3
-----
 - updated display form template

2.3.2
-----
 - updated forms templates

2.3.1
-----
 - added column priority getter for use in responsive tables

2.3.0
-----
 - added support for custom modal content class

2.2.5
-----
 - added formatting strings constants

2.2.4
-----
 - added profile edit form content getter

2.2.3
-----
 - updated Swagger-UI bundle

2.2.2
-----
 - updated user profile ACL
 - updated CSS syntax

2.2.1
-----
 - updated default label getter

2.2.0
-----
 - include MyAMS LightMode theme
 - added table head CSS styles renderers
 - added permission check on home breadcrumb menu
 - update user profile edit form title

2.1.0
-----
 - updated form title management

2.0.1
-----
 - updated Buildout configuration

2.0.0
-----
 - upgraded to Pyramid 2.0

1.15.0
------
 - added support for permissions on menus
 - added simple add and edit forms renderers
 - added secondary context actions viewlet
 - updated group and table switcher button style

1.14.1
------
 - moved Swagger specifications and Swagger-UI view from PyAMS_utils package

1.14.0
------
 - added base sortable class
 - added form legend getter interface
 - added form errors

1.13.0
------
 - added Swagger-UI plug-in

1.12.2
------
 - added generic properties edit form marker interface

1.12.1
------
 - added support for group switchers in standard form groups

1.12.0
------
 - added interface to handle custom table data attributes adapters
 - added default tables length in user profile
 - added support for Python 3.11

1.11.4
------
 - updated translation handler in tables templates

1.11.3
------
 - use PyAMS_utils *copy_request* function to copy request in favicon view to keep request
   registry

1.11.2
------
 - corrected Gitlab-CI configuration

1.11.1
------
 - added i18n domain to inner table template
 - use f-strings in header viewlet helpers

1.11.0
------
 - added support for Python 3.10
 - added "header_label" attribute to management views
 - added default management view header title adapter
 - added table group switcher
 - added table attribute switcher column
 - added trash column permission checker
 - added submit form condition
 - added helper to get table refresh event callback
 - updated views title adapters

1.10.0
------
 - added table method to get row ID, which can be overridden to create custom implementations
 - added marker interface on reorder column
 - added padding to badge in navigation menus item
 - added flex classes to main content element
 - added support for interfaces factories in table refresh helpers
 - added object hint and icon getter interfaces and default adapters
 - added form getter interface
 - added label to context addings dropdown menu
 - added custom base table columns
 - updated list of available MyAMS bundles
 - updated empty table layout
 - updated content header title getter
 - updated form checker fieldset padding

1.9.2
-----
 - package version mismatch

1.9.1
-----
 - updated user profile theme selection checker to handle empty profiles

1.9.0
-----
 - added MyAMS dark theme support
 - added custom breadcrumbs viewlet template
 - added user profile management
 - added support for user selection of graphical theme
 - updated default toolbar add menu status
 - updated table data-attributes getter
 - updated reorder column
 - renamed ZMI resources adapter to default
 - use HTML code instead of JSON in row refresh event to get all row data-attributes
 - use f-strings instead of *format*

1.8.1
-----
 - use constant for unknown principal ID

1.8.0
-----
 - added base ITableView marker interface
 - added TableView and InnerAdminView base classes
 - added CompositeAdminView base class, built from adapters to ICompositeView interface
 - updated utilities view default table length
 - updated view interface of actions viewlet to be able to display menu in inner views
 - updated headers templates to be able to include HTML code in forms headers

1.7.4
-----
 - added support for custom "delete" permission checker in container helper
 - added missing I18n domain in tables templates

1.7.3
-----
 - added label adapters for generic utilities
 - updated forms templates

1.7.2
-----
 - added title check in form header rendering
 - added site root label adapter

1.7.1
-----
 - updated form title rendering template to handle pre-formatted HTML code

1.7.0
-----
 - added runtime environment view to display Python packages versions, environment
   variables and configuration settings
 - added skin management form
 - added top menus groups viewlet manager
 - added home name to ZMI configuration
 - added base class to handle multi-tables views
 - added generic IObjectLabel interface to get label of any object
 - added reordering tables column and data attributes getter
 - updated JSON widget refresh callback
 - updated forms and tables templates

1.6.0
-----
 - use ProtectedViewObjectMixin as base class for table action column, to be able to
   register custom adapters to define permissions
 - added missing "context" to permission check
 - added MyAMS event helper to add new table rows as event callback
 - added MyAMS container helper to handle attribute switch from action column
 - added optional "display_if_empty" table attribute to display full template even when the
   table is empty
 - updated form's fieldset class handler
 - updated default table batch size
 - updated tables templates so that "pyams.toolbar" viewlet manager components may be
   registered for a table instead of a view into which the table is included
 - updated tables templates to display a warning message when display is limited to batch size
 - updated "pyams.context_addings" declaration to include add dropdown menu in any view

1.5.2
-----
 - added runtime environment description string to be displayed below version number
 - updated version display template
 - updated translations

1.5.1
-----
 - added MyAMS Emerald theme to ZMI configuration

1.5.0
-----
 - removed support for Python < 3.7
 - removed toolbar viewlet manager from modal dialogs
 - small templates updates

1.4.0
-----
 - updated forms and tables templates
 - updated form group switcher interface
 - added ActionColumn base class to handle action buttons in tables
 - updated Gitlab-CI configuration
 - removed Travis-CI configuration

1.3.0
-----
 - added favicon settings and metas headers
 - included metas headers in ZMI layout

1.2.0
-----
 - forms and tables templates updates
 - added inner table mixin class
 - included breadcrumbs content provider
 - updated control panel permissions

1.1.2
-----
 - updated Gitlab-CI configuration

1.1.1
-----
 - updated forms legend display condition

1.1.0
-----
 - added support for IObjectData interface in tables
 - updated forms templates
 - added missing IDs in inner tabs sub-forms

1.0.0
-----
 - initial release
