#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2019-07-15.
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
class MedicinalProductAuthorization(domainresource.DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorization"
    country: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    dataExclusivityPeriod: Optional[period.Period] = None
    dateOfFirstAuthorization: Optional[fhirdate.FHIRDate] = None
    holder: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    internationalBirthDate: Optional[fhirdate.FHIRDate] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    jurisdictionalAuthorization: Optional[List[MedicinalProductAuthorizationJurisdictionalAuthorization]] = empty_list()
    legalBasis: Optional[codeableconcept.CodeableConcept] = None
    procedure: Optional[MedicinalProductAuthorizationProcedure] = None
    regulator: Optional[fhirreference.FHIRReference] = None
    restoreDate: Optional[fhirdate.FHIRDate] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    statusDate: Optional[fhirdate.FHIRDate] = None
    subject: Optional[fhirreference.FHIRReference] = None
    validityPeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", period.Period, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", fhirdate.FHIRDate, False, None, False),
            ("holder", "holder", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("internationalBirthDate", "internationalBirthDate", fhirdate.FHIRDate, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("legalBasis", "legalBasis", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
            ("restoreDate", "restoreDate", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MedicinalProductAuthorizationJurisdictionalAuthorization(backboneelement.BackboneElement):
    """ Authorization in areas within a country.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    country: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    legalStatusOfSupply: Optional[codeableconcept.CodeableConcept] = None
    validityPeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js

@dataclass
class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationProcedure"
    application: Optional[List[MedicinalProductAuthorizationProcedure]] = empty_list()
    dateDateTime: Optional[fhirdate.FHIRDate] = None
    datePeriod: Optional[period.Period] = None
    identifier: Optional[identifier.Identifier] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False),
            ("dateDateTime", "dateDateTime", fhirdate.FHIRDate, False, "date", False),
            ("datePeriod", "datePeriod", period.Period, False, "date", False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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