#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2019-07-18.
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
class MedicinalProductAuthorizationProcedure(BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationProcedure"
    application: Optional[List[MedicinalProductAuthorizationProcedure]] = empty_list()
    dateDateTime: Optional[FHIRDate] = None
    datePeriod: Optional[Period] = None
    identifier: Optional[Identifier] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False),
            ("dateDateTime", "dateDateTime", FHIRDate, False, "date", False),
            ("datePeriod", "datePeriod", Period, False, "date", False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductAuthorizationJurisdictionalAuthorization(BackboneElement):
    """ Authorization in areas within a country.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    country: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    legalStatusOfSupply: Optional[CodeableConcept] = None
    validityPeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorization"
    country: Optional[List[CodeableConcept]] = empty_list()
    dataExclusivityPeriod: Optional[Period] = None
    dateOfFirstAuthorization: Optional[FHIRDate] = None
    holder: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    internationalBirthDate: Optional[FHIRDate] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    jurisdictionalAuthorization: Optional[List[MedicinalProductAuthorizationJurisdictionalAuthorization]] = empty_list()
    legalBasis: Optional[CodeableConcept] = None
    procedure: Optional[MedicinalProductAuthorizationProcedure] = None
    regulator: Optional[FHIRReference] = None
    restoreDate: Optional[FHIRDate] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    subject: Optional[FHIRReference] = None
    validityPeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", CodeableConcept, True, None, False),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", Period, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", FHIRDate, False, None, False),
            ("holder", "holder", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("internationalBirthDate", "internationalBirthDate", FHIRDate, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("legalBasis", "legalBasis", CodeableConcept, False, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
            ("restoreDate", "restoreDate", FHIRDate, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
        ])
        return js