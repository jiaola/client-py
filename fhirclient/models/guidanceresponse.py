#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class GuidanceResponse(DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"
    dataRequirement: Optional[List[DataRequirement]] = empty_list()
    encounter: Optional[FHIRReference] = None
    evaluationMessage: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    moduleCanonical: str = None
    moduleCodeableConcept: CodeableConcept = None
    moduleUri: str = None
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    outputParameters: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    requestIdentifier: Optional[Identifier] = None
    result: Optional[FHIRReference] = None
    status: str = None
    subject: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", DataRequirement, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("evaluationMessage", "evaluationMessage", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", CodeableConcept, False, "module", True),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, None, False),
            ("outputParameters", "outputParameters", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("requestIdentifier", "requestIdentifier", Identifier, False, None, False),
            ("result", "result", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
        ])
        return js