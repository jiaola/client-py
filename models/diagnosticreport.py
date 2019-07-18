#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import backboneelement

@dataclass
class DiagnosticReportMedia(backboneelement.BackboneElement):
    """ Key images associated with this report.

    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    resource_type: ClassVar[str] = "DiagnosticReportMedia"
    comment: Optional[str] = None
    link:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DiagnosticReportMedia, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("link", "link", fhirreference.FHIRReference, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.

    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    resource_type: ClassVar[str] = "DiagnosticReport"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    conclusion: Optional[str] = None
    conclusionCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    effectiveDateTime: Optional[fhirdate.FHIRDate] = None
    effectivePeriod: Optional[period.Period] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    imagingStudy: Optional[List[fhirreference.FHIRReference]] = empty_list()
    issued: Optional[fhirdate.FHIRDate] = None
    media: Optional[List[DiagnosticReportMedia]] = empty_list()
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    presentedForm: Optional[List[attachment.Attachment]] = empty_list()
    result: Optional[List[fhirreference.FHIRReference]] = empty_list()
    resultsInterpreter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    specimen: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("conclusion", "conclusion", str, False, None, False),
            ("conclusionCode", "conclusionCode", codeableconcept.CodeableConcept, True, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("media", "media", DiagnosticReportMedia, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True, None, False),
            ("result", "result", fhirreference.FHIRReference, True, None, False),
            ("resultsInterpreter", "resultsInterpreter", fhirreference.FHIRReference, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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