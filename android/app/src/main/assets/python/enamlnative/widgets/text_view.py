'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''
from atom.api import (
    Typed, ForwardTyped, Unicode, Enum, Event, observe, set_default
)

from enaml.core.declarative import d_

from .view import View, ProxyView


class ProxyTextView(View):
    """ The abstract definition of a proxy Label object.

    """
    #: A reference to the Label declaration.
    declaration = ForwardTyped(lambda: TextView)

    def set_text(self, text):
        raise NotImplementedError

    # def set_align(self, align):
    #     raise NotImplementedError
    #
    # def set_vertical_align(self, align):
    #     raise NotImplementedError


class TextView(View):
    """ A simple control for displaying read-only text.

    """
    #: The unicode text for the label.
    text = d_(Unicode())

    # #: The horizontal alignment of the text in the widget area.
    # align = d_(Enum('left', 'right', 'center', 'justify'))
    #
    # #: The vertical alignment of the text in the widget area.
    # vertical_align = d_(Enum('center', 'top', 'bottom'))
    #
    # #: An event emitted when the user clicks a link in the label.
    # #: The payload will be the link that was clicked.
    # link_activated = d_(Event(), writable=False)
    #
    # #: Labels hug their width weakly by default.
    # hug_width = set_default('weak')

    #: A reference to the ProxyLabel object.
    proxy = Typed(ProxyTextView)

    #--------------------------------------------------------------------------
    # Observers
    #--------------------------------------------------------------------------
    @observe('text')#, 'align', 'vertical_align')
    def _update_proxy(self, change):
        """ An observer which sends the state change to the proxy.

        """
        # The superclass implementation is sufficient.
        super(TextView, self)._update_proxy(change)
