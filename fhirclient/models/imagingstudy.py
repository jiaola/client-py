#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImagingStudySeriesPerformer(BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesPerformer"
    actor: FHIRReference = None
    function: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("function", "function", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ImagingStudySeriesInstance(BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesInstance"
    number: Optional[int] = None
    sopClass: Coding = None
    title: Optional[str] = None
    uid: str = None

    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("sopClass", "sopClass", Coding, False, None, True),
            ("title", "title", str, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


@dataclass
class ImagingStudySeries(BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """
    resource_type: ClassVar[str] = "ImagingStudySeries"
    bodySite: Optional[Coding] = None
    description: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = empty_list()
    instance: Optional[List[ImagingStudySeriesInstance]] = empty_list()
    laterality: Optional[Coding] = None
    modality: Coding = None
    number: Optional[int] = None
    numberOfInstances: Optional[int] = None
    performer: Optional[List[ImagingStudySeriesPerformer]] = empty_list()
    specimen: Optional[List[FHIRReference]] = empty_list()
    started: Optional[FHIRDate] = None
    uid: str = None

    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("laterality", "laterality", Coding, False, None, False),
            ("modality", "modality", Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False),
            ("specimen", "specimen", FHIRReference, True, None, False),
            ("started", "started", FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


@dataclass
class ImagingStudy(DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    resource_type: ClassVar[str] = "ImagingStudy"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    description: Optional[str] = None
    encounter: Optional[FHIRReference] = None
    endpoint: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    interpreter: Optional[List[FHIRReference]] = empty_list()
    location: Optional[FHIRReference] = None
    modality: Optional[List[Coding]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    numberOfInstances: Optional[int] = None
    numberOfSeries: Optional[int] = None
    procedureCode: Optional[List[CodeableConcept]] = empty_list()
    procedureReference: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    referrer: Optional[FHIRReference] = None
    series: Optional[List[ImagingStudySeries]] = empty_list()
    started: Optional[FHIRDate] = None
    status: str = None
    subject: FHIRReference = None

    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("interpreter", "interpreter", FHIRReference, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("modality", "modality", Coding, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("procedureCode", "procedureCode", CodeableConcept, True, None, False),
            ("procedureReference", "procedureReference", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("referrer", "referrer", FHIRReference, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("started", "started", FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
        ])
        return js