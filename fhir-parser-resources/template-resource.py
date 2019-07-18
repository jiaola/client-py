#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} ({{ profile.url }}) on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

{%- set imported = {} %}

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *

{% for imp in imports %}{% if imp.module not in imported %}
from . import {{ imp.module }}
{%- endif %}{% endfor %}

{%- for klass in classes[::-1] %}

{% if klass.superclass in imports and klass.superclass.module not in imported -%}
from . import {{klass.superclass.module}}
{% set _ = imported.update({klass.superclass.module: True}) %}
{% endif -%}

@dataclass
class {{klass.name}}({% if klass.superclass in imports %}{{klass.superclass.module}}.{% endif -%}
{{klass.superclass.name | default('object')}}):
    """ {{ klass.short|wordwrap(width=75, wrapstring="\n    ") }}.
{%- if klass.formal %}

    {{ klass.formal|wordwrap(width=75, wrapstring="\n    ") }}
{%- endif %}
    """

{%- if klass.resource_type %}
    resource_type: ClassVar[str] = "{{ klass.resource_type }}"
{%- endif %}


{%- for prop in klass.properties %}
    {{prop.name}}:{%- if prop.is_array %}{%- if prop.nonoptional %} List[{%- if prop.module_name %}{{prop.module_name}}.{% else %} {% endif %}{{prop.class_name}}]{% else %} Optional[List[{%- if prop.module_name %}{{prop.module_name}}.{% else %}{% endif %}{{prop.class_name}}]]{%- endif %} = empty_list(){% else %}{%- if prop.nonoptional %} {%- if prop.module_name %}{{prop.module_name}}.{% else %} {% endif %}{{prop.class_name}}{% else %} Optional[{%- if prop.module_name %}{{prop.module_name}}.{% else %}{% endif %}{{prop.class_name}}]{%- endif %} = None{% endif %}

{%- endfor %}

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)


{%- if klass.properties %}

    def elementProperties(self):
        js = super({{klass.name}}, self).elementProperties()
        {%- if 'element' == klass.module and 'Element' == klass.name %}
        {%- for imp in imports %}{% if imp.module not in imported %}
        from . import {{imp.module}}
        {%- set _ = imported.update({imp.module: True}) %}
        {%- endif %}{% endfor %}
        {%- endif %}
        js.extend([
        {%- for prop in klass.properties %}
            ("{{ prop.name }}", "{{ prop.orig_name }}",
            {%- if prop.module_name %} {{prop.module_name}}.{% else %} {% endif %}{{prop.class_name}}, {# #}
            {{- prop.is_array}},
            {%- if prop.one_of_many %} "{{ prop.one_of_many }}"{% else %} None{% endif %}, {# #}
            {{- prop.nonoptional}}),
        {%- endfor %}
        ])
        return js

{%- endif %}
{%- endfor %}

{% if imports|length > 0 and imported|length != imports|length %}
import sys
{%- endif %}
{%- for imp in imports %}{% if imp.module not in imported %}
try:
    from . import {{ imp.module }}
except ImportError:
    {{ imp.module }} = sys.modules[__package__ + '.{{ imp.module }}']
{%- endif %}{% endfor %}