'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 26, 2017

@author: jrm
'''
from atom.api import (
    Typed, ForwardTyped, Int, Bool, observe
)

from enaml.core.declarative import d_

from .view import View, ProxyView


class ProxyProgressBar(ProxyView):
    """ The abstract definition of a proxy Label object.

    """
    #: A reference to the Label declaration.
    declaration = ForwardTyped(lambda: ProgressBar)

    def set_progress(self, progress):
        raise NotImplementedError

    def set_animated(self, animated):
        pass

    def set_secondary_progress(self, progress):
        raise NotImplementedError

    def set_max(self, max):
        raise NotImplementedError

class ProgressBar(View):
    """ A simple control for displaying read-only text.

    """
    #: Sets the current progress to the specified value.
    progress = d_(Int())

    #: Sets the current progress to the specified value.
    secondary_progress = d_(Int())

    #: Animate the visual position between the current and target values.
    animated = d_(Bool(True))

    #: Set the upper range of the progress bar max.
    max = d_(Int())

    #: A reference to the ProxyLabel object.
    proxy = Typed(ProxyProgressBar)

    #--------------------------------------------------------------------------
    # Observers
    #--------------------------------------------------------------------------
    @observe('progress', 'secondary_progress', 'animated', 'max')
    def _update_proxy(self, change):
        """ An observer which sends the state change to the proxy.

        """
        # The superclass implementation is sufficient.
        super(ProgressBar, self)._update_proxy(change)