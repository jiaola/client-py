#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2019-07-22.
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
class MedicinalProductAuthorizationJurisdictionalAuthorization(BackboneElement):
    """ Authorization in areas within a country.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    identifier: Optional[List[Identifier]] = empty_list()
    country: Optional[CodeableConcept] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    legalStatusOfSupply: Optional[CodeableConcept] = None
    validityPeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("country", "country", CodeableConcept, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductAuthorizationProcedure(BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationProcedure"
    identifier: Optional[Identifier] = None
    type: CodeableConcept = None
    datePeriod: Optional[Period] = None
    dateDateTime: Optional[FHIRDate] = None
    application: Optional[List[MedicinalProductAuthorizationProcedure]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("datePeriod", "datePeriod", Period, False, "date", False),
            ("dateDateTime", "dateDateTime", FHIRDate, False, "date", False),
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorization"
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[FHIRReference] = None
    country: Optional[List[CodeableConcept]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    restoreDate: Optional[FHIRDate] = None
    validityPeriod: Optional[Period] = None
    dataExclusivityPeriod: Optional[Period] = None
    dateOfFirstAuthorization: Optional[FHIRDate] = None
    internationalBirthDate: Optional[FHIRDate] = None
    legalBasis: Optional[CodeableConcept] = None
    jurisdictionalAuthorization: Optional[List[MedicinalProductAuthorizationJurisdictionalAuthorization]] = empty_list()
    holder: Optional[FHIRReference] = None
    regulator: Optional[FHIRReference] = None
    procedure: Optional[MedicinalProductAuthorizationProcedure] = None

    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("country", "country", CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("restoreDate", "restoreDate", FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", Period, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", FHIRDate, False, None, False),
            ("internationalBirthDate", "internationalBirthDate", FHIRDate, False, None, False),
            ("legalBasis", "legalBasis", CodeableConcept, False, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("holder", "holder", FHIRReference, False, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False),
        ])
        return js