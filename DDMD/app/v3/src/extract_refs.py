import requests
import json
import xml.etree.ElementTree as ET

# Specify the path to your NXML file
xml_file_path = "/Users/eshakya@unomaha.edu/Desktop/Extraction Engine/DDMD/app/v3/data/PMC10054724/ijms-24-05988.xml"

# Open the file and read its contents as a string
with open(xml_file_path, 'r', encoding='utf-8') as file:
    xml_content = file.read()

# Now, nxml_content contains the contents of the NXML file as a string
print(xml_content)

# def fetch_pmc_paper(pmc_id):
#     base_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"
#     params = {"id": pmc_id}
#     response = requests.get(base_url, params=params)
#     print(response.text)
#     data = json.loads(response.text)
#     return data.get("records", [])

# def extract_references(paper):
#     # Extract references from the paper
#     references = []
#     if "references" in paper:
#         references = paper["references"]
#     return references

def make_ref_list():
    # Parse the XML data
    root = ET.fromstring(xml_content)

    # Find the reference list
    ref_list = root.find("ref-list")

    # Initialize a list to store references
    references = []

    # Iterate through each reference in the reference list
    for ref_elem in ref_list.findall("ref"):
        # Extract the reference title
        title_elem = ref_elem.find(".//article-title")
        title = title_elem.text if title_elem is not None else None

        # Extract other relevant information (e.g., authors, year, doi, pmid)
        # Customize this part based on your needs

        # Store the reference information in a dictionary
        reference_info = {
            "title": title,
            # Add other fields as needed
        }

        # Append the reference to the list
        references.append(reference_info)

# Print the list of references
for i, ref in enumerate(references, start=1):
    print(f"Reference {i}: {ref['title']}")
    # Print other information as needed
    print("=" * 30)

# # Example: Fetch a paper and its references
# pmc_id = "PMC10062728"  # Replace with an actual PMC ID
# paper = fetch_pmc_paper(pmc_id)
# references = extract_references(paper)