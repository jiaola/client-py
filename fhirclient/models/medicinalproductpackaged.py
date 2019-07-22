#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged) on 2019-07-22.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus
from .prodcharacteristic import ProdCharacteristic
from .productshelflife import ProductShelfLife
from .quantity import Quantity


@dataclass
class MedicinalProductPackagedBatchIdentifier(BackboneElement):
    """ Batch numbering.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedBatchIdentifier"
    outerPackaging: Identifier = None
    immediatePackaging: Optional[Identifier] = None

    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("outerPackaging", "outerPackaging", Identifier, False, None, True),
            ("immediatePackaging", "immediatePackaging", Identifier, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductPackagedPackageItem(BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedPackageItem"
    identifier: Optional[List[Identifier]] = empty_list()
    type: CodeableConcept = None
    quantity: Quantity = None
    material: Optional[List[CodeableConcept]] = empty_list()
    alternateMaterial: Optional[List[CodeableConcept]] = empty_list()
    device: Optional[List[FHIRReference]] = empty_list()
    manufacturedItem: Optional[List[FHIRReference]] = empty_list()
    packageItem: Optional[List[MedicinalProductPackagedPackageItem]] = empty_list()
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = empty_list()
    shelfLifeStorage: Optional[List[ProductShelfLife]] = empty_list()
    manufacturer: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("quantity", "quantity", Quantity, False, None, True),
            ("material", "material", CodeableConcept, True, None, False),
            ("alternateMaterial", "alternateMaterial", CodeableConcept, True, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("manufacturedItem", "manufacturedItem", FHIRReference, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", ProdCharacteristic, False, None, False),
            ("otherCharacteristics", "otherCharacteristics", CodeableConcept, True, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", ProductShelfLife, True, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductPackaged(DomainResource):
    """ A medicinal product in a container or package.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackaged"
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[List[FHIRReference]] = empty_list()
    description: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    marketingStatus: Optional[List[MarketingStatus]] = empty_list()
    marketingAuthorization: Optional[FHIRReference] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    batchIdentifier: Optional[List[MedicinalProductPackagedBatchIdentifier]] = empty_list()
    packageItem: List[MedicinalProductPackagedPackageItem] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("marketingStatus", "marketingStatus", MarketingStatus, True, None, False),
            ("marketingAuthorization", "marketingAuthorization", FHIRReference, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, True),
        ])
        return js