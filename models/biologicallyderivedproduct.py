#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2019-07-15.
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

from . import domainresource

@dataclass
class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.

    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProduct"
    collection: Optional[BiologicallyDerivedProductCollection] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    manipulation: Optional[BiologicallyDerivedProductManipulation] = None
    parent: Optional[List[fhirreference.FHIRReference]] = empty_list()
    processing: Optional[List[BiologicallyDerivedProductProcessing]] = empty_list()
    productCategory: Optional[str] = None
    productCode: Optional[codeableconcept.CodeableConcept] = None
    quantity: Optional[int] = None
    request: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[str] = None
    storage: Optional[List[BiologicallyDerivedProductStorage]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductCollection"
    collectedDateTime: Optional[fhirdate.FHIRDate] = None
    collectedPeriod: Optional[period.Period] = None
    collector: Optional[fhirreference.FHIRReference] = None
    source: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.

    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductManipulation"
    description: Optional[str] = None
    timeDateTime: Optional[fhirdate.FHIRDate] = None
    timePeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js

@dataclass
class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.

    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductProcessing"
    additive: Optional[fhirreference.FHIRReference] = None
    description: Optional[str] = None
    procedure: Optional[codeableconcept.CodeableConcept] = None
    timeDateTime: Optional[fhirdate.FHIRDate] = None
    timePeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js

@dataclass
class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductStorage"
    description: Optional[str] = None
    duration: Optional[period.Period] = None
    scale: Optional[str] = None
    temperature: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("temperature", "temperature", float, False, None, False),
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