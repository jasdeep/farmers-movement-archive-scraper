from utils import get_dt_filename_only, get_pt_filename_only, generate_html

if __name__ == "__main__":
    for source_xml_file in [get_pt_filename_only(), get_dt_filename_only()]:
        generate_html(source_xml_file)
