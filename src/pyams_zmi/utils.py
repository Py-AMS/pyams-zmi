#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_zmi.utils module

This module provides a small set of generic components.
"""

from zope.interface import Interface
from zope.location import ILocation

from pyams_utils.adapter import ContextRequestViewAdapter, adapter_config, query_adapter
from pyams_utils.interfaces import MISSING_INFO
from pyams_utils.interfaces.tales import ITALESExtension
from pyams_zmi.interfaces import IObjectHint, IObjectIcon, IObjectLabel, IObjectName

__docformat__ = 'restructuredtext'


def get_object_adapter(interface, context, request, view=None, name=''):
    """Get object name"""
    adapter = query_adapter(interface, request, context, view, name)
    if name and (adapter is None):
        adapter = query_adapter(interface, request, context, view)
    return adapter


class BaseObjectAdapter(ContextRequestViewAdapter):
    """Object name TALES extension"""

    interface = None
    
    def render(self, context, name=''):
        """Render TALES extension"""
        return get_object_adapter(self.interface, context, request=self.request, view=self.view, name=name)


#
# Objects names
#

@adapter_config(required=ILocation,
                provides=IObjectName)
def location_name(context):
    """Basic location name factory"""
    return context.__name__


def get_object_name(context, request, view=None, name=''):
    """Get object name"""
    return get_object_adapter(IObjectName, context, request, view, name)


@adapter_config(name='object_name',
                required=(Interface, Interface, Interface),
                provides=ITALESExtension)
class ObjectNameTalesExtension(BaseObjectAdapter):
    """Object name TALES extension"""
    
    interface = IObjectName


#
# Objects labels
#

@adapter_config(required=ILocation,
                provides=IObjectLabel)
def location_label(context):
    """Basic location name factory"""
    return MISSING_INFO


def get_object_label(context, request, view=None, name=''):
    """Get object label"""
    return get_object_adapter(IObjectLabel, context, request, view, name)


@adapter_config(name='object_label',
                required=(Interface, Interface, Interface),
                provides=ITALESExtension)
class ObjectLabelTalesExtension(BaseObjectAdapter):
    """Object label TALES extension"""
    
    interface = IObjectLabel


#
# Objects icons
#

@adapter_config(required=ILocation,
                provides=IObjectIcon)
def location_icon(context):  # pylint: disable=unused-argument
    """Basic location icon factory"""
    return 'far fa-square'


def get_object_icon(context, request, view=None, name=''):
    """Get object icon"""
    return get_object_adapter(IObjectIcon, context, request, view, name)


@adapter_config(name='object_icon',
                required=(Interface, Interface, Interface),
                provides=ITALESExtension)
class ObjectIconTalesExtension(BaseObjectAdapter):
    """Object icon TALES extension"""
    
    interface = IObjectIcon
    

#
# Objects hints
#

def get_object_hint(context, request, view=None, name=''):
    """Get object hint"""
    return get_object_adapter(IObjectHint, context, request, view, name)


@adapter_config(name='object_hint',
                required=(Interface, Interface, Interface),
                provides=ITALESExtension)
class ObjectHintTalesExtension(BaseObjectAdapter):
    """Object hint TALES extension"""
    
    interface = IObjectHint
