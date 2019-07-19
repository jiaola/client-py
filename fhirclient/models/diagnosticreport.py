#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DiagnosticReportMedia(BackboneElement):
    """ Key images associated with this report.

    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    resource_type: ClassVar[str] = "DiagnosticReportMedia"
    comment: Optional[str] = None
    link: FHIRReference = None

    def elementProperties(self):
        js = super(DiagnosticReportMedia, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("link", "link", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class DiagnosticReport(DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.

    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    resource_type: ClassVar[str] = "DiagnosticReport"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    conclusion: Optional[str] = None
    conclusionCode: Optional[List[CodeableConcept]] = empty_list()
    effectiveDateTime: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    imagingStudy: Optional[List[FHIRReference]] = empty_list()
    issued: Optional[FHIRDate] = None
    media: Optional[List[DiagnosticReportMedia]] = empty_list()
    performer: Optional[List[FHIRReference]] = empty_list()
    presentedForm: Optional[List[Attachment]] = empty_list()
    result: Optional[List[FHIRReference]] = empty_list()
    resultsInterpreter: Optional[List[FHIRReference]] = empty_list()
    specimen: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("conclusion", "conclusion", str, False, None, False),
            ("conclusionCode", "conclusionCode", CodeableConcept, True, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("imagingStudy", "imagingStudy", FHIRReference, True, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("media", "media", DiagnosticReportMedia, True, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("presentedForm", "presentedForm", Attachment, True, None, False),
            ("result", "result", FHIRReference, True, None, False),
            ("resultsInterpreter", "resultsInterpreter", FHIRReference, True, None, False),
            ("specimen", "specimen", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
        ])
        return js