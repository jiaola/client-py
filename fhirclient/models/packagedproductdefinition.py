#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
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
class PackagedProductDefinitionBatchIdentifier(BackboneElement):
    """ Batch numbering.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionBatchIdentifier"

    outerPackaging: Identifier = None
    immediatePackaging: Optional[Identifier] = None


@dataclass
class PackagedProductDefinitionPackageItem(BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionPackageItem"

    identifier: Optional[List[Identifier]] = None
    type: CodeableConcept = None
    quantity: Quantity = None
    material: Optional[List[CodeableConcept]] = None
    alternateMaterial: Optional[List[CodeableConcept]] = None
    device: Optional[List[FHIRReference]] = None
    manufacturedItem: Optional[List[FHIRReference]] = None
    packageItem: Optional[List["PackagedProductDefinitionPackageItem"]] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = None
    shelfLifeStorage: Optional[List[ProductShelfLife]] = None
    manufacturer: Optional[List[FHIRReference]] = None


@dataclass
class PackagedProductDefinition(DomainResource):
    """ A medicinal product in a container or package.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinition"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[List[FHIRReference]] = None
    description: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    marketingAuthorization: Optional[FHIRReference] = None
    manufacturer: Optional[List[FHIRReference]] = None
    batchIdentifier: Optional[List[PackagedProductDefinitionBatchIdentifier]] = None
    packageItem: List[PackagedProductDefinitionPackageItem] = field(default_factory=list)