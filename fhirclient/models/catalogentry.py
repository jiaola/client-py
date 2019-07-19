#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CatalogEntryRelatedEntry(BackboneElement):
    """ An item that this catalog entry is related to.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"
    item: FHIRReference = None
    relationtype: str = None

    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", FHIRReference, False, None, True),
            ("relationtype", "relationtype", str, False, None, True),
        ])
        return js


@dataclass
class CatalogEntry(DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"
    additionalCharacteristic: Optional[List[CodeableConcept]] = empty_list()
    additionalClassification: Optional[List[CodeableConcept]] = empty_list()
    additionalIdentifier: Optional[List[Identifier]] = empty_list()
    classification: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    lastUpdated: Optional[FHIRDate] = None
    orderable: bool = None
    referencedItem: FHIRReference = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = empty_list()
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    validTo: Optional[FHIRDate] = None
    validityPeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", CodeableConcept, True, None, False),
            ("additionalIdentifier", "additionalIdentifier", Identifier, True, None, False),
            ("classification", "classification", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("lastUpdated", "lastUpdated", FHIRDate, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("validTo", "validTo", FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
        ])
        return js