#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import element

from . import element

@dataclass
class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    resource_type: ClassVar[str] = "RelatedArtifact"
    citation: Optional[str] = None
    display: Optional[str] = None
    document: Optional[attachment.Attachment] = None
    label: Optional[str] = None
    resource: Optional[str] = None
    type: str = None
    url: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("label", "label", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']