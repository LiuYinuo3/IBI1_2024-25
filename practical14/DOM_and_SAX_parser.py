from xml.dom import minidom
import xml.sax
from datetime import datetime
import os

# working dictionary
os.chdir("C:/IBI/IBI1_2024-25/practical14")

XML_FILE = "go_obo.xml"

# --- DOM Parser ---
def dom_parse():
    start = datetime.now()
    
    try:
        doc = minidom.parse(XML_FILE)#build DOM tree
    except Exception as e:
        print(f"DOM Parsing Error: {e}")
        return {}, 0
    
    terms = doc.getElementsByTagName("term")#get all of the terms

    results = {
        "molecular_function": (0, "", ""),
        "biological_process": (0, "", ""),
        "cellular_component": (0, "", "")
    }

    for term in terms:
        try:
            ns = term.getElementsByTagName("namespace")[0].firstChild.data
            name = term.getElementsByTagName("name")[0].firstChild.data
            go_id = term.getElementsByTagName("id")[0].firstChild.data
            is_a_list = term.getElementsByTagName("is_a")
            count = len(is_a_list)

            if ns in results and count > results[ns][0]:
                results[ns] = (count, name, go_id)
        except Exception as e:
            print(f"Error processing term: {e}")
            continue

    end = datetime.now()
    duration = (end - start).total_seconds()
    return results, duration

# --- SAX Parser ---
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.results = {
            "molecular_function": (0, "", ""),
            "biological_process": (0, "", ""),
            "cellular_component": (0, "", "")
        }
        self.current_data = ""
        self.current_term = {
            "name": "",
            "namespace": "",
            "id": "",
            "is_a_count": 0
        }
        self.in_term = False

    def startElement(self, name, attrs):
        self.current_data = name
        if name == "term":
            self.in_term = True
            self.current_term = {
                "name": "",
                "namespace": "",
                "id": "",
                "is_a_count": 0
            }

    def endElement(self, name):
        if name == "term" and self.in_term:
            ns = self.current_term["namespace"]
            count = self.current_term["is_a_count"]
            if ns in self.results and count > self.results[ns][0]:
                self.results[ns] = (
                    count,
                    self.current_term["name"],
                    self.current_term["id"]
                )
            self.in_term = False
        elif name == "is_a" and self.in_term:
            self.current_term["is_a_count"] += 1
        self.current_data = ""

    def characters(self, content):
        if self.in_term and self.current_data in ["name", "namespace", "id"]:
            self.current_term[self.current_data] += content.strip()

def sax_parse():
    start = datetime.now()
    
    try:
        parser = xml.sax.make_parser()
        handler = GOHandler()
        parser.setContentHandler(handler)
        parser.parse(XML_FILE)
    except Exception as e:
        print(f"SAX Parsing Error: {e}")
        return {}, 0
    
    end = datetime.now()
    duration = (end - start).total_seconds()
    return handler.results, duration

# --- Main Function ---
def main():
    print("Gene Ontology XML Parsing Analysis")
    print("=" * 50)
    
    # Run DOM parser
    print("\nRunning DOM parser...")
    dom_results, dom_time = dom_parse()
    
    # Run SAX parser
    print("\nRunning SAX parser...")
    sax_results, sax_time = sax_parse()
    
    # Print results
    print("\nResults Summary:")
    print("-" * 50)
    print(f"{'Namespace':<25} {'GO Term Name':<40} {'GO ID':<15} {'is_a Count':<10}")
    print("-" * 50)
    
    print("\nDOM Parser Results:")
    for ns, (count, name, go_id) in dom_results.items():
        print(f"{ns:<25} {name[:35]:<40} {go_id:<15} {count:<10}")
    
    print("\nSAX Parser Results:")
    for ns, (count, name, go_id) in sax_results.items():
        print(f"{ns:<25} {name[:35]:<40} {go_id:<15} {count:<10}")
    
    # Performance comparison
    print("\nPerformance Comparison:")
    print(f"DOM parsing time: {dom_time:.4f} seconds")
    print(f"SAX parsing time: {sax_time:.4f} seconds")
    
    if dom_time < sax_time:
        print("\nDOM parsing was faster by {:.2f} seconds".format(sax_time - dom_time))
    elif sax_time < dom_time:
        print("\nSAX parsing was faster by {:.2f} seconds".format(dom_time - sax_time))
    else:
        print("\nBoth methods took the same time.")
    
    print("\nNote: SAX is generally more memory-efficient for large files,")
    print("while DOM provides easier access to the document structure.")

if __name__ == "__main__":
    main()

# Based on this run, SAX was faster.