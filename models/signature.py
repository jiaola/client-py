#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Signature) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import coding
from . import element
from . import fhirdate
from . import fhirreference

from . import element

@dataclass
class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..

    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    resource_type: ClassVar[str] = "Signature"
    data: Optional[str] = None
    onBehalfOf: Optional[fhirreference.FHIRReference] = None
    sigFormat: Optional[str] = None
    targetFormat: Optional[str] = None
    type: List[coding.Coding] = empty_list()
    when:fhirdate.FHIRDate = None
    who:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']