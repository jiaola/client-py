#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import datarequirement
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"
    dataRequirement: Optional[List[datarequirement.DataRequirement]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    evaluationMessage: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    moduleCanonical: str = None
    moduleCodeableConcept:codeableconcept.CodeableConcept = None
    moduleUri: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    outputParameters: Optional[fhirreference.FHIRReference] = None
    performer: Optional[fhirreference.FHIRReference] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requestIdentifier: Optional[identifier.Identifier] = None
    result: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
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
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
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