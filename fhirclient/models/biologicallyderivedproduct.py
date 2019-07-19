#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2019-07-18.
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
class BiologicallyDerivedProductStorage(BackboneElement):
    """ Product storage.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductStorage"
    description: Optional[str] = None
    duration: Optional[Period] = None
    scale: Optional[str] = None
    temperature: Optional[float] = None

    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("duration", "duration", Period, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("temperature", "temperature", float, False, None, False),
        ])
        return js


@dataclass
class BiologicallyDerivedProductProcessing(BackboneElement):
    """ Any processing of the product during collection.

    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductProcessing"
    additive: Optional[FHIRReference] = None
    description: Optional[str] = None
    procedure: Optional[CodeableConcept] = None
    timeDateTime: Optional[FHIRDate] = None
    timePeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", Period, False, "time", False),
        ])
        return js


@dataclass
class BiologicallyDerivedProductManipulation(BackboneElement):
    """ Any manipulation of product post-collection.

    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductManipulation"
    description: Optional[str] = None
    timeDateTime: Optional[FHIRDate] = None
    timePeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("timeDateTime", "timeDateTime", FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", Period, False, "time", False),
        ])
        return js


@dataclass
class BiologicallyDerivedProductCollection(BackboneElement):
    """ How this product was collected.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductCollection"
    collectedDateTime: Optional[FHIRDate] = None
    collectedPeriod: Optional[Period] = None
    collector: Optional[FHIRReference] = None
    source: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", Period, False, "collected", False),
            ("collector", "collector", FHIRReference, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class BiologicallyDerivedProduct(DomainResource):
    """ A material substance originating from a biological entity.

    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProduct"
    collection: Optional[BiologicallyDerivedProductCollection] = None
    identifier: Optional[List[Identifier]] = empty_list()
    manipulation: Optional[BiologicallyDerivedProductManipulation] = None
    parent: Optional[List[FHIRReference]] = empty_list()
    processing: Optional[List[BiologicallyDerivedProductProcessing]] = empty_list()
    productCategory: Optional[str] = None
    productCode: Optional[CodeableConcept] = None
    quantity: Optional[int] = None
    request: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    storage: Optional[List[BiologicallyDerivedProductStorage]] = empty_list()

    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("parent", "parent", FHIRReference, True, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("productCode", "productCode", CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("request", "request", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js