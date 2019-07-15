#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Linkage) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import domainresource
from . import fhirreference

from . import domainresource

@dataclass
class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.

    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """
    resource_type: ClassVar[str] = "Linkage"
    active: Optional[bool] = None
    author: Optional[fhirreference.FHIRReference] = None
    item: List[ LinkageItem] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.

    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """
    resource_type: ClassVar[str] = "LinkageItem"
    resource:fhirreference.FHIRReference = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("resource", "resource", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']