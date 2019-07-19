#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProduct) on 2019-07-18.
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
class MedicinalProductSpecialDesignation(BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductSpecialDesignation"
    date: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    indicationCodeableConcept: Optional[CodeableConcept] = None
    indicationReference: Optional[FHIRReference] = None
    intendedUse: Optional[CodeableConcept] = None
    species: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", FHIRReference, False, "indication", False),
            ("intendedUse", "intendedUse", CodeableConcept, False, None, False),
            ("species", "species", CodeableConcept, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


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
    countryLanguage: Optional[List[MedicinalProductNameCountryLanguage]] = empty_list()
    namePart: Optional[List[MedicinalProductNameNamePart]] = empty_list()
    productName: str = None

    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("productName", "productName", str, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufacturingBusinessOperation"
    authorisationReferenceNumber: Optional[Identifier] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    effectiveDate: Optional[FHIRDate] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    operationType: Optional[CodeableConcept] = None
    regulator: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("authorisationReferenceNumber", "authorisationReferenceNumber", Identifier, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", CodeableConcept, False, None, False),
            ("effectiveDate", "effectiveDate", FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("operationType", "operationType", CodeableConcept, False, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicinalProduct(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProduct"
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    attachedDocument: Optional[List[FHIRReference]] = empty_list()
    clinicalTrial: Optional[List[FHIRReference]] = empty_list()
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    contact: Optional[List[FHIRReference]] = empty_list()
    crossReference: Optional[List[Identifier]] = empty_list()
    domain: Optional[Coding] = None
    identifier: Optional[List[Identifier]] = empty_list()
    legalStatusOfSupply: Optional[CodeableConcept] = None
    manufacturingBusinessOperation: Optional[List[MedicinalProductManufacturingBusinessOperation]] = empty_list()
    marketingStatus: Optional[List[MarketingStatus]] = empty_list()
    masterFile: Optional[List[FHIRReference]] = empty_list()
    name: List[MedicinalProductName] = empty_list()
    packagedMedicinalProduct: Optional[List[FHIRReference]] = empty_list()
    paediatricUseIndicator: Optional[CodeableConcept] = None
    pharmaceuticalProduct: Optional[List[FHIRReference]] = empty_list()
    productClassification: Optional[List[CodeableConcept]] = empty_list()
    specialDesignation: Optional[List[MedicinalProductSpecialDesignation]] = empty_list()
    specialMeasures: Optional[List[str]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", CodeableConcept, False, None, False),
            ("attachedDocument", "attachedDocument", FHIRReference, True, None, False),
            ("clinicalTrial", "clinicalTrial", FHIRReference, True, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", CodeableConcept, False, None, False),
            ("contact", "contact", FHIRReference, True, None, False),
            ("crossReference", "crossReference", Identifier, True, None, False),
            ("domain", "domain", Coding, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("marketingStatus", "marketingStatus", MarketingStatus, True, None, False),
            ("masterFile", "masterFile", FHIRReference, True, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", FHIRReference, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", CodeableConcept, False, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", FHIRReference, True, None, False),
            ("productClassification", "productClassification", CodeableConcept, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js