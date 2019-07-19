#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .period import Period
from .usagecontext import UsageContext


@dataclass
class NamingSystemUniqueId(BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    resource_type: ClassVar[str] = "NamingSystemUniqueId"
    comment: Optional[str] = None
    period: Optional[Period] = None
    preferred: Optional[bool] = None
    type: str = None
    value: str = None

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("period", "period", Period, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class NamingSystem(DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    resource_type: ClassVar[str] = "NamingSystem"
    contact: Optional[List[ContactDetail]] = empty_list()
    date: FHIRDate = None
    description: Optional[str] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    kind: str = None
    name: str = None
    publisher: Optional[str] = None
    responsible: Optional[str] = None
    status: str = None
    type: Optional[CodeableConcept] = None
    uniqueId: List[NamingSystemUniqueId] = empty_list()
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
        ])
        return js