#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact


from . import domainresource

@dataclass
class ResearchStudy(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.

    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    resource_type: ClassVar[str] = "ResearchStudy"
    arm: Optional[List[ResearchStudyArm]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    condition: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    description: Optional[str] = None
    enrollment: Optional[List[fhirreference.FHIRReference]] = empty_list()
    focus: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    keyword: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    location: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    objective: Optional[List[ResearchStudyObjective]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    period: Optional[period.Period] = None
    phase: Optional[codeableconcept.CodeableConcept] = None
    primaryPurposeType: Optional[codeableconcept.CodeableConcept] = None
    principalInvestigator: Optional[fhirreference.FHIRReference] = None
    protocol: Optional[List[fhirreference.FHIRReference]] = empty_list()
    reasonStopped: Optional[codeableconcept.CodeableConcept] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    site: Optional[List[fhirreference.FHIRReference]] = empty_list()
    sponsor: Optional[fhirreference.FHIRReference] = None
    status: str = None
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.arm = None
#        """ Defined path through the study for a subject.
#        List of `ResearchStudyArm` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Classifications for the study.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.condition = None
#        """ Condition being studied.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.contact = None
#        """ Contact details for the study.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ What this is study doing.
#        Type `str`
#
#. """
#
#
#        self.enrollment = None
#        """ Inclusion & exclusion criteria.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.focus = None
#        """ Drugs, devices, etc. under study.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business Identifier for study.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.keyword = None
#        """ Used to search for the study.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.location = None
#        """ Geographic region(s) for study.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.note = None
#        """ Comments made about the study.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.objective = None
#        """ A goal for the study.
#        List of `ResearchStudyObjective` items
#
# (represented as `dict` in JSON). """
#
#
#        self.partOf = None
#        """ Part of larger study.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ When the study began and ended.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.phase = None
#        """ n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 |
        phase-2-phase-3 | phase-3 | phase-4.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.primaryPurposeType = None
#        """ treatment | prevention | diagnostic | supportive-care | screening |
        health-services-research | basic-science | device-feasibility.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.principalInvestigator = None
#        """ Researcher who oversees multiple aspects of the study.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.protocol = None
#        """ Steps followed in executing study.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonStopped = None
#        """ accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-
        study-progress | temporarily-closed-per-study-design.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.relatedArtifact = None
#        """ References and dependencies.
#        List of `RelatedArtifact` items
#
# (represented as `dict` in JSON). """
#
#
#        self.site = None
#        """ Facility where study activities are conducted.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.sponsor = None
#        """ Organization that initiates and is legally responsible for the
        study.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | administratively-completed | approved | closed-to-accrual
        | closed-to-accrual-and-intervention | completed | disapproved |
        in-review | temporarily-closed-to-accrual | temporarily-closed-to-
        accrual-and-intervention | withdrawn.
#        Type `str`
#
#. """
#
#
#        self.title = None
#        """ Name for this study.
#        Type `str`
#
#. """
#

#        super(ResearchStudy, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("arm", "arm", ResearchStudyArm, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("condition", "condition", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("enrollment", "enrollment", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("focus", "focus", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("keyword", "keyword", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("location", "location", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("objective", "objective", ResearchStudyObjective, {  # #}True, None, {  # #}False),
            ("partOf", "partOf", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("phase", "phase", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("primaryPurposeType", "primaryPurposeType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("principalInvestigator", "principalInvestigator", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("protocol", "protocol", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("reasonStopped", "reasonStopped", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, {  # #}True, None, {  # #}False),
            ("site", "site", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("sponsor", "sponsor", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("title", "title", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact


from . import backboneelement

@dataclass
class ResearchStudyArm(backboneelement.BackboneElement):
    """ Defined path through the study for a subject.

    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    resource_type: ClassVar[str] = "ResearchStudyArm"
    description: Optional[str] = None
    name: str = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.description = None
#        """ Short explanation of study path.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Label for study arm.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Categorization of study arm.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ResearchStudyArm, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactdetail
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact


@dataclass
class ResearchStudyObjective(backboneelement.BackboneElement):
    """ A goal for the study.

    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    resource_type: ClassVar[str] = "ResearchStudyObjective"
    name: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.name = None
#        """ Label for the objective.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ primary | secondary | exploratory.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ResearchStudyObjective, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js