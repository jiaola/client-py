#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import extension
from . import narrative
from . import resource

from . import resource

@dataclass
class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"
    contained: Optional[List[resource.Resource]] = empty_list()
    extension: Optional[List[extension.Extension]] = empty_list()
    modifierExtension: Optional[List[extension.Extension]] = empty_list()
    text: Optional[narrative.Narrative] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, True, None, False),
            ("extension", "extension", extension.Extension, True, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']
try:
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + '.narrative']