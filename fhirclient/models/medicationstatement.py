#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationStatement) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class MedicationStatement(DomainResource):
    """ Record of medication being taken by a patient.

    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains.
    
    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    resource_type: ClassVar[str] = "MedicationStatement"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    category: Optional[CodeableConcept] = None
    context: Optional[FHIRReference] = None
    dateAsserted: Optional[FHIRDate] = None
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    dosage: Optional[List[Dosage]] = empty_list()
    effectiveDateTime: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    identifier: Optional[List[Identifier]] = empty_list()
    informationSource: Optional[FHIRReference] = None
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    note: Optional[List[Annotation]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = empty_list()
    subject: FHIRReference = None

    def elementProperties(self):
        js = super(MedicationStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("context", "context", FHIRReference, False, None, False),
            ("dateAsserted", "dateAsserted", FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("dosage", "dosage", Dosage, True, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("informationSource", "informationSource", FHIRReference, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("note", "note", Annotation, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
        ])
        return js