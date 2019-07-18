#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/List) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import backboneelement

@dataclass
class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """
    resource_type: ClassVar[str] = "ListEntry"
    date: Optional[fhirdate.FHIRDate] = None
    deleted: Optional[bool] = None
    flag: Optional[codeableconcept.CodeableConcept] = None
    item:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class List(domainresource.DomainResource):
    """ A list is a curated collection of resources.
    """
    resource_type: ClassVar[str] = "List"
    code: Optional[codeableconcept.CodeableConcept] = None
    date: Optional[fhirdate.FHIRDate] = None
    emptyReason: Optional[codeableconcept.CodeableConcept] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    entry: Optional[List[ListEntry]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    mode: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    orderedBy: Optional[codeableconcept.CodeableConcept] = None
    source: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']