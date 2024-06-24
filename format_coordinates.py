#Import coords directly from Izurvive for best results
import sys
def format_coordinates(coord_list):
    coordinates = coord_list.split(" | ")
    formatted_xml = ""
    for coord_pair in coordinates:
        x, z = coord_pair.split(" / ")
        formatted_xml += f'<pos x="{x}" z="{z}" a="-1" />\n'
    return formatted_xml.strip()  # Remove trailing newline

def main():
    coordinates_input = " "
    formatted_xml = format_coordinates(coordinates_input)
    
    print("\nFormatted coordinates in XML format:")
    print(formatted_xml)

if __name__ == "__main__":
    main()
