#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    resource_type: ClassVar[str] = "ImagingStudy"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    description: Optional[str] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    interpreter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    modality: Optional[List[coding.Coding]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    numberOfInstances: Optional[int] = None
    numberOfSeries: Optional[int] = None
    procedureCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    procedureReference: Optional[fhirreference.FHIRReference] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    referrer: Optional[fhirreference.FHIRReference] = None
    series: Optional[List[ImagingStudySeries]] = empty_list()
    started: Optional[fhirdate.FHIRDate] = None
    status: str = None
    subject:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("modality", "modality", coding.Coding, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, True, None, False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """
    resource_type: ClassVar[str] = "ImagingStudySeries"
    bodySite: Optional[coding.Coding] = None
    description: Optional[str] = None
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    instance: Optional[List[ImagingStudySeriesInstance]] = empty_list()
    laterality: Optional[coding.Coding] = None
    modality:coding.Coding = None
    number: Optional[int] = None
    numberOfInstances: Optional[int] = None
    performer: Optional[List[ImagingStudySeriesPerformer]] = empty_list()
    specimen: Optional[List[fhirreference.FHIRReference]] = empty_list()
    started: Optional[fhirdate.FHIRDate] = None
    uid: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("laterality", "laterality", coding.Coding, False, None, False),
            ("modality", "modality", coding.Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js

@dataclass
class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesInstance"
    number: Optional[int] = None
    sopClass:coding.Coding = None
    title: Optional[str] = None
    uid: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("sopClass", "sopClass", coding.Coding, False, None, True),
            ("title", "title", str, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js

@dataclass
class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesPerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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