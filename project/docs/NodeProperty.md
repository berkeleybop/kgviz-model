
# Class: NodeProperty




URI: [kgviz:NodeProperty](https://w3id.org/kgviz/NodeProperty)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PrefixConfiguration]uses%20-.->[NodeProperty&#124;color:Color%20%3F;penwidth(i):integer%20%3F;label(i):string%20%3F;fontcolor(i):Color%20%3F],[AnyConfiguration]uses%20-.->[NodeProperty],[GeneralProperty]^-[NodeProperty],[PrefixConfiguration],[GeneralProperty],[AnyConfiguration])](https://yuml.me/diagram/nofunky;dir:TB/class/[PrefixConfiguration]uses%20-.->[NodeProperty&#124;color:Color%20%3F;penwidth(i):integer%20%3F;label(i):string%20%3F;fontcolor(i):Color%20%3F],[AnyConfiguration]uses%20-.->[NodeProperty],[GeneralProperty]^-[NodeProperty],[PrefixConfiguration],[GeneralProperty],[AnyConfiguration])

## Parents

 *  is_a: [GeneralProperty](GeneralProperty.md) - abstract grouping for properties/configs

## Mixin for

 * [AnyConfiguration](AnyConfiguration.md) (mixin)  - Generic configuration that inherits all aspects of both node and edge configurations
 * [PrefixConfiguration](PrefixConfiguration.md) (mixin)  - style for a particular prefix (e.g. GO)

## Referenced by Class


## Attributes


### Own

 * [color](color.md)  <sub>0..1</sub>
     * Description: Basic drawing color for graphics, not text. For the latter, use the fontcolor attribute.
     * Range: [Color](types/Color.md)
 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

### Inherited from GeneralProperty:

 * [penwidth](penwidth.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
