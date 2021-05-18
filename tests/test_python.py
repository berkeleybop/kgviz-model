import os
import unittest
from kgviz_model.graphviz import StyleType
from kgviz_model.kgviz import StyleSheet, ReasoningType, RelationConfiguration, Condition, ConditionalProperty, AnyConfiguration
from linkml_runtime.dumpers.json_dumper import JSONDumper
from linkml_runtime.dumpers.yaml_dumper import YAMLDumper
from linkml_runtime.loaders import yaml_loader, json_loader, rdf_loader

CWD = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = os.path.join(CWD, 'input')

SUBCLASS = 'rdfs:subClassOf'
class CreateTestCase(unittest.TestCase):
    """ Test object creation"""
    def test_create(self):
        json_dumper = JSONDumper()
        yaml_dumper = YAMLDumper()
        ss = StyleSheet(styles=[StyleType.filled, StyleType.rounded],
                        fillcolor="white",
                        reasoning=[ReasoningType.transitive_reduction],
                        excludeSingletons=True)
        ss.relationProperties[SUBCLASS] = RelationConfiguration(id='rdfs:subClassOf', color="black")
        ss.conditionalProperties = [
            ConditionalProperty(conditions=Condition(type='owl:Class'),
                                properties=AnyConfiguration(color="red"))
        ]
        #assert StyleType.filled in ss.styles
        print()
        print(ss)
        print(json_dumper.dumps(ss))
        print(yaml_dumper.dumps(ss))
        assert ss is not None

    def test_load(self):
        path = os.path.join(INPUT_DIR, "uberon-zfa-style.json")
        #json_loader.load(path, StyleSheet)
