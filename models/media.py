#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Media) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    resource_type: ClassVar[str] = "Media"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    content:attachment.Attachment = None
    createdDateTime: Optional[fhirdate.FHIRDate] = None
    createdPeriod: Optional[period.Period] = None
    device: Optional[fhirreference.FHIRReference] = None
    deviceName: Optional[str] = None
    duration: Optional[float] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    frames: Optional[int] = None
    height: Optional[int] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    issued: Optional[fhirdate.FHIRDate] = None
    modality: Optional[codeableconcept.CodeableConcept] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    operator: Optional[fhirreference.FHIRReference] = None
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    view: Optional[codeableconcept.CodeableConcept] = None
    width: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("content", "content", attachment.Attachment, False, None, True),
            ("createdDateTime", "createdDateTime", fhirdate.FHIRDate, False, "created", False),
            ("createdPeriod", "createdPeriod", period.Period, False, "created", False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("modality", "modality", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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