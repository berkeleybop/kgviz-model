
# Class: EdgeProperty


a property object for an edge/relation

URI: [ex:EdgeProperty](https://w3id.org/kgviz/EdgeProperty)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneralProperty],[RelationConfiguration]uses%20-.->[EdgeProperty&#124;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F;penwidth(i):integer%20%3F;label(i):string%20%3F;fontcolor(i):Color%20%3F],[AnyConfiguration]uses%20-.->[EdgeProperty],[GeneralProperty]^-[EdgeProperty],[RelationConfiguration],[AnyConfiguration])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneralProperty],[RelationConfiguration]uses%20-.->[EdgeProperty&#124;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F;penwidth(i):integer%20%3F;label(i):string%20%3F;fontcolor(i):Color%20%3F],[AnyConfiguration]uses%20-.->[EdgeProperty],[GeneralProperty]^-[EdgeProperty],[RelationConfiguration],[AnyConfiguration])

## Parents

 *  is_a: [GeneralProperty](GeneralProperty.md) - abstract grouping for properties/configs

## Mixin for

 * [AnyConfiguration](AnyConfiguration.md) (mixin)  - Generic configuration that inherits all aspects of both node and edge configurations
 * [RelationConfiguration](RelationConfiguration.md) (mixin)  - style for a particular relation (for example, BFO:0000050 or rdfs:subClassOf).

## Referenced by Class


## Attributes


### Own

 * [arrowhead](arrowhead.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)
 * [arrowtail](arrowtail.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)

### Inherited from GeneralProperty:

 * [penwidth](penwidth.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)
