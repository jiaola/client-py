#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period

from . import domainresource

@dataclass
class RelatedPerson(domainresource.DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    resource_type: ClassVar[str] = "RelatedPerson"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    birthDate: Optional[fhirdate.FHIRDate] = None
    communication: Optional[List[RelatedPersonCommunication]] = empty_list()
    gender: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    name: Optional[List[humanname.HumanName]] = empty_list()
    patient:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    photo: Optional[List[attachment.Attachment]] = empty_list()
    relationship: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", RelatedPersonCommunication, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class RelatedPersonCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    resource_type: ClassVar[str] = "RelatedPersonCommunication"
    language:codeableconcept.CodeableConcept = None
    preferred: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']