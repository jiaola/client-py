#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"
    item:fhirreference.FHIRReference = None
    relationtype: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", fhirreference.FHIRReference, False, None, True),
            ("relationtype", "relationtype", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"
    additionalCharacteristic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    additionalClassification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    additionalIdentifier: Optional[List[identifier.Identifier]] = empty_list()
    classification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    lastUpdated: Optional[fhirdate.FHIRDate] = None
    orderable: bool = None
    referencedItem:fhirreference.FHIRReference = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = empty_list()
    status: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    validTo: Optional[fhirdate.FHIRDate] = None
    validityPeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("validTo", "validTo", fhirdate.FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


import sys
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']