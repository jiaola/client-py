#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Encounter) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import duration
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class Encounter(domainresource.DomainResource):
    """ An interaction during which services are provided to the patient.

    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """
    resource_type: ClassVar[str] = "Encounter"
    account: Optional[List[fhirreference.FHIRReference]] = empty_list()
    appointment: Optional[List[fhirreference.FHIRReference]] = empty_list()
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    classHistory: Optional[List[EncounterClassHistory]] = empty_list()
    class_fhir:coding.Coding = None
    diagnosis: Optional[List[EncounterDiagnosis]] = empty_list()
    episodeOfCare: Optional[List[fhirreference.FHIRReference]] = empty_list()
    hospitalization: Optional[EncounterHospitalization] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    length: Optional[duration.Duration] = None
    location: Optional[List[EncounterLocation]] = empty_list()
    partOf: Optional[fhirreference.FHIRReference] = None
    participant: Optional[List[EncounterParticipant]] = empty_list()
    period: Optional[period.Period] = None
    priority: Optional[codeableconcept.CodeableConcept] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    serviceProvider: Optional[fhirreference.FHIRReference] = None
    serviceType: Optional[codeableconcept.CodeableConcept] = None
    status: str = None
    statusHistory: Optional[List[EncounterStatusHistory]] = empty_list()
    subject: Optional[fhirreference.FHIRReference] = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Encounter, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("classHistory", "classHistory", EncounterClassHistory, True, None, False),
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("diagnosis", "diagnosis", EncounterDiagnosis, True, None, False),
            ("episodeOfCare", "episodeOfCare", fhirreference.FHIRReference, True, None, False),
            ("hospitalization", "hospitalization", EncounterHospitalization, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("length", "length", duration.Duration, False, None, False),
            ("location", "location", EncounterLocation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("participant", "participant", EncounterParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("serviceProvider", "serviceProvider", fhirreference.FHIRReference, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EncounterStatusHistory, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class EncounterClassHistory(backboneelement.BackboneElement):
    """ List of past encounter classes.

    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """
    resource_type: ClassVar[str] = "EncounterClassHistory"
    class_fhir:coding.Coding = None
    period:period.Period = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterClassHistory, self).elementProperties()
        js.extend([
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("period", "period", period.Period, False, None, True),
        ])
        return js

@dataclass
class EncounterDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """
    resource_type: ClassVar[str] = "EncounterDiagnosis"
    condition:fhirreference.FHIRReference = None
    rank: Optional[int] = None
    use: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("use", "use", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class EncounterHospitalization(backboneelement.BackboneElement):
    """ Details about the admission to a healthcare service.
    """
    resource_type: ClassVar[str] = "EncounterHospitalization"
    admitSource: Optional[codeableconcept.CodeableConcept] = None
    destination: Optional[fhirreference.FHIRReference] = None
    dietPreference: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    dischargeDisposition: Optional[codeableconcept.CodeableConcept] = None
    origin: Optional[fhirreference.FHIRReference] = None
    preAdmissionIdentifier: Optional[identifier.Identifier] = None
    reAdmission: Optional[codeableconcept.CodeableConcept] = None
    specialArrangement: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    specialCourtesy: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterHospitalization, self).elementProperties()
        js.extend([
            ("admitSource", "admitSource", codeableconcept.CodeableConcept, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("dietPreference", "dietPreference", codeableconcept.CodeableConcept, True, None, False),
            ("dischargeDisposition", "dischargeDisposition", codeableconcept.CodeableConcept, False, None, False),
            ("origin", "origin", fhirreference.FHIRReference, False, None, False),
            ("preAdmissionIdentifier", "preAdmissionIdentifier", identifier.Identifier, False, None, False),
            ("reAdmission", "reAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("specialArrangement", "specialArrangement", codeableconcept.CodeableConcept, True, None, False),
            ("specialCourtesy", "specialCourtesy", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class EncounterLocation(backboneelement.BackboneElement):
    """ List of locations where the patient has been.

    List of locations where  the patient has been during this encounter.
    """
    resource_type: ClassVar[str] = "EncounterLocation"
    location:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    physicalType: Optional[codeableconcept.CodeableConcept] = None
    status: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterLocation, self).elementProperties()
        js.extend([
            ("location", "location", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js

@dataclass
class EncounterParticipant(backboneelement.BackboneElement):
    """ List of participants involved in the encounter.

    The list of people responsible for providing the service.
    """
    resource_type: ClassVar[str] = "EncounterParticipant"
    individual: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterParticipant, self).elementProperties()
        js.extend([
            ("individual", "individual", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class EncounterStatusHistory(backboneelement.BackboneElement):
    """ List of past encounter statuses.

    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """
    resource_type: ClassVar[str] = "EncounterStatusHistory"
    period:period.Period = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(EncounterStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("status", "status", str, False, None, True),
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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