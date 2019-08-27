#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus


@dataclass
class MedicinalProductDefinitionNameNamePart(BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameNamePart"

    part: str = None
    type: Coding = None


@dataclass
class MedicinalProductDefinitionNameCountryLanguage(BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameCountryLanguage"

    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    language: CodeableConcept = None


@dataclass
class MedicinalProductDefinitionContact(BackboneElement):
    """ A product specific contact, person (in a role), or an organization.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionContact"

    type: Optional[CodeableConcept] = None
    contact: FHIRReference = None


@dataclass
class MedicinalProductDefinitionName(BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionName"

    productName: str = None
    type: Optional[Coding] = None
    namePart: Optional[List[MedicinalProductDefinitionNameNamePart]] = None
    countryLanguage: Optional[List[MedicinalProductDefinitionNameCountryLanguage]] = None


@dataclass
class MedicinalProductDefinitionManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionManufacturingBusinessOperation"

    operationType: Optional[CodeableConcept] = None
    authorisationReferenceNumber: Optional[Identifier] = None
    effectiveDate: Optional[FHIRDate] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = None
    regulator: Optional[FHIRReference] = None


@dataclass
class MedicinalProductDefinitionSpecialDesignation(BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionSpecialDesignation"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    intendedUse: Optional[CodeableConcept] = None
    indicationCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='indication',))
    indicationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='indication',))
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    species: Optional[CodeableConcept] = None


@dataclass
class MedicinalProductDefinition(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinition"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    domain: Optional[Coding] = None
    description: Optional[str] = None
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    indication: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    specialMeasures: Optional[List[str]] = None
    paediatricUseIndicator: Optional[CodeableConcept] = None
    productClassification: Optional[List[CodeableConcept]] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    pharmaceuticalProduct: Optional[List[FHIRReference]] = None
    packagedMedicinalProduct: Optional[List[FHIRReference]] = None
    attachedDocument: Optional[List[FHIRReference]] = None
    masterFile: Optional[List[FHIRReference]] = None
    contact: Optional[List[MedicinalProductDefinitionContact]] = None
    clinicalTrial: Optional[List[FHIRReference]] = None
    name: List[MedicinalProductDefinitionName] = field(default_factory=list)
    crossReference: Optional[List[Identifier]] = None
    manufacturingBusinessOperation: Optional[List[MedicinalProductDefinitionManufacturingBusinessOperation]] = None
    specialDesignation: Optional[List[MedicinalProductDefinitionSpecialDesignation]] = None