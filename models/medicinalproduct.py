#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProduct) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import marketingstatus

from . import domainresource

@dataclass
class MedicinalProduct(domainresource.DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProduct"
    additionalMonitoringIndicator: Optional[codeableconcept.CodeableConcept] = None
    attachedDocument: Optional[List[fhirreference.FHIRReference]] = empty_list()
    clinicalTrial: Optional[List[fhirreference.FHIRReference]] = empty_list()
    combinedPharmaceuticalDoseForm: Optional[codeableconcept.CodeableConcept] = None
    contact: Optional[List[fhirreference.FHIRReference]] = empty_list()
    crossReference: Optional[List[identifier.Identifier]] = empty_list()
    domain: Optional[coding.Coding] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    legalStatusOfSupply: Optional[codeableconcept.CodeableConcept] = None
    manufacturingBusinessOperation: Optional[List[MedicinalProductManufacturingBusinessOperation]] = empty_list()
    marketingStatus: Optional[List[marketingstatus.MarketingStatus]] = empty_list()
    masterFile: Optional[List[fhirreference.FHIRReference]] = empty_list()
    name: List[ MedicinalProductName] = empty_list()
    packagedMedicinalProduct: Optional[List[fhirreference.FHIRReference]] = empty_list()
    paediatricUseIndicator: Optional[codeableconcept.CodeableConcept] = None
    pharmaceuticalProduct: Optional[List[fhirreference.FHIRReference]] = empty_list()
    productClassification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    specialDesignation: Optional[List[MedicinalProductSpecialDesignation]] = empty_list()
    specialMeasures: Optional[List[str]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("attachedDocument", "attachedDocument", fhirreference.FHIRReference, True, None, False),
            ("clinicalTrial", "clinicalTrial", fhirreference.FHIRReference, True, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", fhirreference.FHIRReference, True, None, False),
            ("crossReference", "crossReference", identifier.Identifier, True, None, False),
            ("domain", "domain", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("masterFile", "masterFile", fhirreference.FHIRReference, True, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", fhirreference.FHIRReference, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", fhirreference.FHIRReference, True, None, False),
            ("productClassification", "productClassification", codeableconcept.CodeableConcept, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MedicinalProductManufacturingBusinessOperation(backboneelement.BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufacturingBusinessOperation"
    authorisationReferenceNumber: Optional[identifier.Identifier] = None
    confidentialityIndicator: Optional[codeableconcept.CodeableConcept] = None
    effectiveDate: Optional[fhirdate.FHIRDate] = None
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    operationType: Optional[codeableconcept.CodeableConcept] = None
    regulator: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("authorisationReferenceNumber", "authorisationReferenceNumber", identifier.Identifier, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("effectiveDate", "effectiveDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("operationType", "operationType", codeableconcept.CodeableConcept, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class MedicinalProductName(backboneelement.BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductName"
    countryLanguage: Optional[List[MedicinalProductNameCountryLanguage]] = empty_list()
    namePart: Optional[List[MedicinalProductNameNamePart]] = empty_list()
    productName: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("productName", "productName", str, False, None, True),
        ])
        return js

@dataclass
class MedicinalProductNameCountryLanguage(backboneelement.BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameCountryLanguage"
    country:codeableconcept.CodeableConcept = None
    jurisdiction: Optional[codeableconcept.CodeableConcept] = None
    language:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class MedicinalProductNameNamePart(backboneelement.BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameNamePart"
    part: str = None
    type:coding.Coding = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js

@dataclass
class MedicinalProductSpecialDesignation(backboneelement.BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductSpecialDesignation"
    date: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    indicationCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    indicationReference: Optional[fhirreference.FHIRReference] = None
    intendedUse: Optional[codeableconcept.CodeableConcept] = None
    species: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("intendedUse", "intendedUse", codeableconcept.CodeableConcept, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + '.marketingstatus']