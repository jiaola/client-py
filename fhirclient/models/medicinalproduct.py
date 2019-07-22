#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProduct) on 2019-07-22.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus


@dataclass
class MedicinalProductNameNamePart(BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameNamePart"
    part: str = None
    type: Coding = None

    def elementProperties(self):
        js = super(MedicinalProductNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", Coding, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductNameCountryLanguage(BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameCountryLanguage"
    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    language: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicinalProductNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", CodeableConcept, False, None, False),
            ("language", "language", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductName(BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductName"
    productName: str = None
    namePart: Optional[List[MedicinalProductNameNamePart]] = empty_list()
    countryLanguage: Optional[List[MedicinalProductNameCountryLanguage]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("productName", "productName", str, False, None, True),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufacturingBusinessOperation"
    operationType: Optional[CodeableConcept] = None
    authorisationReferenceNumber: Optional[Identifier] = None
    effectiveDate: Optional[FHIRDate] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    regulator: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("operationType", "operationType", CodeableConcept, False, None, False),
            ("authorisationReferenceNumber", "authorisationReferenceNumber", Identifier, False, None, False),
            ("effectiveDate", "effectiveDate", FHIRDate, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductSpecialDesignation(BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductSpecialDesignation"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[CodeableConcept] = None
    intendedUse: Optional[CodeableConcept] = None
    indicationCodeableConcept: Optional[CodeableConcept] = None
    indicationReference: Optional[FHIRReference] = None
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    species: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("intendedUse", "intendedUse", CodeableConcept, False, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", FHIRReference, False, "indication", False),
            ("status", "status", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("species", "species", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicinalProduct(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProduct"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[CodeableConcept] = None
    domain: Optional[Coding] = None
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    specialMeasures: Optional[List[str]] = empty_list()
    paediatricUseIndicator: Optional[CodeableConcept] = None
    productClassification: Optional[List[CodeableConcept]] = empty_list()
    marketingStatus: Optional[List[MarketingStatus]] = empty_list()
    pharmaceuticalProduct: Optional[List[FHIRReference]] = empty_list()
    packagedMedicinalProduct: Optional[List[FHIRReference]] = empty_list()
    attachedDocument: Optional[List[FHIRReference]] = empty_list()
    masterFile: Optional[List[FHIRReference]] = empty_list()
    contact: Optional[List[FHIRReference]] = empty_list()
    clinicalTrial: Optional[List[FHIRReference]] = empty_list()
    name: List[MedicinalProductName] = empty_list()
    crossReference: Optional[List[Identifier]] = empty_list()
    manufacturingBusinessOperation: Optional[List[MedicinalProductManufacturingBusinessOperation]] = empty_list()
    specialDesignation: Optional[List[MedicinalProductSpecialDesignation]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("domain", "domain", Coding, False, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", CodeableConcept, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", CodeableConcept, False, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", CodeableConcept, False, None, False),
            ("productClassification", "productClassification", CodeableConcept, True, None, False),
            ("marketingStatus", "marketingStatus", MarketingStatus, True, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", FHIRReference, True, None, False),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", FHIRReference, True, None, False),
            ("attachedDocument", "attachedDocument", FHIRReference, True, None, False),
            ("masterFile", "masterFile", FHIRReference, True, None, False),
            ("contact", "contact", FHIRReference, True, None, False),
            ("clinicalTrial", "clinicalTrial", FHIRReference, True, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("crossReference", "crossReference", Identifier, True, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
        ])
        return js