#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import domainresource
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext

from . import backboneelement

@dataclass
class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.

    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    resource_type: ClassVar[str] = "StructureMapStructure"
    alias: Optional[str] = None
    documentation: Optional[str] = None
    mode: str = None
    url: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js

@dataclass
class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTargetParameter"
    valueBoolean: bool = None
    valueDecimal: float = None
    valueId: str = None
    valueInteger: int = None
    valueString: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js

@dataclass
class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTarget"
    context: Optional[str] = None
    contextType: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[List[str]] = empty_list()
    listRuleId: Optional[str] = None
    parameter: Optional[List[StructureMapGroupRuleTargetParameter]] = empty_list()
    transform: Optional[str] = None
    variable: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js

@dataclass
class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleSource"
    check: Optional[str] = None
    condition: Optional[str] = None
    context: str = None
    defaultValueAddress: Optional[address.Address] = None
    defaultValueAge: Optional[age.Age] = None
    defaultValueAnnotation: Optional[annotation.Annotation] = None
    defaultValueAttachment: Optional[attachment.Attachment] = None
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    defaultValueCoding: Optional[coding.Coding] = None
    defaultValueContactDetail: Optional[contactdetail.ContactDetail] = None
    defaultValueContactPoint: Optional[contactpoint.ContactPoint] = None
    defaultValueContributor: Optional[contributor.Contributor] = None
    defaultValueCount: Optional[count.Count] = None
    defaultValueDataRequirement: Optional[datarequirement.DataRequirement] = None
    defaultValueDate: Optional[fhirdate.FHIRDate] = None
    defaultValueDateTime: Optional[fhirdate.FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueDistance: Optional[distance.Distance] = None
    defaultValueDosage: Optional[dosage.Dosage] = None
    defaultValueDuration: Optional[duration.Duration] = None
    defaultValueExpression: Optional[expression.Expression] = None
    defaultValueHumanName: Optional[humanname.HumanName] = None
    defaultValueId: Optional[str] = None
    defaultValueIdentifier: Optional[identifier.Identifier] = None
    defaultValueInstant: Optional[fhirdate.FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueMoney: Optional[money.Money] = None
    defaultValueOid: Optional[str] = None
    defaultValueParameterDefinition: Optional[parameterdefinition.ParameterDefinition] = None
    defaultValuePeriod: Optional[period.Period] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueQuantity: Optional[quantity.Quantity] = None
    defaultValueRange: Optional[range.Range] = None
    defaultValueRatio: Optional[ratio.Ratio] = None
    defaultValueReference: Optional[fhirreference.FHIRReference] = None
    defaultValueRelatedArtifact: Optional[relatedartifact.RelatedArtifact] = None
    defaultValueSampledData: Optional[sampleddata.SampledData] = None
    defaultValueSignature: Optional[signature.Signature] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[fhirdate.FHIRDate] = None
    defaultValueTiming: Optional[timing.Timing] = None
    defaultValueTriggerDefinition: Optional[triggerdefinition.TriggerDefinition] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUsageContext: Optional[usagecontext.UsageContext] = None
    defaultValueUuid: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[str] = None
    logMessage: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    type: Optional[str] = None
    variable: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", str, False, None, True),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js

@dataclass
class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleDependent"
    name: str = None
    variable: List[ str] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("variable", "variable", str, True, None, True),
        ])
        return js

@dataclass
class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRule"
    dependent: Optional[List[StructureMapGroupRuleDependent]] = empty_list()
    documentation: Optional[str] = None
    name: str = None
    rule: Optional[List[StructureMapGroupRule]] = empty_list()
    source: List[ StructureMapGroupRuleSource] = empty_list()
    target: Optional[List[StructureMapGroupRuleTarget]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
        ])
        return js

@dataclass
class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.

    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    resource_type: ClassVar[str] = "StructureMapGroupInput"
    documentation: Optional[str] = None
    mode: str = None
    name: str = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.

    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    resource_type: ClassVar[str] = "StructureMapGroup"
    documentation: Optional[str] = None
    extends: Optional[str] = None
    input: List[ StructureMapGroupInput] = empty_list()
    name: str = None
    rule: List[ StructureMapGroupRule] = empty_list()
    typeMode: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("typeMode", "typeMode", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    resource_type: ClassVar[str] = "StructureMap"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    group: List[ StructureMapGroup] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    import_fhir: Optional[List[str]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    structure: Optional[List[StructureMapStructure]] = empty_list()
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
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
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']