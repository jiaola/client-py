#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import period
from . import usagecontext

from . import backboneelement

@dataclass
class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    resource_type: ClassVar[str] = "NamingSystemUniqueId"
    comment: Optional[str] = None
    period: Optional[period.Period] = None
    preferred: Optional[bool] = None
    type: str = None
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    resource_type: ClassVar[str] = "NamingSystem"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    date:fhirdate.FHIRDate = None
    description: Optional[str] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    kind: str = None
    name: str = None
    publisher: Optional[str] = None
    responsible: Optional[str] = None
    status: str = None
    type: Optional[codeableconcept.CodeableConcept] = None
    uniqueId: List[ NamingSystemUniqueId] = empty_list()
    usage: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']