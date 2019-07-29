#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication) on 2019-07-29.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population
from .quantity import Quantity


@dataclass
class MedicinalProductIndicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndicationOtherTherapy"
    therapyRelationshipType: CodeableConcept = None
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None

    def elementProperties(self):
        js = super(MedicinalProductIndicationOtherTherapy, self).elementProperties()
        js.extend([
            ("therapyRelationshipType", "therapyRelationshipType", CodeableConcept, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
        ])
        return js


@dataclass
class MedicinalProductIndication(DomainResource):
    """ MedicinalProductIndication.

    Indication for the Medicinal Product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndication"
    subject: Optional[List[FHIRReference]] = empty_list()
    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = empty_list()
    intendedEffect: Optional[CodeableConcept] = None
    duration: Optional[Quantity] = None
    otherTherapy: Optional[List[MedicinalProductIndicationOtherTherapy]] = empty_list()
    undesirableEffect: Optional[List[FHIRReference]] = empty_list()
    population: Optional[List[Population]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductIndication, self).elementProperties()
        js.extend([
            ("subject", "subject", FHIRReference, True, None, False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", CodeableConcept, False, None, False),
            ("comorbidity", "comorbidity", CodeableConcept, True, None, False),
            ("intendedEffect", "intendedEffect", CodeableConcept, False, None, False),
            ("duration", "duration", Quantity, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductIndicationOtherTherapy, True, None, False),
            ("undesirableEffect", "undesirableEffect", FHIRReference, True, None, False),
            ("population", "population", Population, True, None, False),
        ])
        return js