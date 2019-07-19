#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/List) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ListEntry(BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """
    resource_type: ClassVar[str] = "ListEntry"
    date: Optional[FHIRDate] = None
    deleted: Optional[bool] = None
    flag: Optional[CodeableConcept] = None
    item: FHIRReference = None

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("flag", "flag", CodeableConcept, False, None, False),
            ("item", "item", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class List(DomainResource):
    """ A list is a curated collection of resources.
    """
    resource_type: ClassVar[str] = "List"
    code: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    emptyReason: Optional[CodeableConcept] = None
    encounter: Optional[FHIRReference] = None
    entry: Optional[List[ListEntry]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    mode: str = None
    note: Optional[List[Annotation]] = empty_list()
    orderedBy: Optional[CodeableConcept] = None
    source: Optional[FHIRReference] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    title: Optional[str] = None

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", CodeableConcept, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("orderedBy", "orderedBy", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js