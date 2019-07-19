#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Media) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Media(DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    resource_type: ClassVar[str] = "Media"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    content: Attachment = None
    createdDateTime: Optional[FHIRDate] = None
    createdPeriod: Optional[Period] = None
    device: Optional[FHIRReference] = None
    deviceName: Optional[str] = None
    duration: Optional[float] = None
    encounter: Optional[FHIRReference] = None
    frames: Optional[int] = None
    height: Optional[int] = None
    identifier: Optional[List[Identifier]] = empty_list()
    issued: Optional[FHIRDate] = None
    modality: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()
    operator: Optional[FHIRReference] = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    status: str = None
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    view: Optional[CodeableConcept] = None
    width: Optional[int] = None

    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("content", "content", Attachment, False, None, True),
            ("createdDateTime", "createdDateTime", FHIRDate, False, "created", False),
            ("createdPeriod", "createdPeriod", Period, False, "created", False),
            ("device", "device", FHIRReference, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("modality", "modality", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("operator", "operator", FHIRReference, False, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("view", "view", CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
        ])
        return js