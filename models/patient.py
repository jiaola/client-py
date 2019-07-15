#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Patient) on 2019-07-15.
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
class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    resource_type: ClassVar[str] = "Patient"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    birthDate: Optional[fhirdate.FHIRDate] = None
    communication: Optional[List[PatientCommunication]] = empty_list()
    contact: Optional[List[PatientContact]] = empty_list()
    deceasedBoolean: Optional[bool] = None
    deceasedDateTime: Optional[fhirdate.FHIRDate] = None
    gender: Optional[str] = None
    generalPractitioner: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    link: Optional[List[PatientLink]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    maritalStatus: Optional[codeableconcept.CodeableConcept] = None
    multipleBirthBoolean: Optional[bool] = None
    multipleBirthInteger: Optional[int] = None
    name: Optional[List[humanname.HumanName]] = empty_list()
    photo: Optional[List[attachment.Attachment]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDateTime", "deceasedDateTime", fhirdate.FHIRDate, False, "deceased", False),
            ("gender", "gender", str, False, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PatientLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """
    resource_type: ClassVar[str] = "PatientCommunication"
    language:codeableconcept.CodeableConcept = None
    preferred: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js

@dataclass
class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    resource_type: ClassVar[str] = "PatientContact"
    address: Optional[address.Address] = None
    gender: Optional[str] = None
    name: Optional[humanname.HumanName] = None
    organization: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    relationship: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

@dataclass
class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """
    resource_type: ClassVar[str] = "PatientLink"
    other:fhirreference.FHIRReference = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
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