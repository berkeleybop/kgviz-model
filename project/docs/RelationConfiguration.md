
# Class: RelationConfiguration


style for a particular relation (for example, BFO:0000050 or rdfs:subClassOf).

Example of usage, where [relationProperties](relationProperties.md)
specifies a collection of RelationConfigurations keyed by property.

```json
{
    "relationProperties": {
        "rdfs:subClassOf": {
            "color": "black",
            "penwith": 3,
            "arrowhead": "open",
            "label": ""
        },
        "BFO:0000050": {
            "arrowhead": "tee",
            "color": "blue"
        }
    }
}
```

This will render

URI: [kgviz:RelationConfiguration](https://w3id.org/kgviz/RelationConfiguration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StyleSheet]++-%20relationProperties%200..*>[RelationConfiguration&#124;id:Node;color:Color%20%3F;penwidth:integer%20%3F;label:string%20%3F;fontcolor:Color%20%3F;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F],[RelationConfiguration]uses%20-.->[EdgeProperty],[ElementConfiguration]^-[RelationConfiguration],[StyleSheet],[ElementConfiguration],[EdgeProperty])](https://yuml.me/diagram/nofunky;dir:TB/class/[StyleSheet]++-%20relationProperties%200..*>[RelationConfiguration&#124;id:Node;color:Color%20%3F;penwidth:integer%20%3F;label:string%20%3F;fontcolor:Color%20%3F;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F],[RelationConfiguration]uses%20-.->[EdgeProperty],[ElementConfiguration]^-[RelationConfiguration],[StyleSheet],[ElementConfiguration],[EdgeProperty])

## Parents

 *  is_a: [ElementConfiguration](ElementConfiguration.md) - Abstract parent for all coniguration classes

## Uses Mixin

 *  mixin: [EdgeProperty](EdgeProperty.md) - a property object for an edge/relation

## Referenced by Class

 *  **None** *[relationProperties](relationProperties.md)*  <sub>0..\*</sub>  **[RelationConfiguration](RelationConfiguration.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Node](types/Node.md)
 * [color](color.md)  <sub>0..1</sub>
     * Description: Basic drawing color for graphics, not text. For the latter, use the fontcolor attribute.
     * Range: [Color](types/Color.md)
 * [penwidth](penwidth.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Mixed in from GeneralProperty:

 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

### Mixed in from EdgeProperty:

 * [arrowhead](arrowhead.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)

### Mixed in from EdgeProperty:

 * [arrowtail](arrowtail.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)
